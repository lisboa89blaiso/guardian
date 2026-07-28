from datetime import datetime
import os
import threading
import time

from app.services.video_recorder import VideoRecorder
from app.services.audio_recorder import AudioRecorder
from app.services.media_muxer import MediaMuxer


class MediaSession:

    def __init__(self):

        self.video = VideoRecorder()
        self.audio = AudioRecorder()
        self.muxer = MediaMuxer()

        self.webcam = None
        self.timer = None

        os.makedirs(
            "guardian_data/recordings",
            exist_ok=True
        )

    def start(self, webcam):

        self.webcam = webcam

        self.audio.start()

        time.sleep(0.15)

        self.video.start(webcam)

    def record(self, webcam, seconds):

        self.start(webcam)

        self.timer = threading.Thread(
            target=self._auto_stop,
            args=(seconds,),
            daemon=True
        )

        self.timer.start()

    def _auto_stop(self, seconds):

        time.sleep(seconds)

        self.stop()

    def stop(self):

        audio_path = self.audio.stop()
        video_path = self.video.stop()

        if not video_path:
            return None

        if not audio_path:
            return video_path

        filename = datetime.now().strftime(
            "%Y%m%d_%H%M%S.mp4"
        )

        output = os.path.join(
            "guardian_data",
            "recordings",
            filename
        )

        ok = self.muxer.mux(
            video_path,
            audio_path,
            output
        )

        if ok:

            try:
                os.remove(video_path)
            except Exception:
                pass

            try:
                os.remove(audio_path)
            except Exception:
                pass

            return output

        return video_path

    def is_recording(self):

        return self.video.is_recording()