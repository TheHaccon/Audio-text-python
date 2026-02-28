import pyaudiowpatch as pyaudio
import sys
import json
import audioop
from vosk import Model, KaldiRecognizer

def run_live():
    model = Model(lang="en-us")
    with pyaudio.PyAudio() as p:
        default_speakers = p.get_default_output_device_info()
        loopback = None
        for candidate in p.get_loopback_device_info_generator():
            if default_speakers["name"] in candidate["name"]:
                loopback = candidate
                break
        if not loopback:
            sys.exit()

        sample_rate = int(loopback["defaultSampleRate"])
        channels = loopback["maxInputChannels"]
        rec = KaldiRecognizer(model, sample_rate)
        stream = p.open(
            format=pyaudio.paInt16,
            channels=channels,
            rate=sample_rate,
            input=True,
            frames_per_buffer=4000,
            input_device_index=loopback["index"]
        )
        print("READY. Play the video now...")
        print("-" * 50)
        
        while True:
            try:
                data = stream.read(4000, exception_on_overflow=False)
                if channels > 1:
                    data = audioop.tomono(data, 2, 0.5, 0.5)
                    
                if rec.AcceptWaveform(data):
                    res = json.loads(rec.Result())
                    if res.get("text"):
                        sys.stdout.write("\r" + res["text"] + " " * 20 + "\n")
                        sys.stdout.flush()
                else:
                    partial = json.loads(rec.PartialResult())
                    if partial.get("partial"):
                        text = partial["partial"]
                        sys.stdout.write("\r" + text + " " * 20)
                        sys.stdout.flush()
                        
                        if len(text.split()) >= 10:
                            sys.stdout.write("\r" + text + " " * 20 + "\n")
                            sys.stdout.flush()
                            rec.Reset()
            except OSError:
                pass
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    run_live()