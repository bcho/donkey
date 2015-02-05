# Donkey [WIP]

[![Build Status](https://travis-ci.org/bcho/donkey.svg)](https://travis-ci.org/bcho/donkey)

A simple cron-like library for executing scheduled jobs.


Donkey is inspired by [Cron][cron-go].

[cron-go]: https://github.com/robfig/cron


```python
from datetime import datetime
from donkey import JobQueue, Worker


q = JobQueue()


@q.job(3)
def this_job_runs_every_3_seconds():
    print('Fuzz', datetime.now())


@q.job(5)
def this_job_runs_every_5_seconds():
    print('Buzz', datetime.now())


Worker().run(q)
# Fuzz 2015-02-03 16:41:01.408136
# Buzz 2015-02-03 16:41:03.404123
# Fuzz 2015-02-03 16:41:04.406813
# Fuzz 2015-02-03 16:41:07.408426
# Buzz 2015-02-03 16:41:08.406851
# Fuzz 2015-02-03 16:41:10.408415
# Fuzz 2015-02-03 16:41:13.403260
# Buzz 2015-02-03 16:41:13.403319
```

## TODO

- [x] tests.
- [ ] add jobs at run time.
- [ ] job states & stats (see [rq][rq]).
- [ ] other backend (namely `thread`, `stackless`) support.


[rq]: http://python-rq.org/


## License

[MIT](LICENSE)
