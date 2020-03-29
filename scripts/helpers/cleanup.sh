#!/usr/bin/env bash

###############################################################################
#
# Cleanup any environment setup, python unused files, git hooks.
#
###############################################################################

script_name="$(basename -- "$0")"

# Formats
bold="\033[1m"
green="\033[0;32m"
red="\033[91m"
no_color="\033[0m"

# Get the directory the script is running in
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

remove_custom_git_hooks()
{
  activated_environment=$(source "${script_dir}/conda-create-env.sh" -a >/dev/null 2>&1)
  if [[ $? -ne 0 ]]; then
    :
  else
    echo -e "${green}Removing custom git hooks...${no_color}"
    pre-commit uninstall
    source "${script_dir}/conda-create-env.sh" -a
  fi
}

remove_python_temp_files()
{
  echo -e "${green}Removing python temp files...${no_color}"
  # Remove eny python unnecessary files
  rm -rf bin dist .pytest_cache .coverage *.egg-info *.log
  find . -path "*/__pycache__" -type d -exec rm -r {} ';'
}

# Get conda commands
cleanup()
{
  # Remove custom git hooks
  remove_custom_git_hooks
  remove_python_temp_files
  # Remove Conda Env alongth with Poetry dependencies.
  source "${script_dir}/conda-remove-env.sh"
}

cleanup