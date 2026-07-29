class StatusController:

    def __init__(self):

        self.panel = None

        self.windows = []

        self.protocol = "Sistema Pronto"

        self.recording = False

    def bind_panel(self, panel):

        self.panel = panel

    def register(self, window):

        if window not in self.windows:
            self.windows.append(window)

        self.refresh()

    def unregister(self, window):

        if window in self.windows:
            self.windows.remove(window)

    def set_chat(self):

        if self.panel:

            self.panel.set_status(
                "CONVERSANDO",
                "Conversando..."
            )

            self.panel.start_timer()

        self.protocol = "Conversando"
        self.recording = False

        self.refresh()

    def set_idle(self):

        if self.panel:

            self.panel.set_status(
                "PRONTO",
                "Aguardando comandos"
            )

            self.panel.reset_timer()

        self.protocol = "Sistema Pronto"
        self.recording = False

        self.refresh()

    def set_help(self):

        if self.panel:

            self.panel.set_status(
                "AJUDA",
                "Solicitando ajuda..."
            )

            self.panel.start_timer()

        self.protocol = "Protocolo de Ajuda"
        self.recording = True

        self.refresh()

    def set_emergency(self):

        if self.panel:

            self.panel.set_status(
                "EMERGÊNCIA",
                "Gravando e enviando..."
            )

            self.panel.start_timer()

        self.protocol = "EMERGÊNCIA"
        self.recording = True

        self.refresh()

    def refresh(self):

        for window in self.windows:

            try:

                window.update_status(
                    self.protocol,
                    self.recording
                )

            except Exception:
                pass