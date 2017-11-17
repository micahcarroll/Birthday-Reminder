import datetime
import pandas as pd
import numpy as np

# Add unsure + add age + add when upcoming
def compose_email(birthdays_today, upcoming_birthdays):
	birthdays_today_string = "Today it is {} people's birthdays: {}".format(len(birthdays_today), ", ".join(list(birthdays_today['Name'])))
	
	if upcoming_birthdays:
		upcoming_birthdays_string = "Upcoming birthdays are: {}".format(", ".join(list(upcoming_birthdays['Name'])))
		birthdays_today_string = birthdays_today_string + "\n\n" + upcoming_birthdays_string

	today_string = "[Update for {}]".format(today)
	final_email_string = "Hello!\n\n" + birthdays_today_string + "\n\n That's it! \n Thanks for checking in!"
	return final_email_string

# Add dynamic naming for emails with the current date
def write_email_to_file(email_string):
	with open("/Users/Micah/git/BirthdayReminder/emails/latest_email.txt", "w") as f:
	    f.write(email_string)

# Birthdays within UPCOMING_BIRTHDAYS_SETTING days will be included in the upcoming birthdays section of the sent email
UPCOMING_BIRTHDAYS_SETTING = 10 

today = datetime.date.today()
today_day_num = today.timetuple().tm_yday 

df = pd.read_csv('/Users/Micah/git/BirthdayReminder/People.csv')
df.dropna(subset=['Day'], inplace=True)

# Adds a column with the day number of the birthday
# TODO: account for 2/29 edge case that breaks with non-leap years
df['Day_num'] = [ datetime.date(datetime.date.today().year, month, day).timetuple().tm_yday 
				  for month, day in 
				  zip(np.array(df['Month'], dtype=int), 
				  	  np.array(df['Day'], dtype=int))]

birthdays_today = df[df.Day_num == today_day_num]
upcoming_birthdays = df[(df.Day_num - today_day_num > 0) & (df.Day_num - today_day_num <= 10)]

# Check if email has already been sent
if len(birthdays_today) != 0 or True:
	email_string = compose_email(birthdays_today, upcoming_birthdays)
	write_email_to_file(email_string)








