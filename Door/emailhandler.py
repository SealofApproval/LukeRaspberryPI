import smtplib
import RPi.GPIO as GPIO
import time
import array

months = {1: "Jan.", 2: "Feb.", 3: "Mar.", 4: "Apr.", 5: "May", 6: "June", 7: "July", 8: "Aug.", 9: "Sept.", 10: "Oct.", 11: "Nov.", 12: "Dec."};

def sendEmail(timeArray):
	smtpUser = 'lukeraspberrypi@gmail.com'
	smtpPass = 'camerontaylor'

	toAdd = '6789204057@vtext.com'
	fromAdd = smtpUser

	subject = ''
	header = 'To: ' + toAdd + '\n' + 'From: ' + '\n' + 'Subject: ' + subject
	body = months[timeArray[1]] + " " + str(timeArray[2]) + ", " + str(timeArray[0]) + " at " + str(timeArray[3].zfill(2)) + ":" + str(timeArray[4].zfill(2)) + ":" + str(timeArray[5].zfill(2)) + " - The door was opened"

	s = smtplib.SMTP('smtp.gmail.com', 587)

	s.ehlo()
	s.starttls()
	s.ehlo()

	s.login(smtpUser, smtpPass)
	s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

	s.quit()

buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)

file = open("log.txt", a)

try:
	while True:
		timeArray = time.localtime()
		if(timeArray[3] != 8):
			input = GPIO.input(buttonPin)
			if(not(GPIO.input(buttonPin))):
				try:
					sendEmail(timeArray)
				except:
					print("Error on sending - no email sent.")
				print(months[timeArray[1]] + " " + str(timeArray[2]) + ", " + str(timeArray[0]) + " at " + str(timeArray[3]) + ":" + str(timeArray[4]) + ":" + str(timeArray[5]) + " - The door was opened")
				file.write(months[timeArray[1]] + " " + str(timeArray[2]) + ", " + str(timeArray[0]) + " at " + str(timeArray[3]) + ":" + str(timeArray[4]) + ":" + str(timeArray[5]) + " - The door was opened\n")
except KeyboardInterrupt:
	file.close()
