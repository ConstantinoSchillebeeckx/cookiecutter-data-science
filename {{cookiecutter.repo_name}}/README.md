{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make clean`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Data generated during the data analysis process, e.g. stats file.
    │   ├── pcoa           <- Generated PCOA plots.
    │   ├── phylo          <- Generated phylogenetic trees.
    │   └── raw            <- The original, immutable data dump including OTU table and mapping file.
    │
    ├── docs               <- MkDocs
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   |                     a short `-` delimited description, and initials (if needed) e.g.
    │   |                     `1.0-jqp-initial-data-exploration-CS`.
    │   ├── explore        <- Initial exploratory work
    │   └── reports        <- Polished work that can be exported as html to the reports directory
    │       |
    │       └── figures    <- Any figure referenced in a reports notebook should use this dir as
    │                         the reference src directory; this acts as a symlink to the main
    │                         reports/figures/ directory.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── setup          <- Scripts generically used at time of project setup
    │   │   └── setup_git_repo.sh
    │   │
    │   └── viz            <- Scripts to create exploratory and results oriented visualizations
    │
    └── test_environment.py
