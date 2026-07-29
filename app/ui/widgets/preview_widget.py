import customtkinter as ctk
from PIL import Image, ImageTk


class PreviewWidget(ctk.CTkFrame):

    def __init__(
        self,
        master,
        width=640,
        height=360
    ):

        super().__init__(master)

        self.width = width
        self.height = height

        self.pack_propagate(False)

        self.label = ctk.CTkLabel(
            self,
            text="Aguardando câmera..."
        )

        self.label.pack(
            fill="both",
            expand=True
        )

        self._image = None

    def set_image(self, frame):

        image = Image.fromarray(frame)

        image = image.resize(
            (self.width, self.height)
        )

        self._image = ImageTk.PhotoImage(image)

        self.label.configure(
            image=self._image,
            text=""
        )

    def clear(self):

        self.label.configure(
            image=None,
            text="Aguardando câmera..."
        )

        self._image = None