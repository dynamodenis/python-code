import smtplib

sender_email= "dmbugua66@gmail.com"
rec_email = "maxmwangimubeah@gmail.com"
password = input(str("Please enter your password:"))
message = "Hey, this was sent to me by Dynamo Denis"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email, password)
print("Login Success")
server.sendmail(sender_email,rec_email,message)
print("Email has been sent to", rec_email)