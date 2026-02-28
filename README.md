# Live Audio Transcriber

A real-time, offline audio transcription tool that captures your system's audio (YouTube, calls, games) and prints it word-by-word directly to your terminal. 

## Features
* **Completely Offline:** Powered by the Vosk AI model, meaning no internet connection is required after the initial local setup.
* **System Audio Capture:** Uses WASAPI loopback to listen directly to your desktop audio without needing third-party virtual audio cables.
* **Word-by-Word Streaming:** Text appears on the screen dynamically as words are spoken, creating a live-typing effect.
* **Auto-Formatting:** Automatically drops to a new line every 10 words to keep the terminal easily readable and prevent visual text-wrapping glitches.

## How to Use (Pre-built Executable)
If you just want to run the app without installing Python or setting up an environment, use the standalone executable.

1. Go to the **Releases** section on the right side of this GitHub repository.
2. Download the `transcribe.exe` file.
3. Double-click the file to run it. The very first launch may take a few seconds to initialize the local language model.
4. Wait for the terminal to display `READY. Play the video now...`
5. Start playing a video, game, or audio call, and the text will immediately start printing.

> **Note on Windows Defender:** Because this is an independently compiled `.exe` file without an expensive Microsoft developer certificate, Windows Defender may flag it with a blue "Windows protected your PC" screen. Simply click **More info** and then **Run anyway** to launch the transcriber.

## Build from Source
If you want to run the Python script directly or compile it yourself. Python 3.12 is highly recommended for compatibility with the required audio libraries.

### Installation
```cmd
python -m pip install pyaudiowpatch speechrecognition vosk pyinstaller
