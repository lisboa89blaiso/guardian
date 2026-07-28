import customtkinter as ctk
from datetime import datetime


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, width=300, corner_radius=0)

        self.grid_propagate(False)

        ctk.CTkLabel(
            self,
            text="GUARDIAN",
            font=("Arial", 28, "bold")
        ).pack(pady=(25, 20))

        self.guardian = ctk.CTkLabel(
            self,
            text="🟢 Guardian",
            anchor="w"
        )

        self.guardian.pack(fill="x", padx=20)

        self.camera = ctk.CTkLabel(
            self,
            text="🟢 Logitech Brio",
            anchor="w"
        )

        self.camera.pack(fill="x", padx=20)

        self.microfone = ctk.CTkLabel(
            self,
            text="🟢 Microfone",
            anchor="w"
        )

        self.microfone.pack(fill="x", padx=20)

        self.telegram = ctk.CTkLabel(
            self,
            text="⚪ Telegram",
            anchor="w"
        )

        self.telegram.pack(fill="x", padx=20)

        ctk.CTkLabel(
            self,
            text="EVENTOS",
            font=("Arial", 18, "bold")
        ).pack(pady=(30, 10))

        self.events = ctk.CTkTextbox(
            self,
            width=250,
            height=500
        )

        self.events.pack(padx=20)

    def add_event(self, text):

        hora = datetime.now().strftime("%H:%M:%S")

        self.events.insert(
            "end",
            f"[{hora}] {text}\n"
        )

        self.events.see("end")