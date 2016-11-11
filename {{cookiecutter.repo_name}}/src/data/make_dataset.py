#!/usr/bin/env python

# will create a sym link of a biom table found within the given directory
# specified by argv[1]
# NOTE: will use the .biom table with longest name found in dir


import sys, os

# GLOBALS
job_num = sys.argv[1]
job_dir = '/home/data_repo/pre_processing/jobs/%s/stage_2/otupick/' %job_num

# get OTU table with longest name
tables = [f for f in os.listdir(job_dir) if '.biom' in f]
biom = sorted(tables)[-1]

comm = "ln -s %s/%s data/raw/" %(job_dir, biom)
os.system(comm)
