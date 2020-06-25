#! /usr/bin/env python
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
import pkg_resources


#Input parameters
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
print(sys.argv[5])
print(sys.argv[6])


infile = sys.argv[1]
outfile = sys.argv[2]
#cm = sys.argv[3]
cm = pkg_resources.resource_filename('tboxscan', sys.argv[3])
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

if path.exists(pkg_resources.resource_filename('tboxscan', 'data/rccodonLUT.csv'))==False:
    print('Error: Missing amino acid LUT file '+pkg_resources.resource_filename('tboxscan', 'data/rccodonLUT.csv')+'.')


#Look up table for amino acid family predictions
aalut=pd.read_csv(pkg_resources.resource_filename('tboxscan', 'data/rccodonLUT.csv'))
 
#Remove previous out file
os.system('rm '+outfile+' >/dev/null 2> /dev/null')
 
#Run cmsearch
os.system('cmsearch --notrunc --notextw '+cm+' '+infile+' > '+infernal+' 2> /dev/null')

#Run pipeline
os.system('python3 -m tboxscan.pipeline_master.py '+infernal+' '+outfile+' '+infile+' $3 > '+logfile)

#Read output file
#try:
if 1>0:
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
        
        
#except:
 #   print('Error: Failed to detect T-boxes in '+infile+' using '+cm)


