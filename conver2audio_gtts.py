from gtts import gTTS


def convert_text_to_audio_gtts(text, output_filename="audiobook.mp3", lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_filename)
    print(f"Audiobook saved as {output_filename}")