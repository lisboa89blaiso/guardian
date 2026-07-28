import cv2
import os
import threading
import time
from datetime import datetime

from app.graphics.video_overlay import VideoOverlay
from app.graphics.overlay_context import OverlayContext


class VideoRecorder:

    def __init__(self):

        self.recording = False

        self.writer = None
        self.thread = None

        self.webcam = None
        self.path = None

        self.overlay = VideoOverlay()

        self.context = OverlayContext()

        os.makedirs(
            "guardian_data/videos",
            exist_ok=True
        )

    def start(self, webcam, protocol="GRAVAÇÃO"):

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

        self.context.protocol = protocol
        self.context.started_at = datetime.now()
        self.context.recording = True

        self.recording = True

        self.thread = threading.Thread(
            target=self._record_loop,
            daemon=True
        )

        self.thread.start()

        return self.path

    def _record_loop(self):

        while self.recording:

            frame = self.webcam.get_frame()

            if frame is not None:

                now = datetime.now()

                self.context.now = now

                self.context.elapsed_seconds = int(
                    (
                        now -
                        self.context.started_at
                    ).total_seconds()
                )

                frame = self.overlay.draw(
                    frame,
                    self.context
                )

                self.writer.write(frame)

            time.sleep(0.03)

    def stop(self):

        if not self.recording:
            return self.path

        self.recording = False

        self.context.recording = False

        if self.thread is not None:
            self.thread.join()

        if self.writer is not None:
            self.writer.release()
            self.writer = None

        return self.path

    def is_recording(self):

        return self.recording