#!/bin/sh


# Script is run after cookiecutter creates its cookie and will:
# - create a symlink of OTU table if job_dir was specified




job_dir="/home/data_repo/pre_processing/jobs/{{ cookiecutter.job_dir }}"
repo="{{ cookiecutter.repository }}"

if [ -z "$VAR" ]; then
    echo "ln -s $job_dir $repo"   
fi
