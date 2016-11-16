#!/usr/bin/env python

# Makefile python script to generate starting dataset.

# will create a sym link of a biom table found within the given directory
# specified by argv[1]
# NOTE: will use the .biom table with longest name found in dir

# any other data generating steps (e.g. filter biom table, create mapping file)
# should be manually appended to this script.


import sys, os

# GLOBALS
job_num = sys.argv[1]
job_dir = '/home/data_repo/pre_processing/jobs/%s/stage_2/otupick/' %job_num


# CLEAN OUT DIR
os.system("rm -rf data/raw/*")

# get OTU table with longest name
tables = [f for f in os.listdir(job_dir) if '.biom' in f]
biom = sorted(tables)[-1]

comm = "ln -s %s/%s data/raw/" %(job_dir, biom)
err = os.system(comm)

if err:
    print "An error occurred while generating the symlink for data/raw/"
else:
    print "Symlink properly generated in data/raw/"

# COPY REP_SET
os.system("ln -s -f %/rep_set.fna data/raw" %(job_dir)) 
os.system("ln -s -f %/rep_set.tre data/raw" %(job_dir)) 
