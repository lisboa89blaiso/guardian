import cv2
import os
import threading
import time
from datetime import datetime


class VideoRecorder:

    def __init__(self):

        self.recording = False

        self.writer = None

        self.thread = None

        self.webcam = None

        self.path = None

        os.makedirs(
            "guardian_data/videos",
            exist_ok=True
        )

    def start(self, webcam, seconds=None):

        if self.recording:
            return None

        self.webcam = webcam

        self.recording = True

        filename = datetime.now().strftime("%Y%m%d_%H%M%S.mp4")

        self.path = os.path.join(
            "guardian_data/videos",
            filename
        )

        frame = webcam.get_frame()

        if frame is None:

            self.recording = False

            return None

        h, w = frame.shape[:2]

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        self.writer = cv2.VideoWriter(
            self.path,
            fourcc,
            20,
            (w, h)
        )

        self.thread = threading.Thread(
            target=self._loop,
            daemon=True
        )

        self.thread.start()

        if seconds is not None:

            timer = threading.Thread(
                target=self._auto_stop,
                args=(seconds,),
                daemon=True
            )

            timer.start()

        return self.path

    def _loop(self):

        while self.recording:

            frame = self.webcam.get_frame()

            if frame is not None:

                self.writer.write(frame)

            time.sleep(0.03)

    def _auto_stop(self, seconds):

        time.sleep(seconds)

        self.stop()

    def stop(self):

        if not self.recording:

            return self.path

        self.recording = False

        if self.thread:

            self.thread.join()

        if self.writer:

            self.writer.release()

            self.writer = None

        return self.path

    def is_recording(self):

        return self.recording