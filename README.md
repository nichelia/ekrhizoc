# ekrhizoc
ekrhizoc (e6c): A web crawler

## Contents
1. [Definition](#definition)
2. [Use Case](#use-case)
3. [Development](#deve∏lopment)
4. [Testing](#testing)
5. [Versioning](#versioning)
6. [Documentation](#documentation)
7. [Deployment](#deployment)

## Definition

εκρίζωση (Greek)
ekrízosi / uprooting, eradication

Also known as __e6c__.

## Use Case

Implementation of a simple python web crawler.  
Input: URL (seed).  
Output: simple textual sitemap (to show links between pages).

### Requirements

* The crawler is limited to *__one__* subdomain (exclude external links).
* No use of web crawling libraries/frameworks (e.g. scrapy).
* (Optional) Use of HTML handling Libraries/Frameworks.
* Production-ready code.

### Assumptions

* The input URL (seed) is limited to __only__ one at every run.
* The targeted URL(s) are not dynamically generated (no backend javascript parsing required).
* Links to be extracted from HTML anchor <a> elements.
* Valid links include
    - Valid URL
        + Non empty
        + Valid url address
        + No longer than `URL_MAX_LENGTH` characters
    - Link not visited before
    - Link not part of ignored file types
    - Link same domain as seed url
    - Link not restricted in robots.txt

### Design

This project implements a Basic Universal Crawler based on breadth first search graph traversal.

## Development

### Configure for local development

* Clone [repo](https://github.com/nichelia/ekrhizoc) on your local machine
* Install [`conda`](https://www.anaconda.com) or [`miniconda`](https://docs.conda.io/en/latest/miniconda.html)
* Create symlink for githooks (based on [`isort`](https://github.com/timothycrosley/isort), [`black`](https://github.com/psf/black)):  
`make git-hooks`
* Create your local project environment (based on [`conda`](https://www.anaconda.com), [`poetry`](https://python-poetry.org)):  
`make env`
* (Optional) Update existing local project environment:  
`make env-update`

### Run locally

On a terminal, run the following (execute on project's root directory):

* Activate project environment:  
`. ./scripts/helpers/environment.sh`
* Run the CLI using `poetry`:  
`poetry run ekrhizoc`

### Contribute

N/A

## Testing

N/A

## Versioning

Increment the version number:  
`poetry version {bump rule}` where valid bump rules are:

1. patch
2. minor
3. major
4. prepatch
5. preminor
6. premajor
7. prerelease

### Changelog

Use `CHANGELOG.md` to track the evolution of this package.  
The `[UNRELEASED]` tag at the top of the file should always be there to log the work until a release occurs.  

Work should be logged under one of the following subtitles:
* Added
* Changed
* Fixed
* Removed

On a release, a version of the following format should be added to all the current unreleased changes in the file.  
`## [major.minor.patch] - YYYY-MM-DD`

## Documentation

N/A

## Deployment

### Pip package

N/A

### Docker image

N/A