#!/usr/bin/env bash

###############################################################################
#
# Locate conda binary files.
# Purpose to source conda and enable conda commands.
# To be used in scripts requiring conda.
#
###############################################################################

script_name="$(basename -- "$0")"

# Formats
bold="\033[1m"
green="\033[0;32m"
red="\033[91m"
no_color="\033[0m"

echo -e "${green}Sourcing conda commands...${no_color}"

if [[ $CONDA_BIN ]]; then
    conda_bin_dir=$CONDA_BIN
else
    conda_bin_dir=$(which conda | sed "s|/conda$||")
fi

if [[ ! ${conda_bin_dir} ]]; then
    echo -e "${red}ERROR: Not able to locate the conda bin directory."\
    "Please make sure you have conda installed on your machine."\
    "Exiting.${no_color}"
    exit 1
fi

source "${conda_bin_dir}/../etc/profile.d/conda.sh"
