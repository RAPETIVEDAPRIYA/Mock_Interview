import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and speaker
recognizer = sr.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Processing...")
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Network error.")
            speak("Network error.")
        return ""
