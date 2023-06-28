import ezgmail
unreadThreads = ezgmail.unread()  # List of GmailThread objects.
ezgmail.summary(unreadThreads)

# The messages attribute contains a list of the GmailMessage objects that make up the thread, 
# and these have subject, body, timestamp, sender, and recipient attributes that describe the email:
len(unreadThreads)

str(unreadThreads[0])

len(unreadThreads[0].messages)

str(unreadThreads[0].messages[0])

unreadThreads[0].messages[0].subject

unreadThreads[0].messages[0].body

unreadThreads[0].messages[0].timestamp

unreadThreads[0].messages[0].sender

unreadThreads[0].messages[0].recipient

# The ezgmail.recent() function will return the 25 most recent threads in your Gmail account.
recentThreads = ezgmail.recent()
len(recentThreads)

recentThreads = ezgmail.recent(maxResults=100)
len(recentThreads)

# Searching Mail from a Gmail Account
resultThreads = ezgmail.search('RoboCop')
len(resultThreads)

ezgmail.summary(resultThreads)

# Downloading Attachments from a Gmail Account
import ezgmail
threads = ezgmail.search('vacation photos')
threads[0].messages[0].attachments

threads[0].messages[0].downloadAttachment('tulips.jpg')
threads[0].messages[0].downloadAllAttachments(downloadFolder='vacation2019')