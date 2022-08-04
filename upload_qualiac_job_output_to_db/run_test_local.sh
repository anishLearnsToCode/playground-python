#!/bin/bash

# enter the project dir
cd ~/projects/playground-python/upload_qualiac_job_output_to_db

# create virtual environment if doesn't exist
if [ ! -d "venv" ]
then
  python3 -m venv venv
fi

# activate the virtual env
source venv/scripts/activate

# install all required dependencies
pip install -r requirements.txt

# run the main python script
python driver.py

# inactivate the virtual env
deactivate
