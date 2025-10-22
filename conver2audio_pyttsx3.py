import pyttsx3


def convert_text_to_audio_pyttsx3(text, output_filename=None):
    engine = pyttsx3.init()
    # Optional: Configure voice properties (rate, volume, voice ID)
    # engine.setProperty('rate', 150)
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id) # Example: set to first available voice

    if output_filename:
        engine.save_to_file(text, output_filename)
        engine.runAndWait()
        print(f"Audiobook saved as {output_filename}")
    else:
        engine.say(text)
        engine.runAndWait()
        print("Speaking text in real-time.")