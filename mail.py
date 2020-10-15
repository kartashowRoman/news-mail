from news import name_and_text
import smtplib, ssl
from datetime import datetime



name_and_text = name_and_text.encode('utf-8')

port = 465  # For SSL
password = "papiks29931540"
sender_mail = "papiks96@gmail.com"
receiver_mail = "VASINS.MAKSIMS@zodiac-crew.com"
# VASINS.MAKSIMS@zodiac-crew.com
# papiks96@gmail.com
# ensane@inbox.lv
# giouras.sismanidis@mail.ru

# Create a secure SSL context
context = ssl.create_default_context()
#get the time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
try:
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login("papiks96@gmail.com", password)
		server.sendmail(sender_mail,receiver_mail,name_and_text)
		print("Successfully sent", dt_string)
except:
	print("Couldn't send the mail", dt_string)











