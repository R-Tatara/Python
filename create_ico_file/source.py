# -*- coding: utf-8 -*-
import os
from PIL import Image


def main():
    img_path = "C:/Users/rabum/PycharmProjects/create_ico_file/sample.png"
    img = Image.open(img_path, "r")

    if img.format != "PNG":
        print("Image format should be PNG")
        return -1

    if img.width != img.height:
        if img.width > img.height:
            longside = img.width
        elif img.width < img.height:
            longside = img.height

        # Make transparent background
        new_img = Image.new(img.mode, (longside, longside), (255, 255, 255, 0))

        # Combine original image and background
        offset_width = int(round(((longside - img.width) / 2), 0))
        offset_height = int(round(((longside - img.height) / 2), 0))
        new_img.paste(img, (offset_width, offset_height))
        new_img.show()
    else:
        new_img = img

    # Save image file
    base_name = os.path.splitext(img_path)[0]
    save_path = base_name + ".ico"
    new_img.save(save_path)
    return


if __name__ == "__main__":
    main()
