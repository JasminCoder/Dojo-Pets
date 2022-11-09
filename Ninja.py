#class Ninja:
# implementar __init__( nombre, apellido, premios, comida_mascota, mascota)

from Mascota import Mascota

class Ninja:

    def __init__(self, nombre, apellido, mascota, premio, comida_mascota):
        
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = premio
        self.comida_mascota = comida_mascota


# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()    
    def caminar(self):
        self.mascota.jugar()
        print("Que divertido paseo!")
        return self


# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self):
        self.mascota.comer()
        print(f"Excelente! {self.mascota.name} comió {self.comida_mascota}")
        return self


# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def bañar_mascota(self):
        self.mascota.sonido_mascota()
        print(f"Mi mascota favorita {self.mascota.name}, ya está limpia!")
        return self