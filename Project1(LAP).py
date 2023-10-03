import speech_recognition as sr
from googletrans import Translator

# Create a recognizer instance
recognizer = sr.Recognizer()

# Function to check the microphone
def mic_check():
    with sr.Microphone() as source:
        print("Testing the microphone... Please speak a short test sentence.")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Microphone test successful. You can start speaking now.")
        except sr.WaitTimeoutError:
            print("No audio detected during the microphone test.")
        except sr.UnknownValueError:
            print("Microphone test failed. Please check your microphone setup.")

# Function to listen for 10 seconds and print spoken text
def listen_and_translate(language='en-US'):
    with sr.Microphone() as source:
        print(f"Listening for 10 seconds in {language}...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            spoken_text = recognizer.recognize_google(audio, language=language)
            if language == 'ur-PK':
                translator = Translator()
                translation = translator.translate(spoken_text, src='ur', dest='en')
                print(f"Translated (English): {translation.text}")
            else:
                print(f"Spoken ({language}): {spoken_text}")
        except sr.WaitTimeoutError:
            print("No speech detected during the 10-second timeout.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")

# Function to welcome the user and explain the program
def welcome_message():
    print()
    print("Welcome to the Language Selection and Speech Recognition Program!")
    while True:
        print()
        print("Choose a language for speech recognition:")
        print("1. English") 
        print("2. Urdu")
        print("3. Terminate the program")
        print()
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            listen_and_translate(language='en-US')
        elif choice == "2":
            listen_and_translate(language='ur-PK')
        elif choice == "3":
            print("Program terminated. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Display the welcome message and let the user choose
welcome_message()

