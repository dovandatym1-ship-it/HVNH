"""Chủ đề tím chuyển sắc"""
from pptx.dml.color import RGBColor
from themes import BaseTheme


class PurpleGradientTheme(BaseTheme):
    name = "Tím chuyển sắc"
    primary = RGBColor(123, 47, 190)
    secondary = RGBColor(224, 64, 251)
    accent = RGBColor(168, 130, 255)
    background = RGBColor(255, 255, 255)
    text = RGBColor(33, 33, 33)
    muted = RGBColor(158, 158, 158)
    dark_bg = RGBColor(30, 15, 50)
