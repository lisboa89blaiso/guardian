from dotenv import load_dotenv
from pathlib import Path

import os
import requests

ROOT = Path(__file__).resolve().parents[3]
load_dotenv(ROOT / ".env")


class DiscordService:

    def __init__(self):
        self.webhook = os.getenv("DISCORD_WEBHOOK")

    def send_message(self, message: str):

        if not self.webhook:
            raise RuntimeError("DISCORD_WEBHOOK não configurado.")

        response = requests.post(
            self.webhook,
            json={
                "content": message
            },
            timeout=10
        )

        response.raise_for_status()

    def send_video(self, video_path: str, message="🆘 Pedido de ajuda"):

        if not self.webhook:
            raise RuntimeError("DISCORD_WEBHOOK não configurado.")

        with open(video_path, "rb") as video:

            response = requests.post(
                self.webhook,
                data={
                    "content": message
                },
                files={
                    "file": video
                },
                timeout=120
            )

        response.raise_for_status()

    def send_image(self, image_path: str, message="🚨 Emergência detectada"):

        if not self.webhook:
            raise RuntimeError("DISCORD_WEBHOOK não configurado.")

        with open(image_path, "rb") as image:

            response = requests.post(
                self.webhook,
                data={
                    "content": message
                },
                files={
                    "file": image
                },
                timeout=60
            )

        response.raise_for_status()