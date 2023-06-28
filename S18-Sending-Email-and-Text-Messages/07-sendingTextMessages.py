from twilio.rest import Client
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+14955551234'
myCellPhone = '+14955558888'
message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)

# The Message object returned from the create() method will 
# have information about the text message that was sent.
message.to

message.from_

message.body

# The status attribute should give you a string.
# The date_created and date_sent attributes should give you 
# a datetime object if the message has been created and sent.
message.status

message.date_created

message.date_sent == None

# Every Twilio message has a unique string ID (SID) that can 
# be used to fetch the latest update of the Message object.
message.sid

updatedMessage = twilioCli.messages.get(message.sid)
updatedMessage.status

updatedMessage.date_sent