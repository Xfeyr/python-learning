import cv2
import os

# Список всех QR-кодов
files = ["qr_github.png", "qr_mom.png", "qr_color.png", "qr_big.png"]

detector = cv2.QRCodeDetector()

for file in files:
    if os.path.exists(file):
        img = cv2.imread(file)
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            print(f"{file}: {data}")
        else:
            print(f"{file}: QR-код не найден")
    else:
        print(f"{file}: файл не существует")