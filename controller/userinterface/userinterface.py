#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys
import time
import logging
import spidev as SPI
from .lib import LCD_1inch14
from PIL import Image,ImageDraw,ImageFont
from random import randint

# Raspberry Pi pin configuration:
logging.basicConfig(level=logging.DEBUG)
REFRESH_RATE = 30

Font2 = ImageFont.truetype("userinterface/Font/Font00.ttf",25)

class User_Interface:

    def __init__(self):
        self.disp = LCD_1inch14.LCD_1inch14()
        self.disp.Init()
        self.disp.clear()

    def prepareFrame(self):
        self.frame = Image.new("RGB", (self.disp.width, self.disp.height), "WHITE")
        self.draw = ImageDraw.Draw(self.frame)

    def renderFrame(self):
        self.disp.ShowImage(self.frame)

    def addText(self, pos_to_render: tuple, text_to_display: str):
        self.draw.text(pos_to_render, text_to_display, font = Font2, fill = "BLACK")

    def setupDisplay(self, text_to_display: str):
        self.prepareFrame()
        self.addText((1, 45), text_to_display)
        self.renderFrame()
        time.sleep(2)

    def printDataToDisplay(self, list_of_text: list):
        self.prepareFrame()
        for element in list_of_text:
            self.addText(element[0], element[1])

        self.renderFrame()

    def __del__(self):
        self.disp.module_exit()

'''
    logging.info("draw point")   
    draw.rectangle((1,1,2,2), fill = "BLACK")
    draw.rectangle((1,7,3,10), fill = "BLACK")
    draw.rectangle((1,13,4,17), fill = "BLACK")
    draw.rectangle((1,19,5,24), fill = "BLACK")

    logging.info("draw line")
    draw.line([(20, 1),(50, 31)], fill = "RED",width = 1)
    draw.line([(50, 1),(20, 31)], fill = "RED",width = 1)
    draw.line([(90,17),(122,17)], fill = "RED",width = 1)
    draw.line([(106,1),(106,33)], fill = "RED",width = 1)

    logging.info("draw rectangle")
    draw.rectangle([(20,1),(50,31)],fill = "WHITE",outline="BLUE")
    draw.rectangle([(55,1),(85,31)],fill = "BLUE")

    logging.info("draw circle")
    draw.arc((90,1,122,33),0, 360, fill =(0,255,0))
    draw.ellipse((125,1,158,33), fill = (0,255,0))
'''
