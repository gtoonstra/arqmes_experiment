import sys

import bbc_songs_async
import logging

FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT,level=logging.DEBUG)

def print_titles( titles ):
    for title in titles:
        print( title )

def main(argv):
    print("Hello world!")
    logging.warning("I just printed hello world")
    logging.debug("Now loading twitter data")
    bbc_songs_async.get_titles(print_titles)
    logging.info("Requested songs, waiting for the results")

if __name__ == "__main__":
    main(sys.argv)

