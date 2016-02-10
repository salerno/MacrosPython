#!/usr/bin/python 
# Roberto Salerno
"A program in python to check the RERB timetable"
"usage: python CheckTimeRERB.py"

import datetime
import sys
import urllib2
#import smtplib
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Define a timeRER() function 
def timeRER():
  url = 'http://www.ratp.fr/horaires/fr/ratp/rer/prochains_passages/RB/Lozere/A'
  data = urllib2.urlopen(url)
  passing_time = "passing_time"
  stop_time = ":"

  #how to send an email via google 
  #message = "test"
  #FROM = 'address'
  #TO = ['address']
  ## Credentials (if needed)
  #username = 'username'
  #password = 'password'

  Y = np.arange(6)
  X = [0,0,0,0,0,0]
  counter = 0
  #print data.read()
  for line in data:
  	if passing_time in line:
	  	if stop_time in line:
  			line_list = line.split(">")
  			string_time = line_list[1]
  			string_justtime =  string_time[0:5]
  			minutesL = string_justtime.split(':')
  			minutesM = int(minutesL[0]) * 60 + int(minutesL[1])
			#current time, convert it in minutes from the starting of the day
  			now = datetime.datetime.now()
  			minuti_start = int(now.hour) * 60 + int(now.minute)
  			diff = minutesM - minuti_start
  			print "Treno tra",diff,"minuti"
			X[counter] = diff
			counter = counter + 1 

  #server = smtplib.SMTP('smtp.gmail.com:587')
  #server.ehlo()
  #server.starttls()
  #server.login(username,password)
  #server.sendmail(FROM, TO, message)
  #server.quit()

  #plotting the values
  width = 0.2        # the width of the bars
  offset = 0.2       # offset of the bars
  fig, ax = plt.subplots()
  rectscomb = ax.bar(Y, X, 1, color='b',edgecolor='white',alpha=0.5)
  ax.set_ylabel('Time (minutes)')
  ax.set_xlabel('Number of train')
  ax.set_xticks(Y+width+offset)
  plt.setp(ax.set_xticklabels(('first', 'second', 'third', 'fourth', 'fifth','sixth')), 
         rotation=45, 
         fontsize=10)  
  plt.show()

# This is the standard boilerplate that calls the timeRER() function.
if __name__ == '__main__':
  timeRER()
