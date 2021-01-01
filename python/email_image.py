from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib
message = MIMEMultipart()
message['From'] = "youremail@gmail.com"
message['To'] = "youremail@gmail.com"
message['Subject'] = "Email with image attachment"
message.attach(MIMEImage(file("/home/asim/screen.png").read()))
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(message['From'],"yourpassword")
server.sendmail(message['From'],message['To'],message.as_string())
server.quit()
print("Email sent suucessfully!")