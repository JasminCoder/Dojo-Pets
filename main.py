from Ninja import Ninja
from Mascota import Mascota


#(self, name, tipo, golosinas, sonido)
mascota = Mascota("Estrella", "Chiguagua", "huesitos", "guau guau!")


#(self, nombre, apellido, mascota, premio, comida_mascota)
ninja = Ninja("Pedro", "Picapiedra", mascota, "Cariñitos", "Croquetas")



ninja.alimentar()

mascota.sonido_mascota()

ninja.caminar()

ninja.bañar_mascota()

mascota.dormir()


