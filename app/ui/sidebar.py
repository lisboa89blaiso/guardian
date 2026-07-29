import customtkinter as ctk
from datetime import datetime


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            width=500,
            corner_radius=0
        )

        self.grid_propagate(False)

        # --------------------------------------------------
        # HEADER
        # --------------------------------------------------

        ctk.CTkLabel(
            self,
            text="GUARDIAN",
            font=("Arial", 30, "bold")
        ).pack(pady=(28, 0))

        ctk.CTkLabel(
            self,
            text="Personal Safety AI",
            font=("Arial", 12),
            text_color="gray70"
        ).pack(pady=(0, 22))

        self._separator()

        # --------------------------------------------------
        # MENU
        # --------------------------------------------------

        self._section_title("MENU")

        self._menu_item("🏠  Início")
        self._menu_item("📹  Sessão")
        self._menu_item("🤖  IA")
        self._menu_item("⚙️  Configurações")

        self._separator(pady=18)

        # --------------------------------------------------
        # STATUS
        # --------------------------------------------------

        self._section_title("STATUS")

        self.guardian = self._status_item(
            "🟢 Guardian"
        )

        self.camera = self._status_item(
            "🟢 Webcam"
        )

        self.microfone = self._status_item(
            "🟢 Microfone"
        )

        self.telegram = self._status_item(
            "⚪ Telegram"
        )

        self._separator(pady=18)

        # --------------------------------------------------
        # EVENTOS
        # --------------------------------------------------

        self._section_title("ATIVIDADE")

        self.events = ctk.CTkTextbox(
            self,
            corner_radius=10,
            border_width=0,
            wrap="word",
            font=("Consolas", 12)
        )

        self.events.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(8, 15)
        )

        self.events.configure(state="disabled")

    # ======================================================
    # HELPERS
    # ======================================================

    def _section_title(self, text):

        ctk.CTkLabel(
            self,
            text=text,
            font=("Arial", 15, "bold"),
            anchor="w"
        ).pack(
            fill="x",
            padx=18,
            pady=(0, 8)
        )

    def _separator(self, pady=22):

        ctk.CTkFrame(
            self,
            height=1
        ).pack(
            fill="x",
            padx=15,
            pady=pady
        )

    def _menu_item(self, text):

        ctk.CTkLabel(
            self,
            text=text,
            anchor="w",
            font=("Arial", 14)
        ).pack(
            fill="x",
            padx=20,
            pady=6
        )

    def _status_item(self, text):

        label = ctk.CTkLabel(
            self,
            text=text,
            anchor="w",
            font=("Arial", 14)
        )

        label.pack(
            fill="x",
            padx=20,
            pady=4
        )

        return label

    # ======================================================
    # LOG
    # ======================================================

    def add_event(self, text):

        hora = datetime.now().strftime("%H:%M:%S")

        self.events.configure(state="normal")

        self.events.insert(
            "end",
            f"[{hora}] {text}\n"
        )

        self.events.see("end")

        self.events.configure(state="disabled")