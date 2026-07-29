from abc import ABC
from abc import abstractmethod


class FrameListener(ABC):

    @abstractmethod
    def on_new_frame(self, frame):
        pass