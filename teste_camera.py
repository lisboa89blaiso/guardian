import cv2

for indice in range(6):

    print(f"\nTestando câmera {indice}...")

    cap = cv2.VideoCapture(indice, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Não abriu.")
        continue

    ok, frame = cap.read()

    if not ok:
        print("Abriu, mas não retornou imagem.")
        cap.release()
        continue

    print("Imagem recebida! Pressione ESC para próxima câmera.")

    while True:

        ok, frame = cap.read()

        if not ok:
            break

        cv2.imshow(f"Camera {indice}", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

print("\nFim.")