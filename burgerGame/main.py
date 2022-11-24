from PIL import Image, ImageDraw, ImageFont
import time
import random
import cv2 as cv
import numpy as np
from colorsys import hsv_to_rgb
from Enemy import Enemy
from Get import Get
from Ingredient import Ingredient
from Character import Character
from Joystick import Joystick

def main():
    joystick = Joystick()
    

