from datetime import datetime

from app.graphics.video_overlay import VideoOverlay
from app.graphics.overlay_context import OverlayContext


class FrameRenderer:

    def __init__(self):

        self.overlay = VideoOverlay()

        self.context = OverlayContext()

    def render(
        self,
        frame,
        protocol="PRONTO",
        event_id="",
        started_at=None,
    ):

        if frame is None:
            return None

        if started_at is None:
            started_at = datetime.now()

        now = datetime.now()

        self.context.protocol = protocol
        self.context.event_id = event_id
        self.context.started_at = started_at
        self.context.now = now
        self.context.elapsed_seconds = int(
            (now - started_at).total_seconds()
        )

        return self.overlay.draw(
            frame.copy(),
            self.context
        )