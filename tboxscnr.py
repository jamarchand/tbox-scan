#Tbox-scan
#Version 1.0.0.
#Updated June 24, 2020
#By Merrick Pierson Smela and Jorge A. Marchand
#Harvard Medical School - Department of Genetics
#George M. Church Lab

import os
import pandas as pd
from os import path
import sys


#Input parameters
infile = sys.argv[1]
outfile = sys.argv[2]
cm = sys.argv[3]
infernal = sys.argv[4]
logfile = sys.argv[5]
verbose = sys.argv[6]
silence = sys.argv[7]


#Initialize
print('\nRunning T-box scanner on '+infile+'\n')

#Check files exist
if path.exists(infile)==False:
    print('Error: Input file '+infile+' does not exist.')

if path.exists(cm)==False:
    print('Error: Covariance model '+cm+' does not exist.')

if path.exist('rccodonLUT.csv')==False:
    print('Error: Missing amino acid LUT file '+cm+'.')


#Look up table for amino acid family predictions
aalut=pd.read_csv('rccodonLUT.csv')
 
#Remove previous out file
os.system('rm '+outfile+' >/dev/null 2> /dev/null')
 
#Run cmsearch
os.system('cmsearch --notrunc --notextw '+cm+' '+infile+' > '+infernal+' 2> /dev/null')

#Run pipeline
os.system('python pipeline_master.py '+infernal+' '+outfile+' '+infile+' $3 > '+logfile+' 2> /dev/null')

#Read output file
try:
    out = pd.read_csv(outfile)
    #Perform aa family lookup using LUT
    aalist=[None]*len(out)
    for i in range (0,len(out)):
        try:
            aalist[i]='T-box '+aalut.loc[aalut['AC']==out['codon'].iloc[i],['AA']].values[0][0]
        except IndexError: #codon not in LUT
            aalist[i]="Unknown"
    out['AA']=aalist

    #Parse for locus from output file, generate print out response
    out['Locus'] = out['Name'].str.split(':').str[-1]
    outmess=out[['Locus','Score','AA', 'codon_region', 'codon', 'discriminator']]
    outmess.columns=['Locus', 'Score', 'AA Family', 'Spec_Region', 'Specifier', 'T-box Seq']

    #Write output
    if verbose == 'True':
        out.to_csv(outfile)
    elif verbose == 'False':
        outmess.to_csv(outfile)

    #Print output
    if silence == 'False':
        print(outmess)
        print('\n\n')
        
        
except:
    print('Error: Failed to detect T-boxes in '+infile+' using '+cm)


