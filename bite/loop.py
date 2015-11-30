from gevent import monkey; monkey.patch_all()

import sys
import asyncio

loop = asyncio.get_event_loop()

def wrap( ctxt, callback ):
    def inner( *args ):
        loop.call_soon( callback, *args )
    return inner

def push(ctxt, func, callback):
    if callback is None:
        loop.call_soon(func)
    else:
        cb = wrap(ctxt, callback)
        loop.call_soon(func, cb)

def run():
    loop.run_forever()
    loop.close()

def stop():
    loop.stop()

