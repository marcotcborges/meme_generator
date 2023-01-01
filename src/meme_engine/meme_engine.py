from PIL import Image, ImageFont, ImageDraw
import random


class MemeEngine:
    """Class to generate actual meme file."""

    def __init__(self, path):
        """Initiate meme engine with path where store produced meme files."""
        self.temp_dir = path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate Meme with given img, text, and author."""
        out_path = f"{self.temp_dir}/{random.randint(0,1000000)}.png"

        if width >= 500:
            width = 500
        try:
            with Image.open(img_path) as img:
                ratio = img.height / img.width
                height = width * ratio
                img = img.resize((int(width), int(height)))
                font_size = int(img.height/20)
                font = ImageFont.truetype("arial.ttf", 15)

                d = ImageDraw.Draw(img)

                x_loc = random.randint(0, int(img.width/4))
                y_loc = random.randint(0, int(img.height-font_size*2))

                d.text((x_loc, y_loc), text, fill=(0, 0, 0), font=font)
                d.text((int(x_loc*1.2), y_loc+font_size), " - " + author, font=font)
                img.save(out_path)
                
        except Exception as e:
            print(f'make_meme error: {e}')

        return out_path