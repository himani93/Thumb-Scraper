import argparse
import json
import sys

from thumb_scraper.scraper import ThumbScraper


def read_json_file(file_path):
    with open(file_path) as pages_file:
        pages = json.load(pages_file)

    return pages


def main():
    parser = argparse.ArgumentParser(description="Legalstart Thumb Parser Solution",
                                     add_help=True,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--url', dest='url', required=False, default="https://yolaw-tokeep-hiring-env.herokuapp.com/",
                        help="Link to first page")
    parser.add_argument('--pages', dest='pages_location', required=True,
                        help="Location to pages JSON file")

    if len(sys.argv) < 3:
        parser.print_help()
        sys.exit(1)

    url =  parser.parse_args().url
    pages_location = parser.parse_args().pages_location

    pages = read_json_file(pages_location)

    scraper = ThumbScraper(url, pages)
    for result in scraper.scrape():
        print result


if __name__ == "__main__":
    main()
