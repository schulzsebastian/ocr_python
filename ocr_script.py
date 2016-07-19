#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io


def image_to_text(image):
    tool = pyocr.get_available_tools()[0]
    lang = tool.get_available_languages()[2]
    req_image = []
    final_text = []
    try:
        image_obj = Image(filename=image, resolution=300)
    except:
        return final_text
    if image[-4:] is not 'jpeg':
        image_obj = image_obj.convert('jpeg')
    for img in image_obj.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))
    for img in req_image:
        txt = tool.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)
    return final_text
