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




#################################################################################
# NEXT STEPS                                                                    #
#################################################################################
print "\n\nCongrats! Your data analysis project directory has been created at: %s" %repo_name

if job_num.isdigit():
    print "\nSince you specified a job number (%s) you'll want to run 'make' from within the" %job_num
    print "project directory and use the command 'data' to setup your /data/raw files."



#################################################################################
# SETUP GITHUB REPO                                                             #
#################################################################################
if setup_git:
    git_user = raw_input("\nPlease enter your GitHub user name: ")

    comm = "git init .; git add .; git commit -m 'initial commit';"
    comm += "git remote add origin git@github.com:%s/%s.git;" %(git_user, repo_name)
    comm += "git push -u origin master"

    err = os.system(comm)

    if err:
        sys.exit(1)




if __name__ == '__main__':
    main()
