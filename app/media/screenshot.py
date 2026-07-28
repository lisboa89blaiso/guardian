import os
from datetime import datetime
import cv2


class ScreenshotService:

    def __init__(self):

        os.makedirs("screenshots", exist_ok=True)

    def save(self, frame):

        if frame is None:
            return None

        filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")

        path = os.path.join(
            "screenshots",
            filename
        )

        cv2.imwrite(path, frame)

        return path