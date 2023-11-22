import requests
import selectorlib
from data_base import store, read
from send_email import send_email

URL = 'http://programmer100.pythonanywhere.com/tours/'
# fool the server that this is a browser
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """ Scrape the page source from the url """
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    """ Extract the tour from the web page """
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value


def get_next_tour():
    # get the web page
    scraped = scrape(URL)
    # extract the tour
    extracted = extract(scraped)

    if extracted != 'No upcoming tours':
        # try to get the tour from the date base
        tour = read(extracted)

        # if not in db, insert in to the date base
        if not tour:
            store(extracted)
            send_email(extracted)


if __name__ == "__main__":
    get_next_tour()
