import keyboard


class InputController:

    def __init__(self, engine):

        self.engine = engine

    def start(self):

        keyboard.add_hotkey(
            "ctrl+shift+e",
            self.engine.conversar
        )

        keyboard.add_hotkey(
            "ctrl+shift+(",
            self.engine.ligar_papai
        )

        keyboard.add_hotkey(
            "ctrl+shift+r",
            self.engine.ajuda
        )

        keyboard.add_hotkey(
            "ctrl+shift+*",
            self.engine.emergencia
        )

        keyboard.add_hotkey(
            "ctrl+shift+f12",
            self.engine.finish_protocol
        )