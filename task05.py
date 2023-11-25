class pc_parts:
    def specs(self):
        pass


class gpu:
    def __init__(self, name, tdp, manufacturer):
        self.name = name
        self.tdp = tdp
        self.manufacturer = manufacturer

    def specs(self):
        print(f"Видеокарта {self.name} от производителя {self.manufacturer} имеет потребление {self.tdp}.")


class cpu:
    def __init__(self, name, tdp, socket):
        self.name = name
        self.tdp = tdp
        self.socket = socket
    def specs(self):
        print(f"Процессор  {self.name} имеет сокет {self.socket} и имеет тепловыделение {self.tdp}.")

class motherboard:
    def __init__(self, name, socket, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
        self.socket = socket

    def specs(self):
        print(f"Материнская плата {self.name} от производителя {self.manufacturer} имеет сокет {self.socket}.")


my_cpu = cpu("AMD Ryzen 5 5600", "65W", "AM4")
my_cpu.specs()
my_mother_board = motherboard("B450-A PRO", "AM4", "MSI")
my_mother_board.specs()
my_gpu = gpu("RTX 3070", "220W", "MSI")
my_gpu.specs()

