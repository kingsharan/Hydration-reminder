# Imports
import datetime
import time
import requests
import json
from boltiot import Bolt
import credentials


mybolt = Bolt(credentials.api_key, credentials.device_id) # Set up bolt iot

# Create function to send message


def send_notification_via_pushbullet(title, body):
    data_send = {"type": "note", "title": title, "body": body}
    ACCESS_TOKEN = 'o.6MScsh07m2sRw3pqzTUSbhGBDtlKxAAb'
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

def alarm():
    mybolt.digitalWrite('0', 'HIGH')
    time.sleep(1)
    mybolt.digitalWrite('0', 'LOW')
    time.sleep(1)
    mybolt.digitalWrite('0', 'HIGH')
    time.sleep(1)
    mybolt.digitalWrite('0', 'LOW')
    time.sleep(1)


send = send_notification_via_pushbullet  # set up variable to send messages

while True:


    current_time = datetime.datetime.now()

    print(current_time.hour, current_time.minute, current_time.second)

    time.sleep(1)
    water_reminder_time = [9,10,11,12,13,14,15,16,17,18,19,20]
    my_event = [15,19]

    if current_time.hour in water_reminder_time and current_time.minute == 00 :
        send("Water Reminder", "Time to hydrate")
        alarm()
        print(current_time.hour)
        time.sleep(300)
    if  current_time.hour in my_event :


        send("Event","It is time for you event")
        alarm()
        print(current_time.hour, current_time.minute, current_time.second)
        time.sleep(3)

