# coding: utf-8

'''
    donkey.job
    ~~~~~~~~~~

    Donkey job data structure.
'''

from .compat import spawn


class Schedule(object):
    '''Job schedule defination.

    :param interval: execute interval (in seconds).
    '''

    def __init__(self, interval):
        # TODO support fuzzy language / crontab format
        self.interval = int(interval)

    def next(self, now):
        '''Calculate next runnable time (in unix timestamp).

        :param now: current unix timestamp.
        '''
        return now + self.interval


class Job(object):
    '''Scheduled job.

    TODO job state

    :param exec_: the actual job.
    :param schedule: a :class:`donkey.Schedule` instance.
    '''

    def __init__(self, exec_, schedule):
        self.exec_ = exec_
        self.schedule = schedule

        self._last_run_at = None
        self._next_run_at = None

    def run(self):
        '''Execute the job'''
        return self.exec_()

    def reschedule(self, now):
        '''Reschedule the job base on current timestamp.

        :param now: current unix timestamp.
        '''
        self._last_run_at = self.next_run_at
        self._next_run_at = self.schedule.next(now)

    @property
    def last_run_at(self):
        '''Last ran timestamp.'''
        return self._last_run_at

    @property
    def next_run_at(self):
        '''Next ran timestamp.'''
        return self._next_run_at


class JobQueue(object):

    def __init__(self):
        # TODO race condition
        self.jobs = []

    def add(self, job):
        '''Add a job to the queue.

        :param job: a :class:`donkey.Job` instance.
        '''
        self.jobs.append(job)

    def job(self, interval):
        '''Return a decorator for adding a function as job:

            @queue.job(300)
            def my_job():
                print('I am working...')

        :param interval: execute interval (in seconds).
        '''
        def wrapper(func):
            job = Job(func, Schedule(interval))

            return self.add(job)

        return wrapper

    def get_runnable_jobs(self):
        '''Get runnable jobs.'''
        # Sort by next run time, sooner the better.
        self.jobs.sort(key=lambda j: j.next_run_at)

        return self.jobs

    @property
    def next_run_at(self):
        '''Get next running unix timestamp.'''
        jobs = self.get_runnable_jobs()

        if not jobs:
            return None
        return jobs[0].next_run_at

    def run_jobs(self, now):
        '''Execute jobs run at this moment.

        :param now: current unix timestamp.
        '''
        for job in self.jobs:
            if job.next_run_at != now:
                return
            spawn(job.run)
            job.reschedule(now)

    def reschedule_jobs(self, now):
        '''Reschedule all jobs base on current timestamp.

        :param now: current unix timestamp.
        '''
        for job in self.jobs:
            job.reschedule(now)
