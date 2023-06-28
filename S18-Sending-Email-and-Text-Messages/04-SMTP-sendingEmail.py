# Sending Email
import smtplib
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login('bob@example.com', 'MY_SECRET_PASSWORD')

smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')

smtpObj.quit()

# Connecting to an SMTP Server
smtpObj = smtplib.SMTP('smtp.example.com', 587)
type(smtpObj)

smtpObj = smtplib.SMTP_SSL('smtp.example.com', 465)

# Sending the SMTP “Hello” Message
smtpObj.ehlo()

# Starting TLS Encryption
smtpObj.starttls()

# Logging In to the SMTP Server
smtpObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')

# Sending an Email
smtpObj.sendmail('my_email_address@example.com', 'recipient@example.com', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')

# Disconnecting from the SMTP Server
smtpObj.quit()