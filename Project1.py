import speech_recognition as sr

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
def listen_and_print():
    with sr.Microphone() as source:
        print("Listening for 10 seconds...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            spoken_text = recognizer.recognize_google(audio)
            print(f"Spoken: {spoken_text}")
        except sr.WaitTimeoutError:
            print("No speech detected during the 10-second timeout.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            

# Check the microphone before proceeding
mic_check()

# Call the function to listen and print spoken text
listen_and_print()
