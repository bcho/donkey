# coding: utf-8

'''
    donkey.worker
    ~~~~~~~~~~~~~

    Donkey worker.
'''

from time import time as get_now_timestamp

from .compat import sleep


A_LONG_TIME = 10 * 365 * 24 * 3600  # 10 years


class Worker(object):

    def run(self, queue):
        '''Let the worker run.

        :param queue: :class:`donkey.JobQueue` instance.
        '''
        queue.reschedule_jobs(get_now_timestamp())

        while True:
            effective = queue.next_run_at
            if effective:
                # Wait until next schedule comes...
                sleep(effective - get_now_timestamp())
                queue.run_jobs(effective)
            else:
                # TODO support add job in the runtime.
                sleep(A_LONG_TIME)
                queue.reschedule_jobs(get_now_timestamp())
