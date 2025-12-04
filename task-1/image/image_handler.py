import os
from .image_processor import ImageProcessor
from PIL import Image
from datetime import datetime

class ImageHandler:
    
    def __init__(self, path):
        self.path = path
        self.image = None
        self.format = None
        
    def load(self):
        try:
            with Image.open(self.path) as img:
                self.image = img.copy()
                self.format = img.format
        except FileNotFoundError:
            raise ValueError("File not found: " + self.path)
        except Exception as e:
            raise ValueError("Could not load image: " + str(e))
        
    def save(self, path, filename):
        if self.image is None:
            raise ValueError("Image not loaded")
        
        out_dir = os.path.dirname(path) or '.'
        os.makedirs(out_dir, exist_ok=True)
        
        name = filename + datetime.now().strftime("%d%m%Y") + ".jpg"
        
        path = os.path.abspath(os.path.join(path, name))
        print(path)
        self.image.save(path, self.format)
        
    def reformat(self, format):
        self.format = format
        
    def resize(self):
        width = self.image.size[0] / 2
        height = self.image.size[1] / 2
        
        self.image.thumbnail((width, height), Image.Resampling.LANCZOS) 
        
    def get_processor(self):
        if self.image is None:
            raise ValueError("Image not loaded")
        
        return ImageProcessor(self.image)
         