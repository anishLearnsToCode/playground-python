#!/bin/bash

# enter the project dir
cd /usr/cern/unixScripts/upload_qualiac_job_output_to_db

# create virtual environment if doesn't exist
if [ ! -d "venv" ]
then
  python3 -m venv venv
fi

# activate the virtual env
source venv/bin/activate

# install all required dependencies
pip --proxy aisproxy:3128 install -r requirements.txt

# run the main python script
python3 driver.py PROD

# inactivate the virtual env
deactivate
