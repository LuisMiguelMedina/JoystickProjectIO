import Interface
from Controllers import JoystickController

teclas = Interface.get_button_letters()
JoystickController.keyboard_controller(teclas)
