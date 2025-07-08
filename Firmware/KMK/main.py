import board
import digitalio
from kmk import KMKKeyboard
from kmk.keys import KC
from kmk.modules import Layer

keyboard = KMKKeyboard()

switch1 = digitalio.DigitalInOut(board.D0)
switch1.switch_to_input(pull=digitalio.Pull.UP)

switch2 = digitalio.DigitalInOut(board.D1)
switch2.switch_to_input(pull=digitalio.Pull.UP)

switch3 = digitalio.DigitalInOut(board.D2)
switch3.switch_to_input(pull=digitalio.Pull.UP)

switch4 = digitalio.DigitalInOut(board.D3)
switch4.switch_to_input(pull=digitalio.Pull.UP)

switch5 = digitalio.DigitalInOut(board.D4)
switch5.switch_to_input(pull=digitalio.Pull.UP)

switch6 = digitalio.DigitalInOut(board.D5)
switch6.switch_to_input(pull=digitalio.Pull.UP)

switch7 = digitalio.DigitalInOut(board.D6)
switch7.switch_to_input(pull=digitalio.Pull.UP)

switch8 = digitalio.DigitalInOut(board.D7)
switch8.switch_to_input(pull=digitalio.Pull.UP)

switch9 = digitalio.DigitalInOut(board.D8)
switch9.switch_to_input(pull=digitalio.Pull.UP)

keyboard.pins = {
    board.D0: KC.A,
    board.D1: KC.B,
    board.D2: KC.C,
    board.D3: KC.D,
    board.D4: KC.E,
    board.D5: KC.F,
    board.D6: KC.G,
    board.D7: KC.H,
    board.D8: KC.I,
}

layer1 = Layer([KC.LSFT, KC.LCTL, KC.LALT])

if __name__ == "__main__":
    while True:
        keyboard.poll()
