from morse_translator import MorseCodeTranslator
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
translator = MorseCodeTranslator()

w = (150, 150, 150)
r = (150, 0, 0)
b = (0, 0, 0)
bl = (0, 0, 150)
g = (0, 150, 0)

dot_image = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, w, w, b, b, b,
    b, b, b, w, w, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
]

dash_image = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
]

left_arrow_image = [
    b, b, r, r, b, b, b, b,
    b, r, r, b, b, b, b, b,
    r, r, b, b, b, b, b, b,
    r, r, r, r, r, r, r, b,
    r, r, r, r, r, r, r, b,
    r, r, b, b, b, b, b, b,
    b, r, r, b, b, b, b, b,
    b, b, r, r, b, b, b, b,
]

right_arrow_image = [
    b, b, b, b, g, g, b, b,
    b, b, b, b, b, g, g, b,
    b, b, b, b, b, b, g, g,
    b, g, g, g, g, g, g, g,
    b, g, g, g, g, g, g, g,
    b, b, b, b, b, b, g, g,
    b, b, b, b, b, g, g, b,
    b, b, b, b, g, g, b, b,
]

done_image = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, bl,
    b, b, b, b, b, b, bl, bl,
    b, b, b, b, b, bl, bl, b,
    bl, b, b, b, bl, bl, b, b,
    bl, bl, b, bl, bl, b, b, b,
    b, bl, bl, bl, b, b, b, b,
    b, b, bl, b, b, b, b, b,
]

sense.clear(b)

morse_code = []

def morse_code_from_sensehat():
    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    if not morse_code:
                        sense.show_message("Morse code cannot be empty!", text_colour=w)
                    else:
                        final_morse = "".join(morse_code)
                        sense.set_pixels(done_image)
                        sleep(0.5)
                        sense.clear(b)
                        return final_morse
                if event.direction == "up":
                    morse_code.append(".")
                    sense.set_pixels(dot_image)
                    sleep(0.5)
                    sense.clear(b)
                if event.direction == "down":
                    morse_code.append("-")
                    sense.set_pixels(dash_image)
                    sleep(0.5)
                    sense.clear(b)
                if event.direction == "left":
                    del morse_code[-1]
                    sense.set_pixels(left_arrow_image)
                    sleep(0.5)
                    sense.clear(b)
                if event.direction == "right":
                    morse_code.append(" ")
                    sense.set_pixels(right_arrow_image)
                    sleep(0.5)
                    sense.clear(b)
                
sense.show_message("Welcome! Please enter morse message: ", text_colour=w)
final_morse = morse_code_from_sensehat()
sense.show_message("Final morse message: {0}".format(final_morse), text_colour=w)
translated_text = translator.translate_morse(final_morse)
sense.show_message("Translated morse: {0}".format(translated_text), text_colour=w)