import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP0, board.GP1, board.GP2)
    row_pins = (board.GP3, board.GP4, board.GP5)

    diode_orientation = DiodeOrientation.COL2ROW