import speech_recognition as sr # just creating a shortcut of using this module as 'sr' #speech_recognition library is used to convert spoken language (audio) into text
import webbrowser # webbrowser module in Python is used to open URLs in your default web browser
import pyttsx3 # pyttsx3 is a text-to-speech conversion library in Python.
import music_library
import requests # using in "news" section
from openai import OpenAI
# from gtts import gTTS # for gTTs
# import pygame # for gTTs
# import os # for gTTs
from dotenv import load_dotenv # pip install python-dotenv==1.0.1
import os

load_dotenv()  # Loading environment variables from .env

openai_api_key = os.getenv("OPENAI_API_KEY")
newsapi = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer() # this helps to use us speech recognation functionality
engine = pyttsx3.init() # it initialises pyttsx to use it,initializes the text-to-speech engine
newsapi = "4404dba6ce3e4d68a0b8b4dd5e94d58a"

# Get all available voices
voices = engine.getProperty('voices')


def speak(text):
    engine.setProperty('voice', voices[0].id)  # Example: 0 for male, 1 for female on most system
    engine.say(text) # tells the pyttsx3 engine to prepare to speak the text that you pass to it, {.say(text)} queues the text for speech — it doesn't actually speak it yet.
    engine.runAndWait() # its what actually runs the speech engine and makes it speak the queued text.


'''
# this(below) a better choice to use it but it is limited also there are some more choices you can ask chat gpt

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    # go to chatgpt "how to play mp3 in pygame"


    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("your_audio.mp3")  # Replace with your MP3 file name

    # Play the music
    pygame.mixer.music.play()

    # Keep the program running while the music is playing
    while pygame.mixer.music.get_busy():
        pygame.time.sleep(1)  # wait for 1 second

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
'''

def aiprocess(command):
    client = OpenAI(api_key=openai_api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Madhav skilled in general tasks like alexa and google cloud, give short responses!!"},
            {"role": "user", "content": "what is coding"}
        ]
    )

    return response.choices[0].message.content  


# after activating Madhav we give him command and it process and find requirements here
def processcommand(c): 
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"): 
        print("playing")
        song = " ".join(c.lower().split(" ")[1:])  # gets everything after 'play'
        link = music_library.music.get(song)

        if link:
            webbrowser.open(link)
        else:
            print(f"Song '{song}' not found in music library.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        if r.status_code == 200:
            
            #Parse the JSON response
            data = r.json()

            # extract the articels
            articles = data.get("articles", [])

            if articles:
                for i, article in enumerate(articles[:5], start=1):  # Top 5 headlines
                    print(f"{i}. {article['title']}")
                    speak(f"{i}. {article['title']}")
            else:
                print("No news articles found.")
        else:
            print("Failed to fetch news. Please check your API key or try later.")
    else:
        #let openai handle now
        output = aiprocess(c)
        print(output)
        speak(output)

if __name__ == "__main__": #This ensures that the code below runs only if this file is executed directly
    speak("Initialising Madhav.....") # This ai asistance speaks this text since we already had defined speak() using pyttx3

    r = sr.Recognizer() # Creates a new speech recognizer object r to convert audio to text.
    while True: # An infinite loop — keeps listening continuously until stopped manually
        # listen for the wake word "krio" then only obtain audio from microphone

        print("recognising..")
        try:
            with sr.Microphone() as source: # uses microphone to record what the user says.
                print("Listening...")
                audio = r.listen(source,timeout=1,phrase_time_limit=3) # The r.listen(source) listen for 2 sec and captures the voice and stores it in the audio variable
                
            word = r.recognize_google(audio) # Converts the spoken input (in audio) into text using Google’s speech recognition service.
            if(word.lower() == "madhav"):
                print("Hari Bol")
                speak("Hari Boll..")
                # Listen for command
                with sr.Microphone() as source: # uses microphone to record what the user says.
                    print("Madhav active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)
            
  
        except Exception as e:
            print("Erorr; {0}".format(e))
