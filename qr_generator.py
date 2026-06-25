import cv2

# Читаем изображение
img = cv2.imread("my_qr.png")

# Декодируем QR-код
detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(img)

if data:
    print(f"Содержимое QR-кода: {data}")
else:
    print("QR-код не найден")