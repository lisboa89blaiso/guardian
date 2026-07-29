import cv2
from datetime import datetime

from app.graphics.overlay_context import OverlayContext


class VideoOverlay:

    TOP_HEIGHT = 42
    BOTTOM_HEIGHT = 42

    BAR_COLOR = (55, 36, 18)          # Azul escuro (BGR)
    TEXT_COLOR = (255, 255, 255)
    SECONDARY_TEXT_COLOR = (190, 190, 190)
    REC_COLOR = (0, 0, 255)

    def __init__(self):

        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def draw(self, frame, context: OverlayContext):

        if frame is None:
            return frame

        now = context.now or datetime.now()

        #
        # Barras sólidas
        #

        cv2.rectangle(
            frame,
            (0, 0),
            (frame.shape[1], self.TOP_HEIGHT),
            self.BAR_COLOR,
            -1
        )

        cv2.rectangle(
            frame,
            (0, frame.shape[0] - self.BOTTOM_HEIGHT),
            (frame.shape[1], frame.shape[0]),
            self.BAR_COLOR,
            -1
        )

        #
        # REC piscando
        #

        if now.second % 2 == 0:

            cv2.circle(
                frame,
                (22, 21),
                7,
                self.REC_COLOR,
                -1
            )

        cv2.putText(
            frame,
            "REC",
            (38, 27),
            self.font,
            0.60,
            self.TEXT_COLOR,
            2,
            cv2.LINE_AA
        )

        #
        # Guardian
        #

        cv2.putText(
            frame,
            "GUARDIAN",
            (110, 27),
            self.font,
            0.60,
            self.SECONDARY_TEXT_COLOR,
            2,
            cv2.LINE_AA
        )

        #
        # Data / Hora
        #

        datetime_text = now.strftime("%d/%m/%Y  %H:%M:%S")

        (w, _), _ = cv2.getTextSize(
            datetime_text,
            self.font,
            0.55,
            2
        )

        cv2.putText(
            frame,
            datetime_text,
            (frame.shape[1] - w - 20, 27),
            self.font,
            0.55,
            self.TEXT_COLOR,
            2,
            cv2.LINE_AA
        )

        #
        # Protocolo
        #

        protocol = context.protocol.upper()

        cv2.putText(
            frame,
            protocol,
            (20, frame.shape[0] - 14),
            self.font,
            0.70,
            self.TEXT_COLOR,
            2,
            cv2.LINE_AA
        )
        #
        # ID da ocorrência
        #
        (w, _), _ = cv2.getTextSize(
            context.event_id,
            self.font,
            0.45,
            1
        )

        cv2.putText(
            frame,
            context.event_id,
            (frame.shape[1] - w - 20, frame.shape[0] - 48),
            self.font,
            0.45,
            self.SECONDARY_TEXT_COLOR,
            1,
            cv2.LINE_AA
        )


        #
        # Cronômetro
        #

        h = context.elapsed_seconds // 3600
        m = (context.elapsed_seconds % 3600) // 60
        s = context.elapsed_seconds % 60

        timer = f"{h:02}:{m:02}:{s:02}"

        (w, _), _ = cv2.getTextSize(
            timer,
            self.font,
            0.70,
            2
        )

        cv2.putText(
            frame,
            timer,
            (frame.shape[1] - w - 20, frame.shape[0] - 14),
            self.font,
            0.70,
            self.TEXT_COLOR,
            2,
            cv2.LINE_AA
        )

        return frame