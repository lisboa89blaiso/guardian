from app.protocols.help_protocol import HelpProtocol
from app.protocols.emergency_protocol import EmergencyProtocol


class ProtocolEngine:

    def __init__(self, guardian):

        self.guardian = guardian

    def execute(self, protocol):

        protocols = {

            "help": HelpProtocol,

            "emergency": EmergencyProtocol

        }

        if protocol not in protocols:

            return

        protocols[protocol](

            self.guardian

        ).execute()