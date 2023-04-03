from gui import Interface
from random import randint

def test():
    print(gui.getSpeedLevel())
    print(gui.getPitchLevel())
    print(gui.getVolumeLevel())
    print(gui.getText())
    gui.setVoiceLevel(randint(0,100))

gui = Interface(test)