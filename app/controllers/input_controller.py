import keyboard


class InputController:

    def __init__(self, guardian):

        self.guardian = guardian

    def start(self):

        keyboard.add_hotkey(
            "ctrl+shift+q",
            self.guardian.toggle_panel
        )

        keyboard.add_hotkey(
            "ctrl+shift+y",
            self.guardian.toggle_main_window
        )

        keyboard.add_hotkey(
            "ctrl+shift+e",
            self.guardian.engine.conversar
        )

        keyboard.add_hotkey(
            "ctrl+shift+(",
            self.guardian.engine.ligar_papai
        )

        keyboard.add_hotkey(
            "ctrl+shift+r",
            self.guardian.engine.ajuda
        )

        keyboard.add_hotkey(
            "ctrl+shift+*",
            self.guardian.engine.emergencia
        )

        keyboard.add_hotkey(
            "ctrl+shift+f12",
            self.guardian.engine.finish_protocol
        )