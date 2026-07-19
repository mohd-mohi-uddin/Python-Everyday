>> steps to send email:

1. set connection using with smtplib.SMTP("emailprovider") as connection

2. secure connection using starttls()

3. login using connection.login(user=,password=)

4. send email using sendmai(from_addrs=,to_addrs,msg=)