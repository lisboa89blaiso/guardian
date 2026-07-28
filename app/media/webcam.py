import cv2
import threading
import time


class WebcamService:

    def __init__(self, camera_index=4):

        self.camera_index = camera_index

        self.cap = None
        self.frame = None

        self.running = False

        self.thread = None

    def start(self):

        # Tenta abrir a câmera configurada
        self.cap = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)

        if not self.cap.isOpened():

            # Fallback usando backend padrão
            self.cap.release()
            self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            raise RuntimeError(
                f"Não foi possível abrir a câmera {self.camera_index}"
            )

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        self.running = True

        self.thread = threading.Thread(
            target=self._update,
            daemon=True
        )

        self.thread.start()

    def _update(self):

        while self.running:

            if self.cap is None:
                break

            ok, frame = self.cap.read()

            if ok:
                self.frame = frame

            time.sleep(0.01)

    def get_frame(self):

        return self.frame

    def stop(self):

        self.running = False

        if self.thread is not None:
            self.thread.join(timeout=1)

        if self.cap is not None:
            self.cap.release()
            self.cap = None