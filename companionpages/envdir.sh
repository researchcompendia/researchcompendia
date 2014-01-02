#!/bin/bash

# a convienence script so that I don't have to type the
# entire envdir command everytime.
#
# more on envdir: https://github.com/jezdez/envdir
#
# this script requires that there is a directory structure like so:
# 
# env
# ├── local
# ├── preprod
# ├── prod
#
# and that filenames exist in each directory that correspond
# to environment variables used by researchcompendia in settings.py 

if [ -z "$1" ]; then
    echo "usage: envdir.sh <local|prod|staging>"
    exit
fi

ENV=$1
case "$ENV" in
    local) ;;
    prod) ;;
    staging) ;;
    *) echo "invalid environment: $ENV"; exit ;;
esac

envdir env/$ENV python manage.py runserver --traceback -v 3
