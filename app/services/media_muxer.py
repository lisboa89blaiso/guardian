import os
import subprocess


class MediaMuxer:

    def __init__(self):

        root = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                ".."
            )
        )

        self.ffmpeg = os.path.join(
            root,
            "ffmpeg",
            "ffmpeg.exe"
        )

    def exists(self):

        return os.path.exists(self.ffmpeg)

    def mux(self, video_path, audio_path, output_path):

        if not self.exists():
            raise FileNotFoundError(
                f"FFmpeg não encontrado:\n{self.ffmpeg}"
            )

        command = [

            self.ffmpeg,

            "-y",

            "-i", video_path,

            "-i", audio_path,

            "-c:v", "copy",

            "-c:a", "aac",

            "-shortest",

            output_path

        ]

        process = subprocess.run(

            command,

            stdout=subprocess.PIPE,

            stderr=subprocess.PIPE,

            text=True

        )

        if process.returncode != 0:

            print(process.stderr)

            return False

        return True