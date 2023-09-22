import os
import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import json

beard_detect = False
#the JSON file you downloaded in step 5 above
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'object.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

#set this thumbnail as the url
# image = types.Image()
# image.source.image_uri = 'https://i.ytimg.com/vi/UQQHSbeIaB0/maxresdefault.jpg'

with open('names.json', 'r') as json_file:
    data = json.load(json_file)
    object_names = data['object_names']

def analyze_image():
    file_name = 'sample.jpg'
    image_path = os.path.join('', file_name)

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image =types.Image(content=content)
    #### LABEL DETECTION ######
    detected_objects = ""
    response_label = client.label_detection(image=image)


        
    for label in response_label.label_annotations:
        print({'label': label.description, 'score': label.score})
        if label.description == "Beard" or label.description == "Facial hair":
            # print("yes, I see that you have a nice beard.")
            global beard_detect
            beard_detect = True
            break
    if beard_detect:
        print("Yes I can see you have a nice beard.")
    else:
        print("No i don't see you have a beard or any signs of it.")

    mobile_names = ["mobile phone","telephone","smartphone", "telephony","communication device","portable communications device"]
    cup_names = ["cup","mug"]
    bottles = ["Plastic bottle","bottle"]
    try:

        print("Entered Loop")
        telephone_count = 0
        cup_count = 0
        bottles_count = 0
        for label in response_label.label_annotations:
            matching_objects = [obj for obj in object_names if label.description.lower() == obj.lower()]
            if label.description.lower()  in mobile_names:
                
                if telephone_count>0:
                    pass
                else:
                    detected_objects += "smartphone , "
                telephone_count+=1
            elif label.description.lower()  in cup_names:
                
                if cup_count>0:
                    pass
                else:
                    detected_objects += "cup , "
                cup_count+=1
            elif label.description.lower()  in bottles:
                
                if bottles_count>0:
                    pass
                else:
                    detected_objects += "bottle , "
                bottles_count+=1
            elif matching_objects:
                print(f"User input '{label.description}' matches the object: '{matching_objects[0]}'")
                detected_objects += label.description + ", "
            print({'label': label.description, 'score': label.score})

        print("I can see:",detected_objects)
    except ValueError:
        print(ValueError)

# analyze_image("FindBeard")