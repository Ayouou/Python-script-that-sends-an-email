import smtplib

# Set up the SMTP server
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login('user@example.com', 'password')

# Send the message
to_email = 'recipient@example.com'
subject = 'Test email from Python'
message = 'This is a test email sent from Python'
msg = "Subject: {}\n\n{}".format(subject, message)
server.sendmail('user@example.com', to_email, msg)

# Disconnect from the server
server.quit()
