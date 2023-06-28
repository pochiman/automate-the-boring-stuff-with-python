import ezgmail
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email')

ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email', ['attachment1.jpg', 'attachment2.mp3'])

# You can also supply the optional keyword arguments cc and bcc to send carbon copies and blind carbon copies:
import ezgmail
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email', cc='friend@example.com', bcc='otherfriend@example.com,someoneelse@example.com')

# If you need to remember which Gmail address the token.json file is configured for:
import ezgmail
ezgmail.init()
ezgmail.EMAIL_ADDRESS