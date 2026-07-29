from dataclasses import dataclass
from datetime import datetime


@dataclass
class OverlayContext:

    event_id: str = ""
    
    protocol: str = ""

    recording: bool = False

    started_at: datetime | None = None

    now: datetime | None = None

    elapsed_seconds: int = 0