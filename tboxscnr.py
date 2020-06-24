#tbox_pipeline_master.py
#By Merrick Pierson Smela 
#Reads INFERNAL output data and calculates T-box features
#Also calculates thermodynamic parameters (code by Thomas Jordan)
import os
import pandas as pd
import sys



infile = 'test.fa'
outfile = 'out.csv'

aalut=pd.read_csv('rccodonLUT.csv')
 
os.system('cmsearch --notrunc --notextw RF00230.cm '+infile+' > INFERNAL.txt')
os.system('python3 pipeline_master.py INFERNAL.txt '+outfile+' '+infile+' $3 > log.txt')
out = pd.read_csv(outfile)
print(out)
print('\n')
print('Running T-box scanner on '+infile)
print('\n')

aalist=[None]*len(out)
for i in range (0,len(out)):
    aalist[i]='T-box '+aalut.loc[aalut['AC']==out['codon'].iloc[i],['AA']].values[0][0]

out['AA']=aalist
outmess=out[['AA','Tbox_start', 'Tbox_end', 'codon_region', 'codon', 'discriminator', 'Score']]


print(outmess)
print('\n\n')
