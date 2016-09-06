# Mendel,MD
An online tool for annotating, filtering and diagnosing Humans (Exome and Genome) with Mendelian Disorders.


Requirements
============

* Python 3.4+
* Perl 5.8+
* Java 1.8
* Ubuntu LTS 16.04

Other Libraries Needed
======================

* [pynnotator](https://github.com/raonyguimaraes/pynnotator)


OMIM Data
=========

You need to register an account at OMIM: http://omim.org/downloads and submit a download request to get a file named "morbidmap".

After obtaining this file you need to put it on this folder: "mendelmd_source/data/omim/".

Installation on Ubuntu 16.04 LTS (tested)
=========================================
    sudo apt-get install gcc git python3-dev zlib1g-dev virtualenvwrapper
    source /etc/bash_completion.d/virtualenvwrapper
    git clone https://github.com/raonyguimaraes/mendelmd.git
    cd mendelmd/mendelmd_source
    mkvirtualenv -p /usr/bin/python3 mendelmd


Installing the Pynnotator
========================

    pip install cython
    pip install pynnotator
    pynnotator install

This will take a long time since it will download around 26GB of data. Go grab a coffee and read a paper.

Installing PostgreSQL Database
==============================

    sudo apt-get install libpq-dev postgresql
    sudo su
    su postgres
    psql template1
    CREATE USER mendelmd WITH PASSWORD 'mendelmd';
    CREATE DATABASE mendelmd;
    GRANT ALL PRIVILEGES ON DATABASE mendelmd to mendelmd;
    \q


Installing Mendel,MD
====================

    pip install -r requirements.stable.txt

    python manage.py migrate auth
    
    #ignore the following error: django.db.utils.ProgrammingError: relation "django_site" does not exist

    python manage.py migrate
    python manage.py populate
    python manage.py createsuperuser
    python manage.py runserver

And now you should have Mendel,MD running on address http://127.0.0.1:8000/

Creating a superuser
====================

    python manage.py createsuperuser

Importing Data
==============

    python manage.py populate

Upload your VCFs using the web interface
========================================

Start the annotation
====================

    python manage.py celery worker
