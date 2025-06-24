## SPEECH RECOGNITION SYSTEM
import speech_recognition as sr

def transcribe_audio(file_path=None):
    recognizer = sr.Recognizer()

    try:
        if file_path:
            with sr.AudioFile(file_path) as source:
                audio = recognizer.record(source)
        else:
with sr.Microphone() as source:
                print("Listening.")
                audio = recognizer.listen(source)

        # You can use other recognizers also like Google, Sphinx, etc.
text = recognizer.recognize_google(audio)
        return f"Transcription: {text}"

    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Request error from Google API: {e}"

# Example usage:
# Substitute 'sample.wav' with the location of your audio file
print(transcribe_audio("sample.wav"))

