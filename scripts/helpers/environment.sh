#!/usr/bin/env bash

###############################################################################
#
# Setup project environment (conda and poetry).
#
###############################################################################

script_name="$(basename -- "$0")"

# Formats
bold="\033[1m"
green="\033[0;32m"
red="\033[91m"
no_color="\033[0m"

usage()
{
    echo -e "${bold}${green}$script_name:${no_color}"
    echo "    " "Script to setup environment for project (conda and poetry)."
    echo "    " "options:"
    echo "    " "  --force, -f             Force to re-create project environment."
    echo "    " "  --prod, -p              Create project environment for production."
    echo "    " "  --help, -h              Show this help message and exit."
}

arg_count=0
force=false
prod=false
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--force)
            force=true
            shift # past argument
            ;;
        -p|--prod)
            prod=true
            shift # past argument
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            >&2 echo "$tag" "error: '$1' not a recognized argument/option"
            >&2 usage
            exit 1
            ;;
    esac
done

# Get the directory the script is running in
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

setup_environment()
{
  source "${script_dir}/conda-create-env.sh"
  source "${script_dir}/poetry_setup.sh"

  if [[ ${prod} = true ]]; then
    poetry install --no-dev
  else
    poetry install
  fi
}

if [[ ${force} = true ]]; then
  setup_environment
  return
fi

# Try and activate conda environment first.
# If fails, then create environment.
activated_environment=$(source "${script_dir}/conda-create-env.sh" -a >/dev/null 2>&1)
if [[ $? -ne 0 ]]; then
  setup_environment
else
  source "${script_dir}/conda-create-env.sh" -a
fi

