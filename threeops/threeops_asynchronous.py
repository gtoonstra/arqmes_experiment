import sys

import asyncio
import bbc_songs_async
import logging

FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(format=FORMAT,level=logging.DEBUG)

def print_titles( loop, titles ):
    for title in titles:
        print( title )
    loop.stop()

def main(argv):
    print("Hello world!")
    logging.warning("I just printed hello world")
    logging.debug("Now loading BBC data")
    loop = asyncio.get_event_loop()
    loop.call_soon(bbc_songs_async.get_titles, print_titles, loop)

    logging.info("Requested songs, waiting for the results")
    loop.run_forever()
    loop.close()

if __name__ == "__main__":
    main(sys.argv)

