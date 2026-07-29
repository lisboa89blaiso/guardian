import customtkinter as ctk
import cv2
import time

from PIL import Image
from PIL import ImageTk

from app.media.frame_listener import FrameListener


class PanelWindow(ctk.CTkToplevel, FrameListener):

    WIDTH = 460
    HEIGHT = 860

    ANIMATION_STEP = 18
    ANIMATION_DELAY = 8

    def __init__(self, root, webcam, actions):

        super().__init__(root)

        self.webcam = webcam
        self.actions = actions

        self.webcam.add_listener(self)

        self._photo = None
        self.animating = False

        self.timer_running = False
        self.timer_started_at = None

        self.withdraw()

        self.title("Guardian")

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        self.resizable(False, False)

        self.protocol(
            "WM_DELETE_WINDOW",
            self.hide
        )

        self._build()

    def _build(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        container = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        container.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        #
        # Header
        #

        header = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(30, 10)
        )

        ctk.CTkLabel(
            header,
            text="GUARDIAN",
            font=("Segoe UI", 28, "bold")
        ).pack()

        ctk.CTkLabel(
            header,
            text="Central de Emergência"
        ).pack()

        #
        # Preview
        #

        self.preview = ctk.CTkLabel(
            container,
            text="Inicializando câmera..."
        )

        self.preview.pack(
            padx=25,
            pady=20
        )

        #
        # Status
        #

        self.status_indicator = ctk.CTkLabel(container,text="🟢 PRONTO",font=("Segoe UI",18,"bold"))
        self.status_indicator.pack(pady=(5,0))

        self.status = ctk.CTkLabel(container,text="Aguardando comandos")
        self.status.pack(pady=(5,10))

        ctk.CTkLabel(container,text="TEMPO",font=("Segoe UI",11,"bold")).pack()

        self.timer_label = ctk.CTkLabel(container,text="00:00:00",font=("Consolas",26,"bold"))
        self.timer_label.pack(pady=(5,20))

        #
        # Botões
        #

        self.chat_button = ctk.CTkButton(
            container,
            text="💬 Conversar",
            height=52,
            command=self.actions.start_chat
        )

        self.chat_button.pack(
            fill="x",
            padx=30,
            pady=8
        )

        self.help_button = ctk.CTkButton(
            container,
            text="🟢 Pedir Ajuda",
            height=60,
            command=self.actions.start_help
        )

        self.help_button.pack(
            fill="x",
            padx=30,
            pady=8
        )

        self.emergency_button = ctk.CTkButton(
            container,
            text="🔴 Emergência",
            height=70,
            command=self.actions.start_emergency
        )

        self.emergency_button.pack(
            fill="x",
            padx=30,
            pady=(8, 25)
        )

        ctk.CTkLabel(
            container,
            text="Guardian v0.1"
        ).pack(
            side="bottom",
            pady=20
        )

    #
    # Webcam
    #

    def on_new_frame(self, frame):

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        media = self.actions.guardian.engine.media

        frame = media.video.renderer.render(
            frame,
            protocol=media.protocol,
            event_id=media.event_id,
            started_at=media.started_at,
        )

        image = Image.fromarray(frame)

        image.thumbnail(
            (390, 220)
        )

        photo = ImageTk.PhotoImage(image)

        def update():

            self.preview.configure(
                image=photo,
                text=""
            )

            self._photo = photo

        self.after(
            0,
            update
        )


    def set_status(self, mode, text=""):
        icons={"PRONTO":"🟢","CONVERSANDO":"🔵","AJUDA":"🟠","EMERGENCIA":"🔴"}
        self.status_indicator.configure(text=f"{icons.get(mode,'⚪')} {mode}")
        if text:
            self.status.configure(text=text)

    def start_timer(self):
        if self.timer_running:
            return
        self.timer_running=True
        import time
        self.timer_started_at=time.time()
        self._update_timer()

    def stop_timer(self):
        self.timer_running=False

    def reset_timer(self):
        self.timer_running=False
        self.timer_label.configure(text="00:00:00")

    def _update_timer(self):
        if not self.timer_running:
            return
        import time
        e=int(time.time()-self.timer_started_at)
        self.timer_label.configure(text=f"{e//3600:02}:{(e%3600)//60:02}:{e%60:02}")
        self.after(1000,self._update_timer)

    #
    # Window
    #

    def show(self):

        if self.animating:
            return

        if self.winfo_viewable():
            return

        self.animating = True

        self.update_idletasks()

        x = self.winfo_screenwidth() - self.WIDTH - 30

        final_y = 60
        start_y = -self.HEIGHT

        self.geometry(
            f"{self.WIDTH}x{self.HEIGHT}+{x}+{start_y}"
        )

        self.deiconify()

        self.attributes("-topmost", True)

        self.after(
            300,
            lambda: self.attributes("-topmost", False)
        )

        self.lift()

        def animate(y):

            if y >= final_y:

                self.geometry(
                    f"{self.WIDTH}x{self.HEIGHT}+{x}+{final_y}"
                )

                self.focus_force()

                self.animating = False

                return

            self.geometry(
                f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}"
            )

            self.after(
                self.ANIMATION_DELAY,
                lambda: animate(
                    y + self.ANIMATION_STEP
                )
            )

        animate(start_y)

    def hide(self):

        if self.animating:
            return

        if not self.winfo_viewable():
            return

        self.animating = True

        x = self.winfo_x()
        y = self.winfo_y()

        def animate(pos):

            if pos <= -self.HEIGHT:

                self.withdraw()

                self.animating = False

                return

            self.geometry(
                f"{self.WIDTH}x{self.HEIGHT}+{x}+{pos}"
            )

            self.after(
                self.ANIMATION_DELAY,
                lambda: animate(
                    pos - self.ANIMATION_STEP
                )
            )

        animate(y)