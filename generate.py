from celery import group
from celery.task.control import discard_all
from proj.tasks import random_list, add, mul, xsum


discard_all()
result = group(random_list.s(i) for i in range(0,10))().get()

for res in result:
	print res
