>> steps to send email:

1. set connection using with smtplib.SMTP("emailprovider") as connection

2. secure connection using starttls()

3. login using connection.login(user=,password=)

4. send email using sendmai(from_addrs=,to_addrs,msg=)


>>steps to create datetime:

1. import datetime module

2. create obect using datetime class
now = datetime.datetime.now()

3. this shows the cureent date time year month 
access any one using now.day, now.time etc.

