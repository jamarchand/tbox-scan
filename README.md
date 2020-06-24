# About tbox-scan
A lightweight tool for discovering tboxes in a given FASTA sequence adapted from tbdb.io. Uses INFERNAL for prediction and allows for flexible use of covariance models. As output, provides predicted specifier region, most likely specifier, and the T-box sequence. 


# Dependencies 
tbox-scan runs requires INFERNAL, python, conda, pandas. Installation of dependencies is easiest using conda with the given installation file. 

# Installation
Have conda installed, then simply run install.sh (e.g. sh ./install.sh) to install tbox-scan. 

# Using tbox-scan 
  
    Usage: tbox-scan -f <Input FASTA file> [-options]

    Scan a fasta sequence file for T-boxes and predict specifier & T-box sequence.
              -- Default: Will use INFERNAL with RFAM00230 covariance model with basic output
              -- Example: tbox-scan  -f input.fa -o output_file.csv -v
    Dependencies: INFERNAL, cmsearch, python3, pandas.


    Options
      -f <file>  : input FASTA <file>
      -o <file>  : save final results in <file> as .csv
      -i <file>  : save INFERNAL output predictions to .txt <file>
                      default: INFERNAL.txt
      -l <file>  : save a .txt log <file> of pipeline output
      -m <model> : search for mitochondrial tRNAs
                      default: RF00230.cm (RFAM)
      -v         : save verbose output
      -s         : silence console output
      -h         : print out summary of available options
