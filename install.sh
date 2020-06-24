#!/bin/bash
#Initialize T-box predictions pipeline

echo "Installing dependencies"
conda init bash
conda env create -f environment.yml
conda activate tbdb

echo "Exporting path to .bash_profile"

echo "alias tbox-scan='./tbox-scan.sh'" >> ~/.bash_profile
echo 'export PATH=${PATH}:'"$(pwd)/tbox-scan" >> ~/.bash_profile
