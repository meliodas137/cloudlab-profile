#!/bin/bash

git clone https://github.com/Clive2312/duckdb
echo "Installing Tools...\n"
sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt install cmake
echo "Done...\nInstalling Dependencies...\n"
pip install numpy
pip install pandas
cd ./duckdb/examples/embedded-c++/gen_db/
echo "Generating data...\n"
python genDB.py
echo "Ready!"