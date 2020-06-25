#!/bin/bash
#Initialize T-box predictions pipeline

echo "Installing dependencies"
conda init bash
conda env create -f environment.yml

source activate tbdb

echo "Exporting path to .bash_profile"

echo "" >> ~/.bash_profile
echo 'export PATH=${PATH}:'"$(pwd)" >> ~/.bash_profile
echo "alias tbox-scan='sh tbox-scanner'" >> ~/.bash_profile

#exec bash
