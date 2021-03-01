global escolha_adversario
def escolha_adversario(variavel_escolha):
    global adversario
    adversario = variavel_escolha




global conta
def conta():
    global contador
    contador += 1





global apaga_tudo
def apaga_tudo(ataque_1, defesa_1, sorte_1, oponente):
    for ele in root.winfo_children():
        ele.destroy()
    
    jogador_1.insert(0, [ataque_1, defesa_1, sorte_1])
    if oponente == 0:
        jogador_2.insert(0, oponente_0)

        def malvado():           
            agilidade = Label(image=personagem_agilidade, borderwidth=0)
            agilidade.grid(row=3, column=3)
            if jogador_2[1][0] <= 0:
                morto_2 = Label(image=personagem_agilidade_morto, borderwidth=0)
                morto_2.grid(row=3, column=3)
    

    elif oponente == 1:
        jogador_2.insert(0, oponente_1)

        def malvado():         
            balanceado = Label(image=personagem_balanceado, borderwidth=0)
            balanceado.grid(row=3, column=3)
            if jogador_2[1][0] <= 0:
                morto_2 = Label(image=personagem_balanceado_morto, borderwidth=0)
                morto_2.grid(row=3, column=3)


    elif oponente == 2:
        jogador_2.insert(0, oponente_2)

        def malvado():
            escudo = Label(image=personagem_escudo, borderwidth=0)
            escudo.grid(row=3, column=3)
            if jogador_2[1][0] <= 0:
                morto_2 = Label(image=personagem_escudo_morto, borderwidth=0)
                morto_2.grid(row=3, column=3)


    else:
        jogador_2.insert(0, oponente_3)
        
        def malvado():
            sorte = Label(image=personagem_sorte, borderwidth=0)
            sorte.grid(row=3, column=3)
            if jogador_2[1][0] <= 0:
                morto_2 = Label(image=personagem_sorte_morto, borderwidth=0)
                morto_2.grid(row=3, column=3)
            
            

    defesa_jogador_1 = defesa_1
    defesa_jogador_2 = jogador_2[0][1]
    
    
    global lutinha
    def lutinha():
        for ele in root.winfo_children():
            ele.destroy()
        
        if jogador_2[1][0] == 100:
            vida_100 = Label(image=vida_100_label, borderwidth=0).grid(row=2, column=3) 
        elif jogador_2[1][0] < 100 and jogador_2[1][0] > 90:
            vida_90 = Label(image=vida_90_label, borderwidth=0).grid(row=2, column=3)
        elif jogador_2[1][0] <= 90 and jogador_2[1][0] > 80:
            vida_80 = Label(image=vida_80_label, borderwidth=0).grid(row=2, column=3)
        elif jogador_2[1][0] <= 80 and jogador_2[1][0] > 70:
            vida_70 = Label(image=vida_70_label, borderwidth=0).grid(row=2, column=3)
        elif jogador_2[1][0] <= 70 and jogador_2[1][0] > 60:
            vida_60 = Label(image=vida_60_label, borderwidth=0).grid(row=2, column=3)
        elif jogador_2[1][0] <= 60 and jogador_2[1][0] > 50:
            vida_50 = Label(image=vida_50_label, borderwidth=0).grid(row=2, column=3)
        elif jogador_2[1][0] <= 50 and jogador_2[1][0] > 40:
            vida_40 = Label(image=vida_40_label, borderwidth=0).grid(row=2, column=3)
        elif jogador_2[1][0] <= 40 and jogador_2[1][0] > 30:
            vida_30 = Label(image=vida_30_label, borderwidth=0).grid(row=2, column=3)
        elif jogador_2[1][0] <= 30 and jogador_2[1][0] > 20:
            vida_20 = Label(image=vida_20_label, borderwidth=0).grid(row=2, column=3)
        elif jogador_2[1][0] <= 20 and jogador_2[1][0] > 10:
            vida_10 = Label(image=vida_10_label, borderwidth=0).grid(row=2, column=3)
        elif jogador_2[1][0] <= 10 and jogador_2[1][0] > 0:
            vida_base = Label(image=vida_0_label, borderwidth=0).grid(row=2, column=3)
            

        if jogador_1[1][0] == 100:
            vida_100 = Label(image=vida_100_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] < 100 and jogador_1[1][0] > 90:
            vida_90 = Label(image=vida_90_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] <= 90 and jogador_1[1][0] > 80:
            vida_80 = Label(image=vida_80_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] <= 80 and jogador_1[1][0] > 70:
            vida_70 = Label(image=vida_70_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] <= 70 and jogador_1[1][0] > 60:
            vida_60 = Label(image=vida_60_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] <= 60 and jogador_1[1][0] > 50:
            vida_50 = Label(image=vida_50_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] <= 50 and jogador_1[1][0] > 40:
            vida_40 = Label(image=vida_40_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] <= 40 and jogador_1[1][0] > 30:
            vida_30 = Label(image=vida_30_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] <= 30 and jogador_1[1][0] > 20:
            vida_20 = Label(image=vida_20_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] <= 20 and jogador_1[1][0] > 10:
            vida_10 = Label(image=vida_10_label, borderwidth=0).grid(row=2, column=2)
        elif jogador_1[1][0] <= 10 and jogador_1[1][0] > 0:
            vida_base = Label(image=vida_0_label, borderwidth=0).grid(row=2, column=2)
 
        


            
            
            
        
        
        principal_label = Label(image=personagem_principal, borderwidth=0)
        principal_label.grid(row=3, column=2)
        malvado()
        def cabeca():
            conta()
            Label(root, text='{}\n{} ROUND {} {}\n{}'.format(29 * '*', 8 * '*', contador, 8 * '*', 29 * '*'), bg=fundo, font = fontStyle).grid(row=0, column=2, columnspan=2)
            Label(root, text=f'\n\nSaúde atual do Jogador 1: {str(jogador_1[1][0])}\t\tSaúde atual do Jogador 2: {str(jogador_2[1][0])}', bg = fundo, font = fontStyle2).grid(row=1, column=2, columnspan=2)

            
        cabeca()
        atacar_1 = Button(root, text="Atacar", borderwidth=1, bg=rosa, command=lambda: ataque_jogador_1(jogador_1[0][0], defesa_jogador_2)).grid(row=4, column=0)
        defender_1 = Button(root, text="Defender", borderwidth=1, bg=rosa, command=lambda: defesa_jogador_1()).grid(row=4, column=1)
        
        
        
        global ataque_jogador_1
        def ataque_jogador_1(dano, defesa):
            valor_ataque = (dano * 2 - defesa)

            if valor_ataque > 0:
                jogador_2[1][0] -= valor_ataque
            defesa = jogador_2[0][1]
            if jogador_1[0][2] > randint(1, 20):
                jogador_2[1][0] -= 10

            jogada_jogador_2()
            
        global defesa_jogador_1
        def defesa_jogador_1():
            defesa_1 = jogador_1[0][1] * 2
            if randint(1, 20) < jogador_1[0][2]:
                jogador_2[1][0] -= 10

            jogada_jogador_2(defesa_1)
            

        global jogada_jogador_2
        def jogada_jogador_2(defesa_1=jogador_1[0][1]):
            if randint(0, 1) == 0:
                if defesa_1 < jogador_2[0][0] * 2:
                    jogador_1[1][0] -= (jogador_2[0][0] * 2 - defesa_1)

            else:
                defesa2 = jogador_2[0][1] * 2

            if randint(1, 20) < jogador_2[0][2]:
                jogador_1[1][0] -= 10

            defesa_1 = jogador_1[0][1]
            if jogador_1[1][0] > 0 and jogador_2[1][0] > 0:
                lutinha()
            else:
                for ele in root.winfo_children():
                    ele.destroy()
                    principal_label = Label(image=personagem_principal, borderwidth=0)
                    principal_label.grid(row=3, column=2)
                    malvado()
                if jogador_1[1][0] <= 0 and jogador_2[1][0] > 0:
                    morreu = Label(image=morreu_label, borderwidth=0).grid(row=2, column=2)
                    venceu = Label(image=venceu_label, borderwidth=0).grid(row=2, column=3)
                    morto_1 = Label(image=personagem_principal_morto, borderwidth=0).grid(row=3, column=2)
                elif jogador_2[1][0] <= 0 and jogador_1[1][0] > 0:
                    morreu = Label(image=morreu_label, borderwidth=0).grid(row=2, column=3)
                    venceu = Label(image=venceu_label, borderwidth=0).grid(row=2, column=2)
                elif jogador_2[1][0] <= 0 and jogador_1[1][0] <= 0:
                    morreu = Label(image=morreu_label, borderwidth=0).grid(row=2, column=2)
                    morreu = Label(image=morreu_label, borderwidth=0).grid(row=2, column=3)
                    morto_1 = Label(image=personagem_principal_morto, borderwidth=0).grid(row=3, column=2)
                
    lutinha()
