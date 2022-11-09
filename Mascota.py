#class Mascota:
# implementa __init__( name , tipo , golosinas ):
# implementa los siguientes métodos:

class Mascota:

    def __init__(self, name, tipo, golosinas, sonido):

        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 500
        self.energia = 150
        self.sonido = sonido
        

    #dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energia += 25
        print("Super, despues de dormir, mi energia aumento en 25! =", self.energia)
        return self


    #comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energia += 5  
        self.salud +=10
        #print(f"Exelente! {self.name} Subiste tu energia a:", self.energia, "y tu salud a:", self.salud)
        print(f"Delicioso!.. Ahora mi energia es de:", self.energia, "y mi salud de:", self.salud) 
        return self
        
    
    #jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        self.salud += 5
        print("Genial, mi energia ahora es de", self.energia)
        return self


    # ruido() - imprime el sonido que produce la mascota
    def sonido_mascota(self):
        print(self.sonido)
        


