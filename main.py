def on_button_pressed_a():
    for index in range(4):
        basic.show_leds("""
            # # # # .
                        # . . . .
                        # # # # .
                        . . . # .
                        # # # # .
        """)
        basic.show_leds("""
            . # # # #
                        . # . . #
                        . # # # #
                        . # . . .
                        . # # # #
        """)
        basic.show_leds("""
            . # . # .
                        # . # . #
                        # . . . #
                        # . . . #
                        # . . . #
        """)
        basic.show_leds("""
            . # # # #
                        . # . . #
                        . # # # #
                        . # . . .
                        . # # # #
        """)
        basic.show_leds("""
            . # # . .
                        # . . # .
                        # # # . .
                        # . . # .
                        # . . . #
        """)
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
        basic.show_leds("""
            . # . # .
                        # . # . #
                        # . . . #
                        # . . . #
                        # . . . #
        """)
        basic.show_leds("""
            . # # # .
                        # . . # .
                        # . . # .
                        # # # . .
                        # . . . .
        """)
        basic.show_leds("""
            . # # # .
                        . . # . .
                        . . # . .
                        . . # . .
                        . # # # .
        """)
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
        basic.show_leds("""
            . # # # #
                        . # . . #
                        . # # # #
                        . # . . .
                        . # # # #
        """)
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # . . . .
                        # . . . .
                        # # # . .
        """)
        basic.show_leds("""
            . # # # #
                        # . . . .
                        # . . . .
                        # . . . .
                        . # # # #
        """)
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
        basic.show_leds("""
            . # # . .
                        # . . # .
                        # # # . .
                        # . . # .
                        # . . . #
        """)
        basic.show_leds("""
            . . # . .
                        . # . # .
                        . # # # .
                        . # . # .
                        . # . # .
        """)
        basic.show_leds("""
            # # # # .
                        . . . # .
                        . . # . .
                        . # . . .
                        # # # # .
        """)
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
        basic.show_leds("""
            # . . . #
                        # # . . #
                        # . # . #
                        # . . # #
                        # . . . #
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
