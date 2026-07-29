from app.media.webcam import WebcamService
from app.media.screenshot import ScreenshotService

from app.ui.guardian_ui import GuardianUI
from app.ui.window_mode import WindowMode

from app.controllers.input_controller import InputController
from app.core.guardian_engine import GuardianEngine


class Guardian:

    def __init__(self):

        self.webcam = WebcamService()

        self.screenshot = ScreenshotService()

        self.ui = GuardianUI(
            self.webcam,
            mode=WindowMode.DEVELOPMENT
        )

        self.engine = GuardianEngine(
            window=self.ui,
            webcam=self.webcam,
            screenshot=self.screenshot
        )

        self.ui.bind_guardian(self)

        self.input = InputController(
            guardian=self
        )

    def start(self):

        self.webcam.start()

        self.input.start()

        self.ui.run()

        self.webcam.stop()

    def toggle_panel(self):

        self.ui.toggle_panel()

    def toggle_main_window(self):

        self.ui.toggle_main_window()