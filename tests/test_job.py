# coding: utf-8

from donkey.job import Schedule, Job, JobQueue


def test_schedule():
    interval = 30
    sched = Schedule(interval)

    assert sched.next(0) == 0 + interval
    assert sched.next(123) == 123 + interval


def test_job_run():
    expected_rv = 42
    job = Job(lambda: expected_rv, Schedule(30))

    assert job.run() == expected_rv


def test_job_run_stats():
    interval = 30
    job = Job(lambda: 'foobar', Schedule(interval))

    # Before first run
    assert job.last_run_at is None
    assert job.next_run_at is None

    job.reschedule(0)

    # After first run
    assert job.last_run_at is None
    assert job.next_run_at == 0 + interval

    job.reschedule(interval)

    # After second run
    assert job.last_run_at == 0 + interval
    assert job.next_run_at == interval + interval


def test_job_queue_add():
    q = JobQueue()

    q.add(Job(lambda: 'nop', Schedule(30)))

    assert len(q.get_runnable_jobs()) == 1


def test_job_queue_job_decorator():
    q = JobQueue()

    @q.job(30)
    def nop():
        pass

    assert len(q.get_runnable_jobs()) == 1


def test_job_queue_next_run_at():
    q = JobQueue()

    # Should return ``None`` when no available job.
    assert q.next_run_at is None

    q.job(30)(lambda: 'nop')
    q.reschedule_jobs(0)  # TODO refine reschedule jobs?

    assert q.next_run_at is not None
