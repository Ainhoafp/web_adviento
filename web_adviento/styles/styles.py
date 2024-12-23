import reflex as rx
from enum import Enum
from .font import Font
from .colors import Color, TextColor

MAX_WIDTH = "1000px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]


class Size(Enum):
    ZERO = "0px"
    SMALL = "1"
    MEDIUM = "2"
    DEFAULT = "3"
    BIG = "4"
    BUTTON = "5"
    VERY_BIG = "6"


STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.heading: {
        "font_family": Font.DEFAULT.value,
        "color": TextColor.ACCENT.value
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none"
        }
    },
    rx.el.span: {
        "font_size": Size.MEDIUM.value
    },
    rx.button: {
        "margin_bottom": Size.DEFAULT.value,
        "height": Size.BUTTON.value,
        "color": f"{TextColor.SECONDARY.value} !important",
        "_hover": {
            "color": f"{TextColor.PRIMARY.value} !important"
        }
    }
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)