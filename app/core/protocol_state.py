from enum import Enum
from datetime import datetime


class ProtocolStatus(Enum):

    IDLE = "IDLE"

    HELP = "AJUDA"

    EMERGENCY = "EMERGÊNCIA"


class ProtocolState:

    def __init__(self):

        self.status = ProtocolStatus.IDLE

        self.active = False

        self.started_at = None

    def start(self, status):

        self.status = status

        self.active = True

        self.started_at = datetime.now()

    def finish(self):

        self.status = ProtocolStatus.IDLE

        self.active = False

        self.started_at = None