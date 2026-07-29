from app.ui.tray_icon import TrayIcon


class TrayController:

    def __init__(self, window):

        self.window = window

        self.tray = TrayIcon()

        self.tray.on_open = self.show
        self.tray.on_exit = self.exit

        self.window.root.protocol(
            "WM_DELETE_WINDOW",
            self.hide
        )

    def start(self):

        self.tray.start()

    def stop(self):

        self.tray.stop()

    def show(self):

        self.window.root.after(
            0,
            self.window.root.deiconify
        )

        self.window.root.after(
            0,
            self.window.root.lift
        )

        self.window.root.after(
            0,
            self.window.root.focus_force
        )

    def hide(self):

        self.window.root.after(
            0,
            self.window.root.withdraw
        )

    def exit(self):

        self.stop()

        self.window.root.after(
            0,
            self.window.root.destroy
        )