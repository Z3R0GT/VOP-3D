# este es un modulo que da al nodo una clase más
# especializada para administrar las estadisticas

class Stats():
    def __stats__(self) -> None:
        self.stats = {}
        
    def apply_effects(self, effect):
        print(effect)