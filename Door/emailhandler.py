import smtplib
import Rpi.GPIO as GPIO
import time

def sendEmail():
	smtpUser = 'lukeraspberrypi@gmail.com'
	smtpPass = 'camerontaylor'

	toAdd = '6789204057@vtext.com'
	fromAdd = smtpUser

	subject = 'Subject Message'
	header = 'To: ' + toAdd + '\n' + 'From: ' + '\n' + 'Subject: ' + subject
	body = 'The door has been opened'

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


while true:
	input = GPIO.input(buttonPin)
	if(not(GPIO.input(buttonPin))):
		sendEmail()
