import sys
import logging
import bbc_songs

import bite.loop as loop
import bite.mq as mq
import bite.context as context

FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT,level=logging.DEBUG)

def print_titles( titles ):
    for title in titles:
        print( title )

def main(argv):
    print("Hello world!")
    logging.warning("I just printed hello world")

    logging.debug("Now loading BBC data")
    ctxt = context.create()

    loop.push(ctxt, bbc_songs.get_titles, print_titles)

    loop.run()

if __name__ == "__main__":
    main(sys.argv)

