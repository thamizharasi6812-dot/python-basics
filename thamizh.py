import smtplib

sender='thamizharasi6812@gmail.com'
receiver='subashinisenthilkumar94@gmail.com'
password='grdt efsc wjjz qvcr'

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login(sender,password)
message='freedom is the oxygen of the soul'
server.sendmail(sender,receiver,message)

print('email send successfully')

server.quit()