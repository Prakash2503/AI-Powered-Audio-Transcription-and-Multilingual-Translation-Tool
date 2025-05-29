# AI-Powered-Audio-Transcription-and-Multilingual-Translation-Tool

# 🔊 AI-Powered Audio Transcription and Multilingual Translation Tool

## 🚀 Overview

This Python-based application empowers users to convert spoken English audio into written text and then translate that text into over 100 languages. It integrates OpenAI's state-of-the-art **Whisper** model for highly accurate speech-to-text transcription and leverages the **Google Translate API** for real-time translation. The goal is to enhance accessibility and remove language barriers across various fields like education, communication, and content localization.

---

## 💡 Key Features

### 🎙️ Speech-to-Text with Whisper
- Utilizes the `large-v3` variant of OpenAI’s **Whisper** model.
- Provides high accuracy in transcribing English audio, even with background noise or various accents.
- Works with `.mp3` and other common audio formats.

### 🌍 Multilingual Text Translation
- Translates the transcribed English text into any of **100+ supported languages** using the `googletrans` library.
- Supports language code input (e.g., `'hi'` for Hindi, `'fr'` for French, `'ta'` for Tamil).
- Ideal for building multilingual applications and user experiences.

### 🧠 Accessibility & Education Friendly
- Designed to help break down language barriers.
- Useful for e-learning platforms, inclusive applications, and multilingual documentation.
- Fully offline transcription with Whisper (no API required) and lightweight translation via Google Translate.

---

## 🔧 Technologies Used

| Tool        | Purpose                           |
|-------------|-----------------------------------|
| **Python**  | Core programming language         |
| **Whisper** | AI-based speech recognition       |
| **Googletrans** | Unofficial Google Translate API |
| **FFmpeg**  | Audio decoding for Whisper        |
| **CLI**     | Simple terminal-based interface   |

---

## 📂 How It Works

### Step 1: Provide the Audio File
- Upload an English audio file (`.mp3` format recommended).
- Make sure the file path is correctly set in the script.

### Step 2: Transcription with Whisper
- The Whisper model processes the audio and outputs the spoken content as text.
- Whisper performs **language detection**, **segmentation**, and **transcription** in one step.

### Step 3: Language Selection
- The app displays a list of supported languages and their respective codes.
- The user inputs the desired language code (e.g., `ta` for Tamil).

### Step 4: Real-Time Translation
- The `googletrans` library translates the transcribed English text into the selected target language.
- The translated output is printed to the terminal.

### Example Output:

🔊 Transcribing audio: sample.mp3

📝 Transcribed Text:
"Welcome to the AI-powered future of communication."

🌍 Available Languages:
hi : Hindi
fr : French
ta : Tamil
...

Enter target language code: ta

✅ Translated Text:
"தொலைத்தொடர்பு உலகில் AI மூலம் ஏற்படும் மாற்றத்திற்கு வரவேற்கிறோம்."

