"""Load an image file, reformat it and add a Quote."""

import os
import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Define toolset to generate a Meme and save it to disk."""

    def __init__(self, output_dir: str):
        """Initialize Meme Engine."""
        self.output_dir = output_dir

    def wrap(self, text):
        """Reformat the text so it will fit the picture."""
        if len(text) < 28:
            return text
        else:
            for i in range(16, len(text)):
                if text[i] == " ":
                    first_half = text[:i]
                    second_half = text[i+1:]
                    text = first_half + "\n" + self.wrap(second_half)
                    break
            return text

    def make_meme(self,
                  img_path: str,
                  text: str,
                  author: str,
                  width: int = 500
                  ) -> str:  # generated image path
        """Create a Meme from a picture and a Quote.

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the body of a quote.
            author {str} -- the author of a quote.
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output image.
        """
        # Resizing the image if it is over 500px wide
        im = Image.open(img_path)
        if im.width > width:
            resize_factor = width / im.width
            im = im.resize(
                (int(im.width * resize_factor),
                 int(im.height * resize_factor)))

        # combine text and author
        text = text + " -" + author

        # make a blank image for the text, init to transparent text color
        txt = Image.new("RGBA", im.size, (0, 0, 0, 0))
        fnt = ImageFont.truetype("./_fonts/LilitaOne-Regular.ttf", 38)
        d = ImageDraw.Draw(txt, mode="RGBA")

        # Preprocessing of msg to fit in the picture
        text = self.wrap(text)

        # generate random position
        if len(text) < 28:
            height_wiggle = random.randint(0, im.height - 40)
        elif len(text) < 50:
            height_wiggle = random.randint(0, im.height - 100)
        else:
            height_wiggle = random.randint(0, 40)

        lr_wiggle = random.randint(int(im.width/2) - 10, int(im.width/2) + 10)

        # Plotting the text to random position
        d.text(
            (lr_wiggle, height_wiggle),
            text,
            font=fnt,
            fill=(255, 255, 255, 255),
            align="center",
            anchor="ma")

        # composing the Meme out of picture and text
        im = im.convert("RGBA")
        final = Image.alpha_composite(im, txt)
        out = final.convert("RGB")

        # generate out path
        meme_name = f"{random.randint(0,10000000000)}.jpg"
        out_path = os.path.join(self.output_dir, meme_name)
        out.save(out_path)
        return out_path
