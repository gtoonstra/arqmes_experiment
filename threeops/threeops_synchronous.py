import sys

import bbc_songs_sync
import logging

FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT,level=logging.DEBUG)

def main(argv):
    print("Hello world!")
    logging.warning("I just printed hello world")
    logging.debug("Now loading twitter data")

    titles = bbc_songs_sync.get_titles()
    for title in titles:
        print( title )

if __name__ == "__main__":
    main(sys.argv)

