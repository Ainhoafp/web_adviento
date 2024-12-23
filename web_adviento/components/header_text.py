import reflex as rx
from web_adviento.styles.styles import Size, TextColor

def header_text(icon: str, text: str, dark=True) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.image(src=icon)
        ),
        rx.heading(
            text,
            size="5",
            style={
                "color": TextColor.ACCENT.value if dark else TextColor.SECONDARY.value
            }
        ),
        spacing="4",
        style={
            "padding_bottom": "1em",
        },
        align="center"
    )