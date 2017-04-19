import requests
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import subprocess as s

def send_message(short,long):
	s.call(['notify-send',short,long])
	return

def crawl():
	#print("crawler called")
	#f = open("./notice_bank.txt","r")
	#last_seen = 0
	#for l in f:
	#	last_seen = int(l)

	display = Display(visible=0, size=(800, 600))
	display.start()

	url = "http://172.61.25.110/ois/login.php"
	driver = webdriver.Firefox()
	driver.get(url)
	time.sleep(2)
	data = driver.page_source
	driver.quit()
	soup = BeautifulSoup(data, "lxml")
	notice_id = 0
	t = None
	cnt = 0
	for node in soup.find_all("div",class_="noticeback"):
		#notice_id = int(node.find('a')['href'].split()[1].split('(')[1][:][:-1])
		#if cnt == 0:
		#	t = notice_id
		#	cnt += 1
		#if notice_id > last_seen:
		#print("new notice id ....")
		send_message(node.contents[0].contents[0],node.contents[4].contents[0] + "\n" + node.contents[5].contents[0])
		#else:
		#print("not new")
	#f = open("./notice_bank.txt",'w')
	#f.write(str(t))
	#f.close()


