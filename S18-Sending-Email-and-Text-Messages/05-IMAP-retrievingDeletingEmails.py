import imapclient
imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)
imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')

imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2019'])
UIDs

rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])
message.get_subject()

message.get_addresses('from')

message.get_addresses('to')

message.get_addresses('cc')

message.get_addresses('bcc')

message.text_part != None

message.text_part.get_payload().decode(message.text_part.charset)

message.html_part != None

message.html_part.get_payload().decode(message.html_part.charset)

imapObj.logout()

# Connecting to an IMAP Server
import imapclient
imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)

# Logging In to the IMAP Server
imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')

# Searching for Email
### Selecting a Folder
import pprint
pprint.pprint(imapObj.list_folders())

# To select a folder to search through, pass the folder’s name as a string into the IMAPClient object’s select_folder() method.
imapObj.select_folder('INBOX', readonly=True)

### Performing the Search
imapObj.search(['ALL'])

imapObj.search(['ON 05-Jul-2019'])

imapObj.search(['SINCE 01-Jan-2019', 'BEFORE 01-Feb-2019', 'UNSEEN'])

imapObj.search(['SINCE 01-Jan-2019', 'FROM alice@example.com'])

imapObj.search(['SINCE 01-Jan-2019', 'NOT FROM alice@example.com'])

imapObj.search(['OR FROM alice@example.com FROM bob@example.com'])

imapObj.search(['FROM alice@example.com', 'FROM bob@example.com'])

# The search() method doesn’t return the emails themselves but rather unique IDs (UIDs)
UIDs = imapObj.search(['SINCE 05-Jul-2019'])
UIDs

### Size Limits
import imaplib
imaplib._MAXLINE = 10000000

### Fetching an Email and Marking It as Read
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
import pprint
pprint.pprint(rawMessages)

imapObj.select_folder('INBOX', readonly=False)

### Getting Email Addresses from a Raw Message
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])

# For example, the method calls might look like this:
message.get_subject()

message.get_addresses('from')

message.get_addresses('to')

message.get_addresses('cc')

message.get_addresses('bcc')

### Getting the Body from a Raw Message
message.text_part != None

message.text_part.get_payload().decode(message.text_part.charset)

message.html_part != None

message.html_part.get_payload().decode(message.html_part.charset)

### Deleting Emails
imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['ON 09-Jul-2019'])
UIDs

imapObj.delete_messages(UIDs)

imapObj.expunge()

### Disconnecting from the IMAP Server
imapObj.logout()