import speech_recognition as sr
import pyaudio
import pyautogui
# Create a recognizer object
r = sr.Recognizer()
key = ""
# Use microphone as source
while True:
    with sr.Microphone() as source:
        print("Speak something...")
        # Listen for audio and capture it
        audio = r.listen(source)


    try:
        print(key)
        # Use Google Speech Recognition to recognize the audio
        text = r.recognize_google(audio, language='pt-BR')
        if "esquerda" in text:
            pyautogui.keyUp(key)
            key = "a"
            print("deu certo a esquerda")
        elif "direita" in text:
            pyautogui.keyUp(key)
            key = "d"
            print("deu certo a direita")
        elif "cima" in text:
            pyautogui.keyUp(key)
            key = "w"
            print("deu certo a cima")
        elif "baixo" in text:
            pyautogui.keyUp(key)
            key = "s"
            print("deu certo a baixo")
        print(f"You said: {text}")
        text = ""
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    if key != "":
        pyautogui.keyDown(key)


