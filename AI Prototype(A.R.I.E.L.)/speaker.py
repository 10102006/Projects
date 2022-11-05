"""
STATUS: Working

OVERVIEW: Uses [pyttsx3] to give a sound output for given string

IMPROVEMENTS:
    - TODO add Regular Expression to format the message

"""

# @ Imports
import pyttsx3

# * Defining
engine = pyttsx3.init()

voices = engine.getProperty("voices")  # ? For getting avail voices

# ? For changing the voice of speaker
engine.setProperty(
    'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')


def Speak(message):
    engine.say(message)
    engine.runAndWait() # * Finishing command


# ? Implementation
if __name__ == "__main__":
    [print(voice.id) for voice in voices]  # ? For printing avail voices
    Speak("Hello World")
