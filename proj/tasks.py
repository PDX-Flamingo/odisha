from __future__ import absolute_import

from time import sleep
from proj.celery import app
from random import randint, uniform


@app.task
def random_list(job):
	print "Start " + str(job)
	sleep(uniform(0,2))
	return "Worker " + str(job) + ": Result " + str(randint(1, 100))

@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)