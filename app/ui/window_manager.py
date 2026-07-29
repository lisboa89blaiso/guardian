class WindowManager:

    def __init__(self):

        self._windows = {}

    def register(self, name, window):

        self._windows[name] = window

    def get(self, name):

        return self._windows.get(name)

    def exists(self, name):

        return name in self._windows

    def all(self):

        return self._windows.values()

    def destroy_all(self):

        for window in self._windows.values():

            try:
                window.root.destroy()
            except Exception:
                pass

    def register_main(self, window):

        self.register(
            "main",
            window
        )

    def main(self):

        return self.get("main")