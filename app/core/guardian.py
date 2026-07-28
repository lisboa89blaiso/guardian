from app.media.webcam import WebcamService
from app.media.screenshot import ScreenshotService

from app.ui.main_window import MainWindow

from app.controllers.input_controller import InputController
from app.core.guardian_engine import GuardianEngine


class Guardian:

    def __init__(self):

        self.webcam = WebcamService()

        self.screenshot = ScreenshotService()

        self.window = MainWindow(
            webcam=self.webcam
        )

        self.engine = GuardianEngine(
            window=self.window,
            webcam=self.webcam,
            screenshot=self.screenshot
        )

        self.window.bind_guardian(
            self.engine
        )

        self.input = InputController(
            engine=self.engine
        )

    def start(self):

        self.webcam.start()

        self.input.start()

        self.window.run()

        self.webcam.stop()