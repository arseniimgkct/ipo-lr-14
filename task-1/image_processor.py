from PIL import Image, ImageDraw, ImageFont, ImageFilter

class ImageProcessor():
    def __init__(self, image):
        if not isinstance(image, Image.Image):
            raise TypeError
        self.img = image

    def filter_emboss(self):
        self.img = self.img.filter(ImageFilter.EMBOSS)
    
    def watermark(self):
        base = self.img.convert("RGBA")

        txt_layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(txt_layer)

        text = "Вариант 5"
        font = ImageFont.truetype("arial.ttf", 20)

        color = (255, 255, 255, 120)

        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]

        bw, bh = base.size
        pos = (bw - w - 10, bh - h - 10)

        draw.text(pos, text, font=font, fill=color)

        self.img = Image.alpha_composite(base, txt_layer).convert("RGB")

        