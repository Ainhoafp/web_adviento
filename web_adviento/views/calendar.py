import reflex as rx
import web_adviento.styles.styles as styles
from web_adviento.styles.styles import Size, TextColor
from datetime import datetime
from web_adviento.components.button import button
from web_adviento.components.header_text import header_text

# Define the list of gift images
gift = [
    "/1.png",
    "/2.png", 
    "/3.png",
    "/4.png",
    "/5.png",
    "/6.png",
    "/7.png",
    "/8.png", 
    "/9.png",
    "/10.png",
    "/11.png",
    "/12.png",
    "/13.png",
    "/14.png",
    "/15.png",
    "/16.png",
    "/17.png",
    "/18.png",
    "/19.png",
    "/20.png",
    "/21.png",
    "/22.png",
    "/23.png",
    "/24.png",
]

class AdventState(rx.State):
    """The advent calendar state."""
    days: list[int] = list(range(1, 25))
    modal_image: str = ""
    modal_open: bool = False

    def _calculate_current_day(self, today: datetime) -> int:
        """Calculate the current day number based on the date."""
        if today.month == 12:
            return today.day - 19  # Days since Dec 20
        elif today.month == 1:
            return today.day + 12  # Days in December (31-19) + days in January
        return 0

    @rx.event
    def check_and_open(self, day: int):
        """Check if day is available and update modal image."""
        today = datetime.now()
        
        # Check if we're in the valid date range (Dec 20 - Jan 12)
        if (today.month == 12 and today.day >= 20) or \
           (today.month == 1 and today.day <= 12):
            
            current_day = self._calculate_current_day(today)
            
            # If clicked day is less than or equal to current day, show the gift
            if day <= current_day:
                self.modal_image = gift[day - 1]
            else:
                self.modal_image = "/no_disponible.png"
        else:
            self.modal_image = "/no_disponible.png"
            
        self.modal_open = True

def calendar() -> rx.Component:
    """Main calendar component."""
    return rx.vstack(
        # Header section
        rx.flex(
            rx.box(
                rx.image(
                    src="/heart.png",
                    width="50px",
                    height="50px"
                )
            ),
            rx.heading(
                "Calendario de (te)ad(miro)(nunca)vi()en(mi vida nadie tan boni)to",
                size="4",
                color=TextColor.PRIMARY.value,
            ),
            spacing="4",
            align="center", 
            justify="center",
            width="100%"
        ),
        # Calendar grid
        rx.flex(
            rx.foreach(
                AdventState.days,
                lambda i: rx.dialog.root(
                    rx.dialog.trigger(
                        rx.image(
                            src=f"/day{i}.png",
                            width="170px",
                            height="170px",
                        )
                    ),
                    rx.dialog.content(
                        rx.dialog.title(f"Día {i}"),
                        rx.flex(
                            rx.image(
                                src=AdventState.modal_image,
                                width="400px",
                                height="400px",
                                object_fit="contain"
                            ),
                            align="center",
                            justify="center",
                            width="100%",
                            height="100%",
                        ),
                        rx.flex(
                            rx.dialog.close(
                                rx.button("Cerrar")
                            ),
                            justify="end",
                            width="100%"
                        ),
                        max_width="500px",
                    ),
                    on_open_change=lambda: AdventState.check_and_open(i),
                )
            ),
            flex_wrap="wrap",
            spacing="8",
            justify="center", 
            padding="4",
            width="100%",
            max_width="1200px",
            margin="0 auto"
        ),
        spacing="8",
        align="center",
        width="100%"
    )