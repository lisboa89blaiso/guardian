class EndEmergencyProtocol:

    def __init__(self, engine):

        self.engine = engine

    def execute(self):

        path = self.engine.video.stop()

        if path:

            self.engine.logger.info(

                f"Vídeo salvo: {path}"

            )

            self.engine.notification.notify(

                "PROTOCOLO FINALIZADO",

                path

            )