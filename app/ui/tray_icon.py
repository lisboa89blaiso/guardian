import threading

from PIL import Image, ImageDraw
import pystray


class TrayIcon:

    def __init__(self):

        self.icon = None

        self.on_open = None
        self.on_exit = None

    def start(self):

        image = self._create_icon()

        menu = pystray.Menu(

            pystray.MenuItem(
                "Abrir Guardian",
                self._open
            ),

            pystray.Menu.SEPARATOR,

            pystray.MenuItem(
                "Sair",
                self._exit
            )
        )

        self.icon = pystray.Icon(
            "Guardian",
            image,
            "Guardian",
            menu
        )

        threading.Thread(
            target=self.icon.run,
            daemon=True
        ).start()

    def stop(self):

        if self.icon:
            self.icon.stop()

    def _open(self):

        if self.on_open:
            self.on_open()

    def _exit(self):

        if self.on_exit:
            self.on_exit()

    def _create_icon(self):

        image = Image.new(
            "RGB",
            (64, 64),
            (15, 39, 68)
        )

        draw = ImageDraw.Draw(image)

        draw.ellipse(
            (16, 16, 48, 48),
            fill=(255, 255, 255)
        )

        draw.rectangle(
            (28, 22, 36, 44),
            fill=(15, 39, 68)
        )

        draw.rectangle(
            (24, 28, 40, 36),
            fill=(15, 39, 68)
        )

        return image