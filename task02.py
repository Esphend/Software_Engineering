class gpu:
    def __init__(self, brand, gen, model, version, manufacturer):
        self.brand = brand
        self.gen = gen
        self.model = model
        self.version = version
        self.manufacturer = manufacturer

    def gpu_type(self):
        print(f"Данная видеокарта серии: {self.gen}, выпущена компаней {self.brand}.")

    def gpu_full_name(self):
        print(f"Полное название видеокарты: {self.manufacturer} {self.brand} {self.model} {self.version}.")


my_gpu = gpu("AMD Radeon", "RX 6000", "RX 6700",
             "Fighter [AXRX 6700XT 12GBD6-3DH]", "PowerColor")
my_gpu.gpu_type()
my_gpu.gpu_full_name()
