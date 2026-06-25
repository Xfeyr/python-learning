class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def info(self):
        return f"Файл {self.name}: {self.size} Б"
        
class ImageFile(File):
    def __init__(self, name, size, width, height):
        super().__init__(name, size)
        self.width = width
        self.height = height
    
    def info(self):
        return f"Изображение {self.name}: {self.size} Б, {self.width}x{self.height}px"
        
class TextFile(File):
    def __init__(self, name, size, encoding = 'utf-8'):
        super().__init__(name, size)
        self.encoding = encoding
    
    def info(self):
        return f"Текстовый файл {self.name}: {self.size} Б, кодировка {self.encoding}"
        
files = [
    File("archive.zip", 1024000),
    ImageFile("photo.jpg", 204800, 1920, 1080),
    TextFile("readme.txt", 4096),
    TextFile("config.ini", 2048, encoding = "cp1251"),
]

for f in files:
    print(f.info())