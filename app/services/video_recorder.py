import cv2
import os
import threading
import time
from datetime import datetime

from app.graphics.frame_renderer import FrameRenderer


class VideoRecorder:

    def __init__(self):

        self.recording = False
        self.protocol = "PRONTO"
        self.event_id = ""
        self.started_at = None
        self.writer = None
        self.thread = None

        self.webcam = None
        self.path = None

        self.renderer = FrameRenderer()

        os.makedirs(
            "guardian_data/videos",
            exist_ok=True
        )

    def start(self, webcam, protocol="GRAVAÇÃO", event_id=""):

        if self.recording:
            return None

        self.webcam = webcam

        frame = webcam.get_frame()

        if frame is None:
            return None

        filename = datetime.now().strftime(
            "%Y%m%d_%H%M%S.mp4"
        )

        self.path = os.path.join(
            "guardian_data",
            "videos",
            filename
        )

        h, w = frame.shape[:2]

        self.writer = cv2.VideoWriter(
            self.path,
            cv2.VideoWriter_fourcc(*"mp4v"),
            20,
            (w, h)
        )

        self.protocol = protocol
        self.event_id = event_id
        self.started_at = datetime.now()

        self.recording = True

        self.thread = threading.Thread(
            target=self._record_loop,
            daemon=True
        )

        self.thread.start()

        self.protocol = protocol
        self.event_id = event_id
        self.started_at = datetime.now()

        return self.path

    def _record_loop(self):

        while self.recording:

            frame = self.webcam.get_frame()

            if frame is not None:

                frame = self.renderer.render(
                    frame,
                    protocol=self.protocol,
                    event_id=self.event_id,
                    started_at=self.started_at,
                )

                self.writer.write(frame)

            time.sleep(0.03)

    def stop(self):

        if not self.recording:
            return self.path

        self.recording = False

    
        if self.thread is not None:
            self.thread.join()

        if self.writer is not None:
            self.writer.release()
            self.writer = None

        return self.path

    def is_recording(self):

        return self.recording