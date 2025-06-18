from video import listen_command, speak
from vision import ask_question

def main():
    while True:
        command = listen_command()
        if command:
            speak("Processing your request.")
            print("You said:", command)
            try:
                answer = ask_question(command)
                print("Jarvis:", answer)
                speak(answer)
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I could not get an answer.")

if _name_ == "_main_":
    main()
