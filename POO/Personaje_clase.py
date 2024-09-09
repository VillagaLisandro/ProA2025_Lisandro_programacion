class Personaje:
    #atributo de clase
    estado = True #vivo
    vida = 100 
    
    #constructor / atributo de instancia
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre  = nombre 
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia 
        self.fuerza = fuerza 
        self.estado = Personaje.estado
        self.vida = Personaje.vida
        
    
    def atacar(self, otro_personaje):
        danio = self.fuerza = (otro_personaje.resistencia)
        #danio = max (0, danio)
        print(f"({self.nombre} ataca a {otro_personaje.nombre}causado " )
        otro_personaje.recibir_dano(danio)
       # else:
        #    print(f"")

        
        
    def recibir_dano(self, cantidad):
        if self.estado:
            self.vida = self.vida - cantidad
            print(f"{self.nombre} resibe {cantidad} de danio. Vida restante     ")
            if self.via <= 0:
             self.vida = 0 
            print(f"{self.nombre}ha muerto")
        else:
            print(f"{self.nombre}ya esta muerto ")
            
            
                
    
    def mostrar_info(sef): 
        
        print()
        
        