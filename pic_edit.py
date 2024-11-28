from PIL import Image, ImageFilter

# Функция изменения размера изображения
def resize_image(image_path, width, height):
    try:
        image = Image.open(image_path)
        resized_image = image.resize((width, height))
        return resized_image
    except Exception as e:
        print(f"Ошибка при изменении размера изображения: {e}")
        return None

# Функция конвертации в черно-белое
def convert_to_grayscale(image_path):
    try:
        image = Image.open(image_path)
        grayscale_image = image.convert("L")
        return grayscale_image
    except Exception as e:
        print(f"Ошибка при конвертации изображения в черно-белое: {e}")
        return None

# Функция применения фильтра Гаусса
def apply_gaussian_blur(image_path, radius=2):
    try:
        image = Image.open(image_path)
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
        return blurred_image
    except Exception as e:
        print(f"Ошибка при применении фильтра Гаусса: {e}")
        return None

# Универсальная функция для сохранения изображения
def save_image(image, save_path):
    try:
        if image.mode == "RGBA":  # Если изображение с альфа-каналом
            image = image.convert("RGB")  # Конвертируем в RGB для совместимости
        image.save(save_path)
        print(f"Изображение сохранено: {save_path}")
    except Exception as e:
        print(f"Ошибка при сохранении изображения: {e}")

# Пример использования
file_path = "kartinka.jpg"  # Замените на путь к вашему изображению

# Изменение размера
resized = resize_image(file_path, 500, 500)  # Указываем новые размеры
if resized:
    resized.show()
    save_image(resized, "resized_kartinka.jpg")

# Конвертация в черно-белое
grayscale = convert_to_grayscale(file_path)
if grayscale:
    grayscale.show()
    save_image(grayscale, "grayscale_kartinka.jpg")

# Применение фильтра Гаусса
blurred = apply_gaussian_blur(file_path, radius=5)
if blurred:
    blurred.show()
    save_image(blurred, "blurred_kartinka.jpg")
