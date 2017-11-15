#!/bin/bash

python /Users/Micah/git/BirthdayReminder/birthday_reminder.py 

# email subject
SUBJECT="Birthday Reminder"
# Email To:
EMAIL="micah.d.carroll@berkeley.edu"
# Email text/message
EMAILMESSAGE=$(</Users/Micah/git/BirthdayReminder/emails/latest_email.txt)
# send an email
echo "$EMAILMESSAGE" | mail -s "$SUBJECT" "$EMAIL"
