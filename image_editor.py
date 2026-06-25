from PIL import Image, ImageFilter

img = Image.open("qr_github.png")
print(f"Исходный размер: {img.size}")

# Уменьшить в 2 раза
new_size = (img.width // 2, img.height // 2)
small = img.resize(new_size)
small.save("qr_small.png")
print(f"Новый размер: {small.size}")

rotated = img.rotate(45, expand = True)   # поворот на 45°
rotated.save("qr_rotated.png")

flipped = img.transpose(Image.FLIP_LEFT_RIGHT)  # отразить по горизонтали
flipped.save("qr_flipped.png")

bw = img.convert("L")              # ч/б
bw.save("qr_bw.png")

blurred = img.filter(ImageFilter.BLUR)  # размытие
blurred.save("qr_blurred.png")