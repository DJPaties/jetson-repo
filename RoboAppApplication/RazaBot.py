import json
import requests
def send_message(msg):
    payload = {

                    "sender": "user1",
                    "message": msg
                }
    print("Payload done")
    r = requests.post('https://2711-185-127-125-57.ngrok.io/webhooks/rest/webhook', json=payload)
    print("Request done")
    data = r.json()

    # Process the response from the Rasa chatbot
    response = None
    for message in data:

        response = message["text"]

    try:
        return_Message = json.loads(response)
        x = (return_Message)
        print(x)
        return return_Message
    except ValueError as e :
        print("Response is not a json")
        
        return response

# while True:
#     msg = input("")
#     print(send_message(msg))


