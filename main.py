strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
basic.show_icon(IconNames.YES)

def on_forever():
    if input.sound_level() > 70:
        strip.show_color(neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        basic.show_icon(IconNames.HAPPY)
        basic.pause(50)
    else:
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        basic.show_icon(IconNames.SAD)
        basic.pause(50)
basic.forever(on_forever)
