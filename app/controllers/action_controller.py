class ActionController:

    def __init__(self, status, session):

        self.status = status
        self.session = session
        self.guardian = None

    def bind_guardian(self, guardian):

        self.guardian = guardian

    def start_help(self):

        self.status.set_help()

        self.session.start(
            "AJUDA",
            None
        )

        if self.guardian is None:
            return

        self.guardian.engine.ajuda()

    def start_emergency(self):

        if self.guardian is None:
            return

        #
        # Emergência já ativa
        #

        if self.guardian.engine.state.active:

            self.stop_protocol()

            return

        self.status.set_emergency()

        self.session.start(
            "EMERGÊNCIA",
            None
        )

        self.guardian.engine.emergencia()

    def stop_protocol(self, update_engine=True):

        self.status.set_idle()

        self.session.finish()

        if (
            update_engine
            and
            self.guardian is not None
        ):

            self.guardian.engine.finish_protocol()

    def start_chat(self):

        self.status.set_chat()

        self.session.start(
            "CONVERSA",
            None
        )

        if self.guardian is None:
            return

        self.guardian.engine.conversar()