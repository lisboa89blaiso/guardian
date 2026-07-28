from app.media.webcam import WebcamService
from app.ui.main_window import MainWindow


class Guardian:

    def __init__(self):

        self.webcam = WebcamService()

        self.ui = MainWindow(
            webcam=self.webcam
        )

    def start(self):

        self.webcam.start()

        self.ui.run()
