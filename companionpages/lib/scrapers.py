import logging

from bs4 import BeautifulSoup
import requests

logger = logging.getLogger('researchcompendia.lib')


def scrape_abstract(article_url, timeout=3):
    """ try to scrape an abstract and return text.

    do not allow this to cause a failure. if anything breaks, return an empty string

    """
    content = ''
    try:
        r = requests.get(article_url, timeout=timeout)
    except requests.exceptions.RequestException:
        logger.debug('requests exception')
        logger.warning('requests exception')
        return content

    if not r.ok:
        logger.warning('exception %s', r)
        return content

    # we can get fancier but for now we know how to scrape aps.org
    content = scrape_aps(r.text)

    return content


def scrape_aps(text):
    content = ''
    soup = BeautifulSoup(text)
    abstracts = soup.find_all("div", class_="aps-abstractbox")
    if len(abstracts) > 0:
        if abstracts[0].text is not None:
            content = abstracts[0].text
    return content
