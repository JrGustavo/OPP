class Automovil:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = None
    
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapido':
           self.motor.inyecta_gasolina(10)
        else:
            self.motor.inyecta_gasolina(3)
                   
        self._estado = 'en_movimiento'(1):
        
class motor: 

      def __init__(self, cilindros, tipo='gasolina'):
          self.cilindros = cilindros
          self.tipo = tipo
          self._temperatura = 0
      
      def inyecta_gasolina(self, cantidad):      