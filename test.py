#!/home/sekhar/anaconda3/bin/python

from apscheduler.schedulers.blocking import BlockingScheduler
from crawler import *


sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=2)
def crawl_job():
	crawl()

sched.start()