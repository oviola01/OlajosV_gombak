class Gombaosztaly:
    def __init__(self,sor):
        self.gombaneve = sor[0]
        self.nemzettseg = sor[1]
        self.evszak = sor[2]
        
    def __str__(self):
        return f"{self.gombaneve}, {self.nemzettseg}, {self.evszak}"