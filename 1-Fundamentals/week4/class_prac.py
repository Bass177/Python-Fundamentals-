class Stationery:

    def __init__(self, color, size, model):
        self.color = color
        self.size = size
        self.model = model

    def write(self, message):
        print("the stationery is being used...")
        print(message)


class Pen(Stationery):

    def write(self, message):
        print(f"This message is dark and pretty: {message}")


class Pencil(Stationery):

    def write(self, message):
        print(f"this message is in graphite: {message}")


pen1 = Pen("black", 1.6, "velocity")
pencil1 = Pencil("yellow", 0.7, "mechanical")
