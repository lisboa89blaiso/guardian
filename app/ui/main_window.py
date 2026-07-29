import customtkinter as ctk
import cv2


from app.media.frame_listener import FrameListener
from PIL import Image
from PIL import ImageTk
from app.ui.sidebar import Sidebar
from app.ui.status_panel import StatusPanel


class MainWindow(FrameListener):

    def __init__(self, webcam, actions):

        self.webcam = webcam
        self.webcam.add_listener(self)
        self.actions = actions
        self.guardian = None
        self.status_panel = None

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Guardian")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        #
        # GRID PRINCIPAL
        #

        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=1)

        self.root.grid_rowconfigure(0, weight=1)

        #
        # SIDEBAR
        #
       
        self.sidebar = Sidebar(self.root)
        
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        #
        # ÁREA PRINCIPAL
        #

        self.main = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

        self.main.grid_columnconfigure(0, weight=1)

        self.main.grid_rowconfigure(0, weight=1)
        self.main.grid_rowconfigure(1, weight=0)
        self.main.grid_rowconfigure(2, weight=0)
        self.main.grid_rowconfigure(3, weight=0)

        #
        # WEBCAM
        #

        self.camera_frame = ctk.CTkFrame(self.main)

        self.camera_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.camera_frame.grid_propagate(False)

        self.camera_frame.configure(
            width=1920,
            height=1080
        )

        self.camera_label = ctk.CTkLabel(
            self.camera_frame,
            text=""
        )

        self.camera_label.pack(
            expand=True,
        )

        #
        # STATUS
        #

        #
        # MENSAGEM
        #

        self.message_frame = ctk.CTkFrame(self.main)

        self.message_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(18, 0)
        )

        self.message_label = ctk.CTkLabel(
            self.message_frame,
            text="Guardian pronto para ajudar.",
            anchor="w",
            justify="left",
            font=ctk.CTkFont(size=16)
        )

        self.message_label.pack(
            fill="x",
            padx=20,
            pady=16
        )

        #
        # BOTÕES
        #

        self.buttons_frame = ctk.CTkFrame(self.main)

        self.buttons_frame.grid(
            row=3,
            column=0,
            sticky="ew",
            pady=(18, 0)
        )

        self.buttons_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.btn_conversation = ctk.CTkButton(
            self.buttons_frame,
            text="💬 Conversar",
            height=48,
            command=self.start_conversation
        )

        self.btn_conversation.grid(
            row=0,
            column=0,
            padx=10,
            pady=15,
            sticky="ew"
        )

        self.btn_help = ctk.CTkButton(
            self.buttons_frame,
            text="🟢 Pedir ajuda",
            height=48,
            command=self.start_help
        )

        self.btn_help.grid(
            row=0,
            column=1,
            padx=10,
            pady=15,
            sticky="ew"
        )

        self.btn_emergency = ctk.CTkButton(
            self.buttons_frame,
            text="🔴 Emergência",
            height=48,
            command=self.start_emergency
        )

        self.btn_emergency.grid(
            row=0,
            column=2,
            padx=10,
            pady=15,
            sticky="ew"
        )
    def bind_guardian(self, guardian):

        self.guardian = guardian

        self.actions.bind_guardian(guardian)

        if self.status_panel is None:

            self.status_panel = StatusPanel(
                self.main,
                guardian
            )

            self.status_panel.grid(
                row=1,
                column=0,
                sticky="ew",
                pady=(18, 0)
            )

    def set_message(self, message):

        self.message_label.configure(text=message)


    def start_conversation(self):

        if self.actions is not None:
         self.actions.start_chat()


    def start_help(self):

        if self.actions is not None:
            self.actions.start_help()


    def start_emergency(self):

        if self.actions is not None:
            self.actions.start_emergency()

    def update_preview(self, path):
        pass    

    def on_new_frame(self, frame):

        
        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        media = self.guardian.engine.media

        frame = media.video.renderer.render(
            frame,
            protocol=media.protocol,
            event_id=media.event_id,
            started_at=media.started_at,
        )

        image = Image.fromarray(frame)

        frame_w = self.camera_frame.winfo_width()
        frame_h = self.camera_frame.winfo_height()

        if frame_w < 10:
            frame_w = 1600

        if frame_h < 10:
            frame_h = 900

        img_w, img_h = image.size

        scale = min(frame_w / img_w, frame_h / img_h)

        new_w = int(img_w * scale)
        new_h = int(img_h * scale)

        image = image.resize((new_w, new_h), Image.LANCZOS)

        photo = ImageTk.PhotoImage(image)

        def update():

            self.camera_label.configure(
                image=photo,
                text=""
            )

            self.camera_label.image = photo

        self.root.after(
            0,
            update
        )

    def run(self):

        self.root.mainloop()