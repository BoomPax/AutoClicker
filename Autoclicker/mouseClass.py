import mouse

class Mouse():
    def __init__(self):
        print(mouse.get_position())
        mouse.move(500,500, absolute=True)
        mouse.click("left")
        print(mouse.get_position())

