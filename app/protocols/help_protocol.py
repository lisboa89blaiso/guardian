import threading

from app.core.protocol_state import ProtocolStatus
from app.services.audio_recorder import AudioRecorder


class HelpProtocol:

    def __init__(self, engine):

        self.engine = engine

        self.audio = AudioRecorder()
        self.audio.list_devices()
        

    def execute(self):

        self.engine.state.start(
            ProtocolStatus.HELP
        )

        frame = self.engine.webcam.get_frame()

        image_path = self.engine.screenshot.save(frame)

        if image_path:

            self.engine.window.update_preview(
                image_path
            )

            self.engine.logger.warning(
                f"Foto salva: {image_path}"
            )

        video_path = self.engine.video.start(
            self.engine.webcam,
            seconds=10
        )

        if video_path:

            self.engine.logger.warning(
                f"Vídeo iniciado: {video_path}"
            )

        audio_path = self.audio.start(
            seconds=10
        )

        if audio_path:

            self.engine.logger.warning(
                f"Áudio iniciado: {audio_path}"
            )

        self.engine.notification.notify(
            "AJUDA",
            "Protocolo iniciado."
        )

        threading.Thread(
            target=self._finish_after_recording,
            daemon=True
        ).start()

    def _finish_after_recording(self):

        while self.engine.video.is_recording():

            import time

            time.sleep(0.25)

        self.engine.state.finish()

        self.engine.logger.info(
            "Protocolo AJUDA finalizado automaticamente."
        )

        self.engine.notification.notify(
            "AJUDA",
            "Protocolo encerrado."
        )