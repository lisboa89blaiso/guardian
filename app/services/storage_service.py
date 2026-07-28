from pathlib import Path
from datetime import datetime
import json


class StorageService:

    def __init__(self):

        self.base = Path("guardian_data")

        self.base.mkdir(exist_ok=True)

        self.log_file = self.base / "events.json"

    def save_event(self, level, message):

        event = {
            "time": datetime.now().isoformat(),
            "level": level,
            "message": message
        }

        data = []

        if self.log_file.exists():

            try:

                with open(self.log_file, "r", encoding="utf8") as f:

                    data = json.load(f)

            except:

                data = []

        data.append(event)

        with open(self.log_file, "w", encoding="utf8") as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )