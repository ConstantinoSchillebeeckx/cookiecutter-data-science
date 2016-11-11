#!/usr/bin/env python
"""

Script is run after cookiecutter creates its cookie and will:
- create a symlink of OTU table if job_dir was specified

"""

import sys, os

#################################################################################
# GLOBALS                                                                       #
#################################################################################
job_num = '{{ cookiecutter.job_dir }}'
job_dir = os.path.join('/home/data_repo/pre_processing/jobs/', job_num, 'stage_2/otupick/')
repo = '{{ cookiecutter.module_name }}'
repo_data_dir = os.path.join(repo, 'data/raw/')







#################################################################################
# OTU TABLE DATA                                                                #
#################################################################################
if job_num.isdigit():

    # assumes user wants the .biom file that has the longest name
    otu_tables = [f for f in os.listdir(job_dir) if '.biom' in f]
    table = os.path.join(job_dir, sorted(otu_tables)[-1])

    print "Copying OTU table from job %s to %s." %(job_dir, repo_data_dir)
    comm = "ln -s %s %s" %(table, repo_data_dir)
    os.system(comm)
