from random import randint

class Jogador:    
        
    def __init__(self, ataque, defesa, sorte, vida=100, defesa_forte=False):
        self.ataque = ataque
        self.defesa = defesa
        self.sorte = sorte
        self.vida = vida
        self.defesa_forte = defesa_forte
        
        
    def vida_atual(self):
        print(f'Vida atual = {self.vida}')
        
    def atacando(self, destino):
        if destino.defesa_forte == True:            
            if (self.ataque * 2) > (destino.defesa * 2):
                ataque_forte_defesa(self, destino)
            else:
                falha()

        else:
            if (self.ataque * 2) > (destino.defesa):
                ataque_fraco(destino)
            else:
                falha()



    global ataque_forte_defesa
    def ataque_forte_defesa(self, destino):
        destino.vida -= (self.ataque * 2) - destino.defesa * 2
        print(f'O ataque removeu {(self.ataque * 2) - (destino.defesa * 2)}')
        reset_defesa(destino)
        
    global reset_defesa    
    def reset_defesa(destino):
        destino.defesa_forte == False
                
    def defendendo(self):
        self.defesa_forte = True
        
    global falha
    def falha():
        return 'Ataque não efetivo'
