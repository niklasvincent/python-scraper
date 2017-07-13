import argparse
import logging


from scraper import Scraper


def parse_args():
    """Parse command line arguments"""
    args_parser = argparse.ArgumentParser()
    args = args_parser.parse_args()
    return args


def main():
    args = parse_args()
    scraper = Scraper(cache_name=__name__, cache_expiry=36000)

    #  Perform your scraping here


if __name__ == "__main__":
    logging.basicConfig(filename="{}.log".format(__name__), level=logging.INFO)
    try:
        main()
    except Exception as e:
        logging.exception(e)
