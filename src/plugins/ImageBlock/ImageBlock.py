#!/usr/bin/env python
import os
import sys
sys.path.insert(0, '...')


from reportlab.lib.units import cm

from common.PluginInterface import PluginInterface


class ImageBlock(PluginInterface):
    def __init__(self):
        pass

    def Name(self):
        return 'image'

    def prepare(self, block, context):
        pass

    def process(self, block, context):

        # filename element
        imageFilename = os.path.join(block['_path'], block['filename'])

        # caption element, default ''
        caption = self.getElemValue(block, 'caption', '')

        # width element
        width = block["width"] * \
            cm if "width" in block else context.doc.currentWidth()

        # align element
        align = self.getElemValue(block, 'align', 'CENTER').upper()

        # padding element, defaukt 10
        padding = self.getElemValue(block, 'padding', 10)

        context.appendImage(imageFilename, caption, width, align, padding)
