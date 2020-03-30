#!/usr/bin/env bash

###############################################################################
#
# Build a docker image.
#
###############################################################################

# shellcheck disable=SC2034
script_name="$(basename -- "$0")"

# Colour Formats
# shellcheck disable=SC2034
bold="\033[1m"
# shellcheck disable=SC2034
green="\033[0;32m"
# shellcheck disable=SC2034
red="\033[91m"
# shellcheck disable=SC2034
no_color="\033[0m"

echo -e "${green}Building docker image...${no_color}"

version="0.0.1"
version=$(poetry version | sed 's/[^0-9.]*//g')

echo -e "${green}Using version ${version}${no_color}"
docker build -f ./deployment/docker/ekrhizoc.dockerfile -t nichelia/ekrhizoc:"${version}" --build-arg APP_VERSION="${version}" .
