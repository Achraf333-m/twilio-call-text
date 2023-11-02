from twilio.rest import Client
from datetime import datetime
import time



client = Client(twil_sid, twil_auth_token)

call_time = datetime(2023, 10, 26, 22, 30)
current_time = datetime.now()
time_difference = call_time - current_time
time_to_wait = time_difference.total_seconds()

# if time_to_wait > 0:
#     time.sleep(time_to_wait)
call = client.calls.create(
    from_="+16562185759",
    to="+14389698704",
    # to="+14387255776",
    url="https://handler.twilio.com/twiml/EH983e5e0bcd4e74d3e37b710a137ed3cb",
)
# while True:
#     message = client.messages.create(
#     from_='+16562185759',
#     body='you have won $5000, click here to get your prize blablablablabla',
#     to='+14389698704'
#     )

