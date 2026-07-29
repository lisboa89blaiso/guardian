import customtkinter as ctk
from datetime import datetime


class StatusPanel(ctk.CTkFrame):

    def __init__(self, master, guardian):

        super().__init__(
            master,
            height=60,
            corner_radius=12
        )

        self.guardian = guardian
        self.engine = guardian.engine

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=0)

        #
        # WEBCAM
        #

        self.camera = ctk.CTkLabel(
            self,
            text="📷 Webcam • Online",
            font=("Arial", 14, "bold"),
            anchor="w"
        )

        self.camera.grid(
            row=0,
            column=0,
            padx=(20, 10),
            pady=15,
            sticky="w"
        )

        #
        # STATUS
        #

        self.protocol = ctk.CTkLabel(
            self,
            text="🛡 Pronto",
            font=("Arial", 14, "bold"),
            anchor="w"
        )

        self.protocol.grid(
            row=0,
            column=1,
            padx=10,
            pady=15,
            sticky="w"
        )

        #
        # GRAVAÇÃO
        #

        self.recording = ctk.CTkLabel(
            self,
            text="⏺ Gravação desligada",
            font=("Arial", 14),
            anchor="w"
        )

        self.recording.grid(
            row=0,
            column=2,
            padx=10,
            pady=15,
            sticky="w"
        )

        #
        # TIMER
        #

        self.timer = ctk.CTkLabel(
            self,
            text="⏱ 00:00",
            font=("Arial", 18, "bold")
        )

        self.timer.grid(
            row=0,
            column=3,
            padx=10,
            pady=15
        )

        #
        # BOTÃO
        #

        self.finish = ctk.CTkButton(
            self,
            text="Encerrar protocolo",
            width=180,
            height=36,
            command=self.finish_protocol
        )

        self.finish.grid(
            row=0,
            column=4,
            padx=(10, 20),
            pady=12,
            sticky="e"
        )

        self.update_status()

    # =====================================================

    def finish_protocol(self):

        self.engine.finish_protocol()

    # =====================================================

    def update_status(self):

        state = self.engine.state

        if state.active:

            status = state.status.value.upper()

            if status == "HELP":

                self.protocol.configure(
                    text="🟡 Pedido de ajuda"
                )

            elif status == "EMERGENCY":

                self.protocol.configure(
                    text="🔴 Emergência"
                )

            elif status == "CONVERSATION":

                self.protocol.configure(
                    text="💬 Em conversa"
                )

            elif status == "FINISHED":

                self.protocol.configure(
                    text="⚪ Finalizado"
                )

            else:

                self.protocol.configure(
                    text=f"🛡 {state.status.value}"
                )

            self.recording.configure(
                text="🔴 Gravando"
            )

        else:

            self.protocol.configure(
                text="🛡 Pronto"
            )

            self.recording.configure(
                text="⏺ Gravação desligada"
            )

        #
        # TIMER
        #

        if state.started_at:

            elapsed = datetime.now() - state.started_at

            seconds = int(
                elapsed.total_seconds()
            )

            minutes = seconds // 60
            seconds = seconds % 60

            self.timer.configure(
                text=f"⏱ {minutes:02}:{seconds:02}"
            )

        else:

            self.timer.configure(
                text="⏱ 00:00"
            )

        self.after(
            1000,
            self.update_status
        )