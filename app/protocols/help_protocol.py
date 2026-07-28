import threading
import time

from app.core.protocol_state import ProtocolStatus


class HelpProtocol:

    def __init__(self, engine):

        self.engine = engine

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

        self.engine.media.record(
            self.engine.webcam,
            seconds=10
        )

        self.engine.logger.warning(
            "Gravação de áudio e vídeo iniciada."
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

        while self.engine.media.is_recording():
            time.sleep(0.25)

        self.engine.finish_protocol()