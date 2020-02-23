import re
from typing import Set

import urlcanon

from ekrhizoc.logging import logger


def _canonicalise_url(url: str = "") -> str:
    """
    Canonicalise the url
    """
    try:
        parsed_url = urlcanon.parse_url(url)
        canonical_url = urlcanon.semantic_precise(parsed_url)
        return str(canonical_url)
    except Exception as e:
        logger.error(e)
        return ""


def _is_valid_url(url: str = "") -> bool:
    pattern = re.compile(
        "^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
    )

    if url == "":
        return False

    if not pattern.match(url):
        return False

    # TODO: Variable here - no magic number
    if not len(url) < 300:
        return False

    return True


def get_url_domain(url: str = "") -> str:
    """
    Return the host of the given url
    """
    try:
        parsed_url = urlcanon.parse_url(url)
        return (parsed_url.host).decode()
    except Exception as e:
        logger.error(e)
        return ""


def is_same_subdomain(url: str = "", domain: str = "") -> bool:
    """
    Check if given (sub)domain is idential (sub)domain to the given url
    """
    if url == "" or domain == "":
        return False

    try:
        parsed_url = urlcanon.parse_url(url)
        normalised_domain = urlcanon.normalize_host(domain)
        return urlcanon.url_matches_domain_exactly(parsed_url, normalised_domain)
    except Exception as e:
        logger.error(e)
        return False


def get_full_url(url: str = "", domain: str = "", ignore_filetypes: Set = {}) -> str:
    """
    """
    if _is_valid_url(url):
        return _canonicalise_url(url)

    if url.startswith("/"):
        full_url = domain + url
        if _is_valid_url(full_url):
            return _canonicalise_url(full_url)

    return ""
