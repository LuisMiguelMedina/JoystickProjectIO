import Interface
from Controllers import JoystickController

Interface.ACTIVE

teclas = Interface.get_button_letters()
JoystickController.keyboard_controller(teclas)