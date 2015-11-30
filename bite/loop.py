from gevent import monkey; monkey.patch_all()

import sys
import asyncio

loop = asyncio.get_event_loop()

def _wrap( ctxt, callback ):
    def inner( future ):
        loop.call_soon( callback, future.result() )
    return inner

def push(ctxt, func):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(func)

def run():
    try:
        loop.run_forever()
    finally:
        loop.close()

def stop():
    loop.stop()

