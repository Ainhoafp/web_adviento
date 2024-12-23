import reflex as rx
import web_adviento.styles.styles as styles
from web_adviento.styles.styles import Size
from web_adviento.views.navbar import navbar
from web_adviento.views.header import header
from web_adviento.views.calendar import calendar

title = "Calendario de adviento 2024 | 24 días. 24 regalos."
description = "¡Aquí está tu calendario de adviento sorpresa amor!"

def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.script(src="/js/snow.js"),
        navbar(),
        rx.spacer(),
        rx.vstack(
            header(),
            rx.spacer(),
            calendar(),
            align="center",
            width="100%",
            spacing="8"
        )
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-Y6GDVB3FJB"),
    ],
)


app.add_page(
    index,
    title=title,
    description=description,
    image="/amor.png"
)