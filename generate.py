from celery import group, chord, chain
from celery.task.control import discard_all
from proj.tasks import random_int, add, mul, xsum


discard_all()

# Chain

res = chain(add.s(4, 4), mul.s(8), mul.s(10))()
print res.get()

# Chord Example

callback = xsum.s()
header = [add.s(i,i) for i in range(0,10)]
result = chord(header)(callback)

result = result.get()

print result

# Group Example

job = group(random_int.s(i) for i in range(0,10))
result = job.apply_async()

while not result.ready():
	pass

print result.ready()
print result.successful()

for res in result:
	print res

result = result.get()

for res in result:
	print res
