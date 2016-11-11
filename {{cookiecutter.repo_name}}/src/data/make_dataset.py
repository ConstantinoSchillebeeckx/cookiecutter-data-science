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

comm = "ln -s -f %s/%s data/raw/" %(job_dir, biom)
err = os.system(comm)

if err:
    print "An error occurred while generating the symlink for data/raw/"
else:
    print "Symlink properly generated in data/raw/"
