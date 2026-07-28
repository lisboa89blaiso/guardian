from app.core.protocol_state import ProtocolStatus


class EmergencyProtocol:

    def __init__(self, engine):

        self.engine = engine

    def execute(self):

        self.engine.state.start(
            ProtocolStatus.EMERGENCY
        )

        frame = self.engine.webcam.get_frame()

        image_path = self.engine.screenshot.save(frame)

        if image_path:

            self.engine.window.update_preview(
                image_path
            )

            self.engine.logger.critical(
                f"Captura salva: {image_path}"
            )

        self.engine.media.start(
            self.engine.webcam
        )

        self.engine.logger.critical(
            "Gravação de áudio e vídeo iniciada."
        )

        self.engine.notification.notify(
            "EMERGÊNCIA",
            "Protocolo iniciado."
        )

        self.engine.logger.critical(
            "PROTOCOLO EMERGÊNCIA"
        )