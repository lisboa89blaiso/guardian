import cv2

print("Procurando câmeras...\n")

for i in range(10):

    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)

    if cap.isOpened():

        ok, frame = cap.read()

        if ok:
            print(f"Câmera encontrada no índice {i}")
        else:
            print(f"Índice {i} abriu mas não retornou imagem")

        cap.release()