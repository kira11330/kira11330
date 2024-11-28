from PIL import Image

def process_image(file_path):
    # Открываем изображение
    image = Image.open(file_path)
    
    # Проверяем, является ли формат PNG и содержит ли альфа-канал
    if image.format == "PNG" and image.mode in ("RGBA", "LA"):
        # Преобразуем фон в режим RGBA
        background = Image.new("RGBA", image.size, (255, 255, 255, 255))  # Белый фон с альфа-каналом
        # Преобразуем изображение в RGBA
        image = image.convert("RGBA")
        # Накладываем изображение на фон
        image = Image.alpha_composite(background, image)
    else:
        # Если изображение не в режиме RGBA, преобразуем его в RGB
        image = image.convert("RGB")
    
    # Возвращаем обработанное изображение
    return image

# Пример использования
file_path = "kartinka.png"  # Укажите путь к вашему файлу
processed_image = process_image(file_path)

# Преобразуем изображение в RGB, если нужно, перед сохранением в формате JPEG
if processed_image.mode != "RGB":
    processed_image = processed_image.convert("RGB")

processed_image.show()  # Покажем результат
processed_image.save("obr_kartinka.jpg")  # Сохраним в новый файл
