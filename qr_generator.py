import qrcode

# Задание 1: GitHub
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data("https://github.com/Xfeyr")
qr.make(fit=True)
img = qr.make_image(fill_color = "black", back_color = "white")
img.save("qr_github.png")
print("qr_github.png сохранён")

# Задание 2: Текст маме
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data("Привет, мама! Я сделал это на Python!")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_mom.png")
print("qr_mom.png сохранён")

# Задание 3: Цветной
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data("😒")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="yellow")
img.save("qr_color.png")
print("qr_color.png сохранён")

# Задание 4: Большой размер
qr = qrcode.QRCode(version=1, box_size=20, border=2)
qr.add_data("https://github.com/Xfeyr")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_big.png")
print("qr_big.png сохранён")