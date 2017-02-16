#!/usr/bin/env python
"""

Script is run after cookiecutter creates its cookie and will:
- print next step text
- setup GitHub repo if requested

"""

import sys, os

#################################################################################
# GLOBALS                                                                       #
#################################################################################
job_num = '{{ cookiecutter.job_dir }}'
repo_name = '{{ cookiecutter.repo_name }}'
setup_git = True if '{{ cookiecutter.setup_git_repo }}' == "Yes" else False
private = True if '{{ cookiecutter.open_source_license }}' == 'Not open source' else False


#################################################################################
# SETUP SYMLINK (CANT GET IT TO WORK IN REPO)                                   #
#################################################################################
os.system("ln -s ../../reports/figures/ notebooks/reports/")
#os.system("ln -s ../../data/interim/ notebooks/explore/")



#################################################################################
# SETUP PERMISSIONS TO WORK WITH KOMPYUTA
#################################################################################
os.system('chgrp -R writers .')
os.system('chmod -R g+w .')
 


#################################################################################
# NEXT STEPS                                                                    #
#################################################################################
print "\n==----------------------------------------------------------------------------------------=="
print "Congrats! Your data analysis project directory has been created at: %s" %repo_name

if job_num.isdigit():
    print "\nSince you specified a job number (%s) you'll want to run 'make' from within the" %job_num
    print "project directory and use the command 'data' to setup your /data/raw files."

print "==----------------------------------------------------------------------------------------==\n"


#################################################################################
# SETUP GITHUB REPO                                                             #
#################################################################################
if setup_git:

    err = os.system('bash src/setup/setup_git_repo.sh %s' %repo_name)
    if err: print "Error with GitHub repo setup!"
        

#################################################################################
# SETUP MKDOCS                                                                  #
#################################################################################
if not private and setup_git:
    os.system("mkdocs build")
    os.system("mkdocs gh-deploy")




#################################################################################
# MOVE INTO PROJECT DIR                                                         #
#################################################################################
#os.system("cd %s" %repo_name)
