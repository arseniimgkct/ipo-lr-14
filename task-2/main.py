import os
from image import ImageHandler, ImageProcessor

if __name__ == "__main__":
    filename = input("Введите название картинки из data/source: ")
    current_path = os.getcwd()
    src_path = os.path.join(current_path, "data", "source", filename)

    print("Путь к файлу:", src_path)
    print("Существует ли файл:", os.path.exists(src_path))

    handler = ImageHandler(src_path)

    handler.load()
    print("Формат:", handler.format)
    print("Размер до обработки:", handler.image.size)

    handler.resize()
    print("Размер после resize:", handler.image.size)

    processor = handler.get_processor()

    processor.filter_emboss()

    processor.watermark()

    handler.image = processor.img

    out_dir = os.path.join(current_path, "data", "changed")
    handler.save(out_dir, filename)

    print("Готово!")
