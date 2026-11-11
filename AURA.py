import speech_recognition as sr
import pyttsx3
import json
import urllib.request
import urllib.error
import subprocess
import os

# Initialize AURA
recognizer = sr.Recognizer()

MODEL = "qwen2.5:1.5b"
URL = "http://localhost:11434/api/chat"

# Conversation memory
messages = [
    {
        "role": "system",
        "content": (
            "Your name is AURA. You are a helpful personal "
            "assistant. Always respond in English. "
            "Keep answers clear and conversational."
        )
    }
]


def speak(text):
    print("AURA:", text)

    engine = pyttsx3.init()

    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    engine.say(str(text))
    engine.runAndWait()

    engine.stop()
    del engine


def open_app(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe"
    }

    app_name = app_name.lower().strip()

    if app_name in apps:

        subprocess.Popen([apps[app_name]])
        speak("Opening " + app_name)
    else:
        speak("Sorry, I don't know this application yet.")


def close_app(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "CalculatorApp.exe",
        "paint": "mspaint.exe"
    }

    app_name = app_name.lower().strip()

    if app_name in apps:
        result = subprocess.run(
            ["taskkill", "/IM", apps[app_name]],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            speak("Closing " + app_name)
        else:
            speak("I couldn't close " + app_name)

    else:
        speak("I don't know this application yet.")


def open_folder(folder_name):
    folders = {
        "documents": os.path.expanduser("~/Documents"),
        "downloads": os.path.expanduser("~/Downloads"),
        "desktop": os.path.expanduser("~/Desktop"),
        "pictures": os.path.expanduser("~/Pictures")

    }

    folder_name = folder_name.lower().strip()

    if folder_name in folders:
        folder_path = folders[folder_name]

        if os.path.exists(folder_path):
            os.startfile(folder_path)
            speak("Opening " + folder_name)

        else:
            speak("This folder does not exist.")

    else:
        speak("I don't know this folder yet.")


def create_folder(folder_name):
    folder_name = folder_name.strip()

    folder_path = os.path.join(
        os.path.expanduser("~/Documents"),
        folder_name
    )

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        speak("Folder created successfully.")

    else:
        speak("This folder already exists.")


def delete_folder(folder_name):
    folder_name = folder_name.strip()

    folder_path = os.path.join(
        os.path.expanduser("~/Documents"),
        folder_name
    )

    if not os.path.exists(folder_path):
        speak("This folder does not exist.")
        return

    if not os.path.isdir(folder_path):
        speak("This is not a folder.")
        return

    speak("Are you sure you want to delete " + folder_name + "? Say yes or no.")

    confirmation = listen().lower().strip()

    if confirmation in ["yes", "yes please", "confirm"]:
        try:
            os.rmdir(folder_path)
            speak("Folder deleted successfully.")

        except OSError:
            speak("The folder is not empty or cannot be deleted.")

    else:
        speak("Deletion cancelled.")


def create_file(file_name):
    file_name = file_name.strip()

    file_path = os.path.join(
        os.path.expanduser("~/Documents"),
        file_name
    )

    if os.path.exists(file_path):
        speak("This file already exists.")
        return

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            pass

        speak("File created successfully.")

    except OSError as error:
        print("File error:", error)
        speak("I couldn't create the file.")


def listen():
    try:
        with sr.Microphone() as source:
            print("\nAURA: I'm listening...")

            recognizer.adjust_for_ambient_noise(
                source, duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

        text = recognizer.recognize_google(  # type: ignore
            audio,
            language="en-US"
        )

        print("YOU:", text)
        return text

    except sr.WaitTimeoutError:
        print("AURA: No speech detected.")
        return ""

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError as error:
        print("Speech recognition error:", error)
        speak("I cannot connect to speech recognition.")
        return ""

    except Exception as error:
        print("Microphone error:", error)
        return ""


def ask_ai(question):
    messages.append({
        "role": "user",
        "content": question
    })

    data = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    request = urllib.request.Request(
        URL,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(
            request, timeout=120
        ) as response:
            result = json.loads(
                response.read().decode("utf-8")
            )

        answer = result["message"]["content"]

        messages.append({
            "role": "assistant",
            "content": answer
        })

        return answer

    except urllib.error.URLError as error:
        print("Ollama connection error:", error)
        messages.pop()
        return "I cannot connect to my AI model."

    except Exception as error:
        print("AI error:", error)
        messages.pop()
        return "Something went wrong."


def main():
    speak("Hello! I am AURA. Your AI assistant is ready.")

    while True:
        command = listen()

        if not command:
            continue

        if command.lower().strip() in [
            "goodbye", "bye", "exit", "quit"
        ]:
            speak("Goodbye! Have a great day.")
            break

        if command.lower().startswith("open "):
            target = command[5:].strip()

            if target in ["documents", "downloads", "desktop", "pictures"]:
                open_folder(target)
            else:
                open_app(target)

        elif command.lower().startswith("close "):
            target = command[6:].strip()
            close_app(target)

        elif command.lower().startswith("create folder "):
            folder_name = command[14:].strip()
            create_folder(folder_name)

        elif command.lower().startswith("delete folder "):
            folder_name = command[14:].strip()
            delete_folder(folder_name)

        elif command.lower().startswith("create file "):
            folder_name = command[12:].strip()
            create_file(folder_name)

        else:
            answer = ask_ai(command)
            speak(answer)


if __name__ == "__main__":
    main()
