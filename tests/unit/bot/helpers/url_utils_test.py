import pytest

from ekrhizoc.bot.helpers import url_utils


def test_canonicalise_url(canonical_urls):
    for uncanonical, canonical in canonical_urls.items():
        parsed_url = url_utils._canonicalise_url(uncanonical)
        assert parsed_url == canonical


def test_is_valid_url(valid_urls, invalid_urls):
    for value in valid_urls:
        assert url_utils._is_valid_url(value) == True
    for value in invalid_urls:
        assert url_utils._is_valid_url(value) == False


# TODO: Unit test for test_get_robots_file_parser


def test_get_url_domain(url_data):
    for value in url_data:
        url = value.get("href", "")
        host = value.get("hostname", "")
        if url and host:
            assert url_utils.get_url_domain(url) == host


# TODO: Unit test for test_is_robots_restricted


@pytest.mark.parametrize(
    "url1, url2, same_subdomain",
    [
        ("", "", False),
        ("", "http://example.com", False),
        ("http://example.com", "", False),
        ("http://1.2.3.4/", "1.2.3.4", True),
        ("scheme://1.2.3.4", "1.2.3.4", True),
        ("ftp://1.2.3.4/a/b/c/d", "1.2.3.4", True),
        ("http://1.2.3.4", "1.2.3.4", True),
        ("http://foo.example.com", "example.com", False),
        ("http://example.com", "foo.example.com", False),
        ("http://foo.EXAMPLE.COM", "example.com", False),
        ("http://☃.net", "xn--n3h.net", False),
        ("http://☃.net", "☃.net", True),
        ("http://😬.☃.net", "☃.net", False),
        ("http://😬.☃.net", "☃.net", False),
    ],
)
def is_same_subdomain(url1, url2, same_subdomain):
    assert url_utils.is_same_subdomain(url1, url2) == same_subdomain


# TODO: Unit test for test_get_full_url
