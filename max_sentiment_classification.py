import requests as rq
import urllib
import json
from  pythonosc import udp_client

url = 'http://text-processing.com/api/sentiment/'
print("Welcome to sound narrator")
print("Please write a sentece and press enter")
print("The sentece will be kept secure. No worries ")
print("type 'exit' in order to go out")
print("_._._._._._._._._._._._._._._._._._._._._._._._._._._._")

while True:
    text_input = input()
    if text_input == "exit":
        break

    params={
        'text':text_input,
    }
    response = rq.post(url, data= params)
    # data = response.json()
    data = json.loads(response.text)
    k = data["probability"]
    label = data["label"]
    result = k.get(label)
    value = list(k.values())

    # print(result)
    # print("({})".format(label))
    # print (value)

    # ip, port = '192.168.43.179' , 5000
    ip, port = '127.0.0.1' , 5000

    client = udp_client.SimpleUDPClient(ip, port)

    msg = value
    client.send_message("/message",msg)
    # print ('sent {} to {}'.format(msg,ip))
