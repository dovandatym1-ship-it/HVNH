"""Chủ đề xanh đại dương"""
from pptx.dml.color import RGBColor
from themes import BaseTheme


class OceanBlueTheme(BaseTheme):
    name = "Xanh đại dương"
    primary = RGBColor(0, 119, 182)
    secondary = RGBColor(0, 180, 216)
    accent = RGBColor(144, 224, 239)
    background = RGBColor(255, 255, 255)
    text = RGBColor(33, 33, 33)
    muted = RGBColor(158, 158, 158)
    dark_bg = RGBColor(8, 30, 52)
