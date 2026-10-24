"""Chủ đề công nghệ xanh dương"""
from pptx.dml.color import RGBColor
from themes import BaseTheme


class BlueTechnologyTheme(BaseTheme):
    name = "Công nghệ xanh dương"
    primary = RGBColor(0, 102, 204)
    secondary = RGBColor(0, 204, 153)
    accent = RGBColor(0, 180, 216)
    background = RGBColor(255, 255, 255)
    text = RGBColor(33, 33, 33)
    muted = RGBColor(158, 158, 158)
    dark_bg = RGBColor(10, 25, 49)
