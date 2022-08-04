#!/bin/bash

cd /usr/cern/unixScripts/aoi_form

#Before running your script, activate the venv
source .venv/bin/activate

#Run the script
python3 ./aoi.py PROD >> ./aoi.log
