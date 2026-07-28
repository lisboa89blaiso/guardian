import customtkinter as ctk


class StatusPanel(ctk.CTkFrame):

    def __init__(self, master, guardian):

        super().__init__(master, height=80)

        self.guardian = guardian

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(4, weight=2)

        self.camera = ctk.CTkLabel(
            self,
            text="📷 Câmera: Online",
            font=("Arial", 14, "bold")
        )

        self.camera.grid(
            row=0,
            column=0,
            padx=15,
            pady=20,
            sticky="w"
        )

        self.protocol = ctk.CTkLabel(
            self,
            text="⚪ Protocolo: IDLE",
            font=("Arial", 14, "bold")
        )

        self.protocol.grid(
            row=0,
            column=1,
            padx=15,
            pady=20,
            sticky="w"
        )

        self.recording = ctk.CTkLabel(
            self,
            text="⏺ REC: OFF",
            font=("Arial", 14, "bold")
        )

        self.recording.grid(
            row=0,
            column=2,
            padx=15,
            pady=20,
            sticky="w"
        )

        self.timer = ctk.CTkLabel(
            self,
            text="00:00",
            font=("Arial", 14, "bold")
        )

        self.timer.grid(
            row=0,
            column=3,
            padx=15,
            pady=20,
            sticky="w"
        )

        self.finish = ctk.CTkButton(
            self,
            text="ENCERRAR PROTOCOLO",
            command=self.finish_protocol,
            width=220
        )

        self.finish.grid(
            row=0,
            column=4,
            padx=20,
            pady=15,
            sticky="e"
        )

        self.update_status()

    def finish_protocol(self):

        self.guardian.finish_protocol()

    def update_status(self):

        state = self.guardian.state

        if state.active:

            self.protocol.configure(
                text=f"🔴 {state.status.value}"
            )

            self.recording.configure(
                text="🔴 REC"
            )

        else:

            self.protocol.configure(
                text="⚪ IDLE"
            )

            self.recording.configure(
                text="⏺ REC OFF"
            )

        if state.started_at:

            from datetime import datetime

            elapsed = datetime.now() - state.started_at

            seconds = int(elapsed.total_seconds())

            m = seconds // 60
            s = seconds % 60

            self.timer.configure(
                text=f"{m:02}:{s:02}"
            )

        else:

            self.timer.configure(
                text="00:00"
            )

        self.after(
            1000,
            self.update_status
        )