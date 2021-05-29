import requests
from datetime import datetime
from twilio.rest import Client
import time

while True:
    twilio_client = Client("AC3f505f78f8c0e41fa941c89836840243", "006c666549917253882057b7e65c4658")
    today = datetime.today().strftime('%d-%m-%Y')
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?'

    somanur_pin = 641668
    singanalur_pin = 641005
    date = today

    somanur_url = url + "pincode=" + str(somanur_pin) + "&date=" + str(date)
    singanallur_url = url + "pincode=" + str(singanalur_pin) + "&date=" + str(date)

    somanur = requests.get(somanur_url)
    somanur_data = somanur.json()
    singanallur = requests.get(singanallur_url)
    singanallur_data = singanallur.json()

    print(somanur)
    print("*************")
    print(somanur_data)
    print(today)

    for i in somanur_data['sessions']:
        total_avl = i['available_capacity']
        dose1_avl = i['available_capacity_dose1']
        dose2_avl = i['available_capacity_dose2']

        if (total_avl >0) or (dose1_avl >0) or (dose2_avl >0):

            # phone_number = '9688574979'
            message =  "slot available in somanur 641668"
            twilio_message = twilio_client.messages.create(body=message, from_='+13159300063', to='+919688574979')
        else:
            pass


    for i in singanallur_data['sessions']:
        total_avl = i['available_capacity']
        dose1_avl = i['available_capacity_dose1']
        dose2_avl = i['available_capacity_dose2']

        if (total_avl >0) or (dose1_avl >0) or (dose2_avl >0):

            # phone_number = '9688574979'
            message =  "slot available in singanallur 641005"
            twilio_message = twilio_client.messages.create(body=message, from_='+13159300063', to='+919688574979')
        else:
            pass

    print("success")

    time.sleep(10)

