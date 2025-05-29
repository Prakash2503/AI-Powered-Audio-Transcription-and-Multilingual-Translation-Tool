import whisper
from googletrans import Translator, LANGUAGES
import os

# Load Whisper large-v3 model
model = whisper.load_model("large-v3")

# Initialize Google Translate
translator = Translator()

def transcribe_audio(audio_path):
    print(f"🔊 Transcribing audio: {audio_path}")
    result = model.transcribe(audio_path, language="en")
    return result["text"]

def translate_text(text, target_lang_code):
    print(f"🌐 Translating to: {target_lang_code}")
    try:
        translated = translator.translate(text, dest=target_lang_code)
        return translated.text
    except Exception as e:
        return f"Translation Error: {e}"

def show_languages():
    print("\n🌍 Available Languages:")
    for code, name in LANGUAGES.items():
        print(f"{code} : {name}")
    print("\n")

def main():
    # ✅ Use raw string to prevent path issues
    audio_path = r"/content/WhatsApp Audio 2025-05-28 at 12.19.58 PM.mp3"

    if not os.path.exists(audio_path):
        print("❌ File not found!")
        return

    english_text = transcribe_audio(audio_path)
    print("\n📝 Transcribed Text:\n", english_text)

    show_languages()
    target_lang_code = input("Enter target language code (e.g., 'hi' for Hindi): ").strip()

    translated = translate_text(english_text, target_lang_code)
    print("\n✅ Translated Text:\n", translated)

if __name__ == "__main__":
    main()
