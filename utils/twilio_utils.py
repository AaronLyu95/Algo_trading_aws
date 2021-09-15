from twilio.rest import Client
from utils.config import twilio_config



def twilio_message(message):
    account = twilio_config['sid']
    token = twilio_config['token']
    my_phone_number = twilio_config['my_phone_number']
    twilio_phone_number = twilio_config['twilio_phone_number']
    client = Client(account, token)

    send_message = client.messages.create(to=my_phone_number, from_=twilio_phone_number,
                                          body=message)

