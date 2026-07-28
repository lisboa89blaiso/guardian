from app.core.event_logger import EventLogger
from app.core.protocol_engine import ProtocolEngine
from app.core.protocol_state import ProtocolState

from app.services.notification_service import NotificationService
from app.services.media_session import MediaSession


class GuardianEngine:

    def __init__(self, window, webcam, screenshot):

        self.window = window
        self.webcam = webcam
        self.screenshot = screenshot

        self.state = ProtocolState()

        self.logger = EventLogger(
            window.sidebar
        )

        self.notification = NotificationService()

        self.media = MediaSession()

        self.protocols = ProtocolEngine(
            self
        )

    def conversar(self):

        self.logger.info(
            "Quero conversar"
        )

    def ligar_papai(self):

        self.logger.info(
            "Ligar para papai"
        )

    def ajuda(self):

        if self.state.active:

            self.logger.warning(
                "Já existe um protocolo em execução."
            )

            return

        self.protocols.execute(
            "help"
        )

    def emergencia(self):

        if self.state.active:

            self.logger.warning(
                "Já existe um protocolo em execução."
            )

            return

        self.protocols.execute(
            "emergency"
        )

    def finish_protocol(self):

        if not self.state.active:
            return

        final_video = self.media.stop()

        if final_video:

            self.logger.info(
                f"Gravação salva: {final_video}"
            )

        self.state.finish()

        self.notification.notify(
            "PROTOCOLO",
            "Encerrado."
        )

        self.logger.info(
            "Protocolo encerrado."
        )