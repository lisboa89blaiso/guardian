import customtkinter as ctk
import cv2

from PIL import Image
from PIL import ImageTk

from app.ui.sidebar import Sidebar
from app.ui.status_panel import StatusPanel


class MainWindow:

    def __init__(self, webcam):

        self.webcam = webcam

        self.guardian = None

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("Guardian")

        self.root.geometry("1700x920")

        self.root.grid_columnconfigure(1, weight=1)

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=0)

        self.sidebar = Sidebar(self.root)

        self.sidebar.grid(
            row=0,
            column=0,
            rowspan=3,
            sticky="ns"
        )

        self.status_panel = None

        self.camera_frame = ctk.CTkFrame(self.root)

        self.camera_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=20,
            pady=(10, 10)
        )

        self.camera_label = ctk.CTkLabel(
            self.camera_frame,
            text=""
        )

        self.camera_label.pack(
            expand=True,
            fill="both"
        )

        self.bottom = ctk.CTkFrame(self.root)

        self.bottom.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=20,
            pady=(0, 20)
        )

        self.bottom.grid_columnconfigure(0, weight=1)
        self.bottom.grid_columnconfigure(1, weight=2)

        self.preview = ctk.CTkLabel(
            self.bottom,
            text="Última captura"
        )

        self.preview.grid(
            row=0,
            column=0,
            padx=20,
            pady=20
        )

        self.info = ctk.CTkTextbox(
            self.bottom,
            height=180
        )

        self.info.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

        self.info.insert(
            "end",
            "Guardian Online\n"
        )

        self.update_camera()

    def bind_guardian(self, guardian):

        self.guardian = guardian

        self.status_panel = StatusPanel(
            self.root,
            guardian
        )

        self.status_panel.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=20,
            pady=(20, 5)
        )

    def update_preview(self, path):

        image = Image.open(path)

        image.thumbnail((300, 180))

        photo = ImageTk.PhotoImage(image)

        self.preview.configure(
            image=photo,
            text=""
        )

        self.preview.image = photo

    def update_camera(self):

        frame = self.webcam.get_frame()

        if frame is not None:

            frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            image = Image.fromarray(frame)

            image.thumbnail((1300, 700))

            photo = ImageTk.PhotoImage(image)

            self.camera_label.configure(
                image=photo
            )

            self.camera_label.image = photo

        self.root.after(
            15,
            self.update_camera
        )

    def run(self):

        self.root.mainloop()