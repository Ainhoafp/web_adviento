import reflex as rx
from web_adviento.styles.styles import Size, Color, TextColor
import web_adviento.styles.styles as styles


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="/gift_pixel.png",
                alt="Imagen de regalo",
                width="4em",
                height="4em"
            ),
             rx.el.span(
                    "¡Un regalo para la ",
                    rx.el.span(
                        "MEJOR",
                        color=TextColor.TERTIARY.value,
                        font_size=Size.DEFAULT.value
                    ),
                    " personita del universo!"
                ),
            rx.spacer(),
            align="center",
            width="100%"
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )