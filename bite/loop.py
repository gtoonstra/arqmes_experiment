from gevent import monkey; monkey.patch_all()

import sys
import asyncio

loop = asyncio.get_event_loop()

def _wrap( ctxt, callback ):
    def inner( future ):
        loop.call_soon( callback, future.result() )
    return inner

def push(ctxt, func, callback):
    if callback is None:
        task = asyncio.Task(func())
    else:
        cb = _wrap(ctxt, callback)
        task = asyncio.Task(func())
        task.add_done_callback(cb)

def run():
    loop.run_forever()
    loop.close()

def stop():
    loop.stop()

