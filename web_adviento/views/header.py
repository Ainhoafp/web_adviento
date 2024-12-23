import reflex as rx
import web_adviento.styles.styles as styles
from web_adviento.styles.styles import Size, TextColor
from web_adviento.components.button import button

class State(rx.State):
    playing: bool = False
    
    @rx.event
    def play_audio(self):
        self.playing = not self.playing

def audio_player():
    return rx.audio(
        url="/santa.mp3",
        playing=State.playing,
        controls=True,
        width="0px",
        height="0px"
    )

def header() -> rx.Component:
    return rx.vstack(
        audio_player(),
        rx.spacer(),  # Add spacer between components
        rx.spacer(),
        rx.flex(
            rx.heading(
                "¡Feliz navidad!",
                size="8",
                padding_bottom=Size.DEFAULT.value
            ),
            width="100%",
            align="center",
            justify="center"
        ),
        rx.spacer(),  # Add spacer
        rx.spacer(),
        rx.flex(
            rx.image(
                src="/amor.png",
                alt="Imagen amor estilo navideño.",
                width="20em",
                height="20em",
                margin_right=Size.BIG.value,
                on_click=State.play_audio
            ),
            rx.spacer(),  # Add spacer
            rx.vstack(
                rx.box(
                    rx.text("24 días. 24 regalos."),
                    rx.spacer(),  # Add spacer
                    rx.text("Del 20 de diciembre al 12 de enero."),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.spacer(),  # Add spacer
                rx.el.span(
                    "¡Aquí está tu calendario de adviento sorpresa ",
                    rx.el.span(
                        "AMORCITO",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    ),
                    "!"
                ),
                rx.el.span(
                    "Cada día de este més tendras una actividad nueva para hacer."
                ),
                rx.el.span(
                    "Espero que te guste muchísimo jejeje. (Pd: haz click en la imagen)"
                ),
                align_items="start",
                spacing="4"  # Add spacing between vstack items
            ),
            flex_direction=styles.FLEX_DIRECTION,
            spacing="5",  # Add spacing between flex items
            align="center",  # Centers items vertically
            justify="center"
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style,
        spacing="4"  # Add spacing between vstack items
    )