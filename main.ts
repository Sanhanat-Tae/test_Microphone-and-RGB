let strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    if (input.soundLevel() > 70) {
        strip.showColor(neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255)))
        basic.showIcon(IconNames.Happy)
        basic.pause(50)
    } else {
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        basic.showIcon(IconNames.Sad)
        basic.pause(50)
    }
})
