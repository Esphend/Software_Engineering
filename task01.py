class gpu:
    def __init__(self, brand, gen):
        self.brand = brand
        self.gen = gen


my_gpu = gpu("Radeon", "RX 500")
print(f"Данная видеокарта серии: {my_gpu.gen}, выпущена компаней {my_gpu.brand}.")
