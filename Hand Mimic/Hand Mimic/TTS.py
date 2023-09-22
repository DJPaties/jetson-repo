
import os
from google.cloud import texttospeech
import pygame
import glob
import time
from mutagen.mp3 import MP3

lang_code = "en-US"


def tts(response_message):
   
        print("TTS")
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'tts.json'
        try:        
            
            client = texttospeech.TextToSpeechClient()
            print("Client created successfully.")
        except Exception as e:
            print("Error:", str(e))
        print("TTS")
        if response_message is not None:

            text = '<speak>'+""+response_message+""+'</speak>'
            synthesis_input = texttospeech.SynthesisInput(ssml=text)
            try:
                voice = texttospeech.VoiceSelectionParams(
                    language_code=lang_code ,
                    ssml_gender=texttospeech.SsmlVoiceGender.MALE,
                )
                audio_config = texttospeech.AudioConfig(
                            audio_encoding=texttospeech.AudioEncoding.MP3,
                        )
                response = client.synthesize_speech(
                            input=synthesis_input, voice=voice, audio_config=audio_config,
                        )


                filename = 'audio.mp3'
                with open(filename, 'wb') as out:
                    out.write(response.audio_content)
                pygame.mixer.init()
                pygame.mixer.music.load('dummy.mp3')
                files = glob.glob('audio*.mp3')
                for f in files:
                    try:
                        os.remove(f)
                    except OSError as e:
                        print("Error: %s - %s." % (e.filename, e.strerror))
                filename = 'audio' + str(pygame.time.get_ticks()) + '.mp3'
                with open(filename, 'wb') as out:
                    out.write(response.audio_content)
                audio = MP3(filename)
                
                print("MP3 audio length is ",audio.info.length)
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.2)  # Wait a second before checking again
            except Exception as e:
                print("Error occured ", e)

        else:
            print('no response message availbale')
    
# tts()