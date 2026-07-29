import time


class SessionController:

    def __init__(self):

        self.protocol = None
        self.event_id = None

        self.recording = False

        self.started_at = None

        self.listeners = []

    #
    # Listeners
    #

    def add_listener(self, listener):

        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_listener(self, listener):

        if listener in self.listeners:
            self.listeners.remove(listener)

    def notify(self):

        for listener in self.listeners:

            try:
                listener.on_session_changed(self)

            except Exception:
                pass

    #
    # Session
    #

    def start(self, protocol, event_id):

        self.protocol = protocol
        self.event_id = event_id

        self.started_at = time.time()

        self.recording = True

        self.notify()

    def finish(self):

        self.protocol = None
        self.event_id = None

        self.started_at = None

        self.recording = False

        self.notify()

    @property
    def elapsed(self):

        if self.started_at is None:
            return 0

        return int(time.time() - self.started_at)