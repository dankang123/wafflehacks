from twilio.rest import Client 
import smtplib 
#  variable x y, converts number into a message, where x is the number and y is the message
def message(x,y):
    message = f"whatsapp:{x}"
    account_sid = 'AC874ba10657a496bd165a2af123412093' 
    auth_token = 'f6eb61a0efa76563d2d29d3eb71defce' 
    client = Client(account_sid, auth_token)

    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=y,      
                              to=message
                          ) 

def event_mail(x,y):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("NJ12jonathan@gmail.com", 'Jonathan@2007') 

    msg = f"Subject: Food kitchen event\n\n{y}"

    server.sendmail(
        "NJ12jonathan@gmail.com",
        f"{x}",
        msg
    )
    server.quit()