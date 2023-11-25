class gpu:
    def __init__(self, brand, gen, model, version, manufacturer):
        self.brand = brand
        self.gen = gen
        self._model = model
        self._version = version
        self.__manufacturer = manufacturer

    def gpu_type(self):
        print(f"Данная видеокарта серии: {self.gen}, выпущена компаней {self.brand}.")

    def gpu_full_name(self):
        print(f"Полное название видеокарты: {self.__manufacturer} {self.brand} {self._model} {self._version}.")


myning_gpu = gpu("GeForce", "GTX 1000", "GTX 1050",
                 "Ti", "Palit")
print(myning_gpu._model)
print(myning_gpu._version)
#print(myning_gpu.__manufacturer) ошибка! приватный атрибут не доступен
myning_gpu.gpu_full_name()