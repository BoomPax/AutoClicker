from pynput import keyboard

class Keyboard():
    def __init__(self):
        def onPress(key):
            print("{} was pressed".format(key))
        def onRelease(key):
            print("{} was released".format(key))

        #myKeyboard = Keyboard()
        listener = keyboard.Listener(
            on_press = onPress,
            on_release = onRelease)
        listener.start()
