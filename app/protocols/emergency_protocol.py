from app.core.protocol_state import ProtocolStatus


class EmergencyProtocol:

    def __init__(self, engine):

        self.engine = engine

    def execute(self):

        self.engine.state.start(
            ProtocolStatus.EMERGENCY
        )

        frame = self.engine.webcam.get_frame()

        path = self.engine.screenshot.save(frame)

        if path:

            self.engine.window.update_preview(path)

            self.engine.logger.critical(
                f"Captura salva: {path}"
            )

        self.engine.video.start(
            self.engine.webcam
        )

        self.engine.notification.notify(

            "EMERGÊNCIA",

            "Gravação iniciada."

        )

        self.engine.logger.critical(

            "Gravação de vídeo iniciada"

        )

        self.engine.logger.critical(

            "PROTOCOLO EMERGÊNCIA"

        )