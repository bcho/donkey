# coding: utf-8

'''
    donkey.compat
    ~~~~~~~~~~~~~

    Compatibility.
'''

import gevent


def spawn(func, *args, **kwargs):
    '''Spawn a function.

    By now only `gevent` is supported.

    :param func: function to be ran.
    '''
    return gevent.spawn(func, *args, **kwargs)


def sleep(seconds):
    '''Sleep for some times.

    :param seconds: seonds you want to sleep.
    '''
    return gevent.sleep(seconds)
