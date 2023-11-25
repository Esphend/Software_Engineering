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


class gpu_specifications(gpu):
    def __init__(self, brand, gen, model, version, manufacturer, frequency, memory_type, tdp):
        super().__init__(brand, gen, model, version, manufacturer)
        self.frequency = frequency
        self.memory_type = memory_type
        self.tdp = tdp

    def gpu_specs(self):
        print(
            f'Характеристики данной видеокарты:\nЧастота = {self.frequency}\nТип памяти: {self.memory_type}\nПотребление: {self.tdp}')


my_gpu = gpu("AMD Radeon", "RX 6000", "RX 6700",
             "Fighter [AXRX 6700XT 12GBD6-3DH]1", "PowerColor")
my_gpu_spec = gpu_specifications("AMD Radeon", "RX 6000", "RX 6700",
                                 "Fighter [AXRX 6700XT 12GBD6-3DH]", "PowerColor",
                                 "2321 mhz", "GDDR6", "223 W")
my_gpu.gpu_type()
my_gpu.gpu_full_name()
my_gpu_spec.gpu_specs()
