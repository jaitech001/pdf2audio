from conver2audio_gtts import convert_text_to_audio_gtts
from conver2audio_pyttsx3 import convert_text_to_audio_pyttsx3
from readpdf import extract_text_from_pdf

# Example Usage
pdf_file = "Jaishankar Varadharajan.pdf"  # Replace with your PDF file path
extracted_text = extract_text_from_pdf(pdf_file)

if extracted_text:
    # Option 1: Save as MP3 using gTTS
    convert_text_to_audio_gtts(extracted_text, "my_audiobook1.mp3")

    # Option 2: Speak in real-time or save using pyttsx3
    convert_text_to_audio_pyttsx3(extracted_text, "my_audiobook2.wav") # Save as WAV
    # convert_text_to_audio_pyttsx3(extracted_text) # Speak in real-time
else:
    print("Could not extract text from the PDF.")