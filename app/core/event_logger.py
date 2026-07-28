from datetime import datetime

from app.services.storage_service import StorageService


class EventLogger:

    def __init__(self, sidebar):

        self.sidebar = sidebar

        self.storage = StorageService()

        self.history = []

    def log(self, level, message):

        event = {

            "time": datetime.now(),

            "level": level,

            "message": message

        }

        self.history.append(event)

        self.storage.save_event(
            level,
            message
        )

        self.sidebar.add_event(
            f"{level} {message}"
        )

    def info(self, message):

        self.log(
            "ℹ️",
            message
        )

    def warning(self, message):

        self.log(
            "🟡",
            message
        )

    def critical(self, message):

        self.log(
            "🔴",
            message
        )