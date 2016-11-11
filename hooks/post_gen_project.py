# Script is run after cookiecutter creates its cookie and will:
# - create a symlink of OTU table if job_dir was specified

import sys


job_dir = '{{ cookiecutter.job_dir }}'
repo = '{{ cookiecutter.module_name }}'

if job_dir.isdigit():
    print "job_dir repo"
