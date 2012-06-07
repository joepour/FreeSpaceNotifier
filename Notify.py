# Author:  Joe Pour
# Date:    31/01/12
# Version: 1.0.0 

# This script monitors the amount of free space on the C: disk and emails you when there is less than 10% disk space
#
# To create a schedule task you can just run this command, changing the paths to apply to your environment.
# schtasks /Create /SC HOURLY /TN CalculateFreeDiskSpace /TR "C:\Python27\python.exe C:\Users\joe.pour\Documents\Python Projects\CalculateFreeDiskSpace.py"
#
# To check status of new scheduled task
# schtasks /Query /TN CalculateFreeDiskSpace

import wmi
import smtplib

c = wmi.WMI()

# Sender Email Address
sender = ''

# Email Address of person who is notified
receiver = ''

# Server name/details
serverName = ''

# SMTP Server ip
smtpHost = ''

for disk in c.Win32_LogicalDisk(DriveType=3):
	if disk.Caption == 'C:':
		freespace = round((100.0 * long (disk.FreeSpace) / long (disk.Size)))
		#freespace = round(freespace, 2)
		
		if freespace < 90.0:
			# Notify me if there is less than 10% free disk space
			message  = """From: {0}
Subject: Subject: Low Disk space ({1})

The C Disk on the on {1} has {2}% free space
""".format(sender, serverName, freespace)

			smtpObj  = smtplib.SMTP(smtpHost)
			smtpObj.sendmail(sender, receiver, message)         
			print "Successfully sent email"
			
			
