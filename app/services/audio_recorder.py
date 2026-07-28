import os
import queue
import threading
from datetime import datetime

import sounddevice as sd
import soundfile as sf


class AudioRecorder:

    def __init__(self):

        self.recording = False

        self.device = None

        self.thread = None

        self.queue = queue.Queue()

        self.path = None

        os.makedirs(
            "guardian_data/audio",
            exist_ok=True
        )

    def start(self, device=None):

        if self.recording:
            return None

        self.device = device

        filename = datetime.now().strftime(
            "%Y%m%d_%H%M%S.wav"
        )

        self.path = os.path.join(
            "guardian_data",
            "audio",
            filename
        )

        self.recording = True

        self.thread = threading.Thread(
            target=self._record_loop,
            daemon=True
        )

        self.thread.start()

        return self.path

    def _callback(self, indata, frames, time_info, status):

        if self.recording:
            self.queue.put(indata.copy())

    def _record_loop(self):

        samplerate = 48000

        with sf.SoundFile(
            self.path,
            mode="w",
            samplerate=samplerate,
            channels=1,
            subtype="PCM_16"
        ) as file:

            with sd.InputStream(
                samplerate=samplerate,
                channels=1,
                dtype="int16",
                callback=self._callback,
                device=self.device
            ):

                while self.recording:

                    try:

                        file.write(
                            self.queue.get(timeout=0.2)
                        )

                    except queue.Empty:
                        pass

                while not self.queue.empty():

                    file.write(
                        self.queue.get_nowait()
                    )

    def stop(self):

        if not self.recording:
            return self.path

        self.recording = False

        if self.thread is not None:
            self.thread.join()

        return self.path

    def is_recording(self):

        return self.recording