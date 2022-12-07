import interfaz
from Controllers import KeyboardController

teclas = interfaz.get_button_letters()
KeyboardController.keyboard_controller(teclas)
