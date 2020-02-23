#!/usr/bin/env bash

###############################################################################
#
# Build a docker image.
#
###############################################################################

script_name="$(basename -- "$0")"

# Formats
bold="\033[1m"
green="\033[0;32m"
red="\033[91m"
no_color="\033[0m"

echo -e "${green}Building docker image...${no_color}"

version="0.0.1"
version=$(poetry version | sed 's/[^0-9.]*//g')

echo -e "${green}Using version ${version}${no_color}"
docker build -f ./deployment/docker/ekrhizoc.dockerfile -t nichelia/ekrhizoc:${version} --build-arg APP_VERSION=${version} .