from twilio.rest import Client 
 
def message(x,y):
    account_sid = 'AC874ba10657a496bd165a2af123412093' 
    auth_token = '[AuthToken]' 
    client = Client(account_sid, auth_token)

    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=y,      
                              to=x 
                          ) 

print(message.sid) 