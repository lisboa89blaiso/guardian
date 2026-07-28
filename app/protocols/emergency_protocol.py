from app.core.protocol_state import ProtocolStatus


class EmergencyProtocol:

    def __init__(self, engine):

        self.engine = engine

    def execute(self):

        #
        # Marca o protocolo como ativo
        #

        self.engine.state.start(
            ProtocolStatus.EMERGENCY
        )

        #
        # Captura uma foto inicial
        #

        frame = self.engine.webcam.get_frame()

        image_path = self.engine.screenshot.save(frame)

        if image_path:

            self.engine.window.update_preview(
                image_path
            )

            self.engine.logger.critical(
                f"Captura salva: {image_path}"
            )

        #
        # Inicia gravação contínua
        #

        self.engine.media.start(
    self.engine.webcam,
    protocol="EMERGÊNCIA"
)

        self.engine.notification.notify(
            "EMERGÊNCIA",
            "Protocolo iniciado."
        )

        self.engine.logger.critical(
            "================================="
        )

        self.engine.logger.critical(
            "PROTOCOLO DE EMERGÊNCIA ATIVO"
        )

        self.engine.logger.critical(
            "Pressione F10 novamente para encerrar."
        )

        self.engine.logger.critical(
            "================================="
        )