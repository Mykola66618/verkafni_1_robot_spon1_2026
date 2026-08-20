from machine import Pin
from neopixel import NeoPixel
from servo import Servo
from time import sleep_ms
from random import randint

neo = NeoPixel(Pin(42), 2)
servo = Servo(Pin(15))

while True:

    # Случайный цвет
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    # Противоположные цвета
    neo[0] = [r, g, b]
    neo[1] = [255 - r, 255 - g, 255 - b]
    neo.write()

    # Открываем рот
    for angle in range(80, 131, 5):
        servo.write_angle(angle)

        # Моргание
        neo.fill([0, 0, 0])
        neo.write()
        sleep_ms(100)

        neo[0] = [r, g, b]
        neo[1] = [255 - r, 255 - g, 255 - b]
        neo.write()
        sleep_ms(100)

    # Закрываем рот
    for angle in range(130, 79, -5):
        servo.write_angle(angle)

        # Моргание
        neo.fill([0, 0, 0])
        neo.write()
        sleep_ms(100)

        neo[0] = [r, g, b]
        neo[1] = [255 - r, 255 - g, 255 - b]
        neo.write()
        sleep_ms(100)