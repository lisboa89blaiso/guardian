import os
import threading
from datetime import datetime

import sounddevice as sd
import soundfile as sf


class AudioRecorder:

    def __init__(self):

        self.recording = False
        self.thread = None
        self.device = None

        os.makedirs(
            "guardian_data/audio",
            exist_ok=True
        )

    def list_devices(self):

        devices = sd.query_devices()

        print("\n======= DISPOSITIVOS DE ÁUDIO =======\n")

        for i, d in enumerate(devices):

            if d["max_input_channels"] > 0:

                print(
                    f"{i} - {d['name']}"
                )

        print("\n=====================================\n")

    def set_device(self, index):

        self.device = index

    def start(self, seconds=10):

        if self.recording:

            return None

        self.recording = True

        filename = datetime.now().strftime("%Y%m%d_%H%M%S.wav")

        self.path = os.path.join(
            "guardian_data/audio",
            filename
        )

        self.thread = threading.Thread(

            target=self._record,

            args=(seconds,),

            daemon=True

        )

        self.thread.start()

        return self.path

    def _record(self, seconds):

        samplerate = 48000

        audio = sd.rec(

            int(seconds * samplerate),

            samplerate=samplerate,

            channels=1,

            dtype="int16",

            device=self.device

        )

        sd.wait()

        sf.write(

            self.path,

            audio,

            samplerate

        )

        self.recording = False

    def is_recording(self):

        return self.recording