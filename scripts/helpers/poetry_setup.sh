#!/usr/bin/env bash

###############################################################################
#
# Setup poetry for project.
#
###############################################################################

script_name="$(basename -- "$0")"

# Formats
bold="\033[1m"
green="\033[0;32m"
red="\033[91m"
no_color="\033[0m"

poetry config virtualenvs.create false

echo -e "\n${green}Poetry config:${no_color}"
poetry config --list
