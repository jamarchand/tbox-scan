#!/bin/bash
#Initialize T-box predictions pipeline

echo "Installing trnascan python scripts to current python environment"
pip install -i https://test.pypi.org/simple/ tboxscan==0.5.15

echo "Exporting path to .bash_profile"
echo "" >> ~/.bash_profile
echo 'export PATH=${PATH}:'"$(pwd)" >> ~/.bash_profile


echo "Changing permissions for executable"
chmod +x tbox-scan


