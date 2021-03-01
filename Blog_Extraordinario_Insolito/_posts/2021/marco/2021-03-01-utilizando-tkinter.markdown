---
layout: post
title: "Um código aleatório com Tkinter"
description: "Um dia eu resolvi complicar um pouco mais o que era para ser um simples exercício de lógica"
---


---


<br>


## Utilizando o Tkinter para fazer um jogo simples


Antes de mais nada é importante deixar claro que a ideia do jogo não é a diversão com ele em si, mas sim com o código. O jogo se trata apenas de uma luta entre um jogador humano e um computador. Sendo totalmente estático, utilizando apenas imagens (muito bem desenhadas por sinal) e dois botões para clicar (ataque e defesa).


<br>


### Como surgiu a ideia


Um dia um colega da faculdade me ligou e me perguntou se eu entendia de vetores e matriz em C, para ajudar um outro amigo dele em um trabalho da faculdade dele de Engenharia Química.
O trabalho era da matéria de Algoritmos e Programação Computacional, do professor Bruno Faccini Santoro (que eu não conheço).


Esta era a proposta :
<br>
>
 Criar um programa simulando um jogo de luta. Haverá
dois jogadores na partida, sendo o Jogador 1 o usuário (humano) e o Jogador 2 o computador.
Os jogadores duelam em uma sequência de embates (turnos). A cada jogador estão associados quatro números: seu poder de Ataque,
seu poder de Defesa, seu valor de Sorte e o seu nível de Saúde (HP). A soma dos valores de
Ataque, Defesa e Sorte deve ser exatamente igual a 30, sendo que cada um dos parâmetros deve
ser menor ou igual a 20. Para o Jogador 1, essas quantidades serão escolhidas pelo usuário antes
de iniciar a partida. Para o Jogador 2, o usuário poderá escolher um entre quatro oponentes:<br>
- Balanceado: Ataque = 10, Defesa = 10, Sorte = 10.
- Ofensivo: Ataque = 15, Defesa = 5, Sorte = 10.
- Defensivo: Ataque = 5, Defesa = 15, Sorte = 10.
- Sortudo: Ataque = 5, Defesa = 5, Sorte = 20.
<br><br>
Em cada turno, os jogadores devem escolher entre atacar ou defender.
No ataque, seu poder de Ataque é dobrado apenas para aquele ataque. No caso
da defesa, seu poder de Defesa é temporariamente dobrado.
Os dois jogadores iniciam com 100 pontos de Saúde. Ambos escolhem os
seus movimentos (o Jogador 2 por meio
de uma “inteligência artificial”) e então o programa calcula o dano causado por seus ataques:
- Se o valor de Ataque do Jogador 1 naquele instante é maior do que o valor de Defesa
do Jogador 2 no mesmo instante, o nível de Saúde do Jogador 2 será reduzido de uma
quantidade igual à diferença entre esses valores. Em caso contrário, o nível de Saúde do
Jogador 2 não é alterado.
- Posteriormente, os Jogadores têm uma chance de causar um dano extra conforme o seu
nível de Sorte. É gerado um número aleatório entre 1 e 20 e se o parâmetro de
Sorte do Jogador for maior do que o valor sorteado, então o oponente sofrerá 10 de dano adicional.
Esse “ataque crítico” é independente do que
aconteceu no item anterior.
>


Até então, tudo tranquilo. Ajudei o colega do meu colega(?) a realizar o trabalho, aproveitei para dar uma olhada novamente na linguagem C e fiquei pensando em fazer esse programa em Python e fazer uma interface só para praticar. Por que não?


### Mas o Tkinter não é orientado a objeto?


Sim. Mas por se tratar de uma GUI bem trivial, resolvi só utilizar o básico mesmo. De qualquer forma, já me comprometi a reescrever este código utilizando POO e irei posta-lo aqui no futuro :)



### Vamos ao código


Como sempre, iniciando pelas importações
{% highlight python %}
from random import randint
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
{% endhighlight %}

O randint é para gerar o valor aleatório entre 1 e 20 para testar se haverá o dano crítico ou não. Também utilizei para decidir os movimentos do Jogador 2 (computador), utilizando um range de 2 números, sendo um deles para ataque e outro para defesa.<br>O restante é coisa do Tkinter mesmo.


Agora é feita a configuração da interface e o upload das imagens
{% highlight python %}
root = Tk()
root.title('Capybara Fight')
fundo = '#ffaec9'
rosa = '#ffccdd'
root.configure(bg = fundo)
root.iconbitmap('./imagens/icone.ico')
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=15)

personagem_principal = ImageTk.PhotoImage(Image.open("./imagens/personagem_principal.png"))
personagem_agilidade = ImageTk.PhotoImage(Image.open("./imagens/personagem_agilidade.png"))
personagem_balanceado = ImageTk.PhotoImage(Image.open("./imagens/personagem_balanceado.png"))
personagem_escudo = ImageTk.PhotoImage(Image.open("./imagens/personagem_escudo.png"))
personagem_sorte = ImageTk.PhotoImage(Image.open("./imagens/personagem_sorte.png"))
personagem_principal_morto = ImageTk.PhotoImage(Image.open("./imagens/personagem_principal_morto.png"))
personagem_agilidade_morto = ImageTk.PhotoImage(Image.open("./imagens/personagem_agilidade_morto.png"))
personagem_balanceado_morto = ImageTk.PhotoImage(Image.open("./imagens/personagem_balanceado_morto.png"))
personagem_escudo_morto = ImageTk.PhotoImage(Image.open("./imagens/personagem_escudo_morto.png"))
personagem_sorte_morto = ImageTk.PhotoImage(Image.open("./imagens/personagem_sorte_morto.png"))
vida_100_label = ImageTk.PhotoImage(Image.open("./imagens/vida_100.png"))
vida_90_label = ImageTk.PhotoImage(Image.open("./imagens/vida_90.png"))
vida_80_label = ImageTk.PhotoImage(Image.open("./imagens/vida_80.png"))
vida_70_label = ImageTk.PhotoImage(Image.open("./imagens/vida_70.png"))
vida_60_label = ImageTk.PhotoImage(Image.open("./imagens/vida_60.png"))
vida_50_label = ImageTk.PhotoImage(Image.open("./imagens/vida_50.png"))
vida_40_label = ImageTk.PhotoImage(Image.open("./imagens/vida_40.png"))
vida_30_label = ImageTk.PhotoImage(Image.open("./imagens/vida_30.png"))
vida_20_label = ImageTk.PhotoImage(Image.open("./imagens/vida_20.png"))
vida_10_label = ImageTk.PhotoImage(Image.open("./imagens/vida_10.png"))
vida_0_label = ImageTk.PhotoImage(Image.open("./imagens/vida_base.png"))
morreu_label = ImageTk.PhotoImage(Image.open("./imagens/morreu.png"))
venceu_label = ImageTk.PhotoImage(Image.open("./imagens/venceu.png"))
{% endhighlight %}


Como a maior parte do programa é feita de imagens, criarei essas imagens diversas vezes ao longo do código


Mais interface. Esta é a primeira tela que aparece ao abrir o programa. Nela podemos ler as instruções, escolher os atributos do nosso personagem
e o adversário.<br>O código se inicia com um laço for para limpar toda a tela, passando por todos os widgets e 'destruindo-os'. O objeto disso é poder limpar a última tela do jogo e retornar para esta. Esse laço for será utilizado novamente para trocar desta tela para outra.
{% highlight python %}
global main
def main():
    for ele in root.winfo_children():
        ele.destroy()
    frame_instrucoes = LabelFrame(root, text='Instruções', font=fontStyle2, bg=rosa, bd=4, padx=10, pady=10)
    frame_instrucoes.grid(padx=40, pady=40, row=0, column=0, columnspan=3)
    Label(frame_instrucoes, bg=rosa, font=fontStyle2, text='Cada jogador terá uma ação por turno, escolhendo entre uma manobra arriscada ou conservadora.\nNo caso do movimento arriscado, seu poder de Ataque é dobrado apenas neste instante\nNo caso do movimento conservador, seu poder de Defesa é temporariamente dobrado.\nTem uma chance de causar 10 de dano extra (crítico) conforme o seu nível de Sorte.\nÉ feito o sorteio de um número aleatório entre 1 e 20 e se o parâmetro de Sorte for maior do que o valor sorteado,\nentão o Jogador 2 sofrerá esse ataque crítico, que é independente do que aconteceu no item anterior.').grid(row=0, column=0)
               
    frame_atributos = LabelFrame(root, text='Escolha seus atributos', font=fontStyle, bg=rosa, bd=4, padx=5, pady=5)
    frame_atributos.grid(padx=10, pady=10, row=1, column=0)
    Label(frame_atributos, font=fontStyle2, bg=rosa, text='Escolha seus atributos.\nVocê possui 30 pontos para dividir entre ataque, defesa e sorte.\n*Um atributo precisa ter ao menos 1 ponto e no máximo 20').grid(row=0, column=0, columnspan=3)
    Label(frame_atributos, font=fontStyle2, bg=rosa, text='Ataque').grid(row=1, column=0)
    entryAtaque = Entry(frame_atributos, width=4)
    entryAtaque.grid(row=1, column=1)
    Label(frame_atributos, font=fontStyle2, bg=rosa, text='Defesa').grid(row=2, column=0)
    entryDefesa = Entry(frame_atributos, width=4)
    entryDefesa.grid(row=2, column=1)
    Label(frame_atributos, font=fontStyle2, bg=rosa, text='Sorte').grid(row=3, column=0)
    entrySorte = Entry(frame_atributos, width=4)
    entrySorte.grid(row=3, column=1)

    frame_adversario = LabelFrame(root, text='Escolha seu adversario', font=fontStyle, bg=rosa, bd=4, padx=5, pady=5)
    frame_adversario.grid(padx=5, pady=5, row=1, column=1)
    variavel_escolha = IntVar()
    variavel_escolha.set(' ')
    Radiobutton(frame_adversario, font=fontStyle2, text='Ofensivo', variable=variavel_escolha, value=0, bg=rosa, command=lambda: escolha_adversario(variavel_escolha.get())).grid(row=5, column=0)
    Radiobutton(frame_adversario, font=fontStyle2, text='Balanceado', variable=variavel_escolha, value=1, bg=rosa, command=lambda: escolha_adversario(variavel_escolha.get())).grid(row=6, column=0)
    Radiobutton(frame_adversario, font=fontStyle2, text='Defensivo', variable=variavel_escolha, value=2, bg=rosa, command=lambda: escolha_adversario(variavel_escolha.get())).grid(row=7, column=0)
    Radiobutton(frame_adversario, font=fontStyle2, text='Sortudo', variable=variavel_escolha, value=3, bg=rosa, command=lambda: escolha_adversario(variavel_escolha.get())).grid(row=8, column=0)
{% endhighlight %}


<br>


![Tela inicial do projeto](/assets/img_posts/tela_inicial.jpg)


<br>


Após selecionar os atributos e o adversário, é só iniciar a luta

{% highlight python %}
    global escolha_adversario
    def escolha_adversario(variavel_escolha):
        global adversario
        adversario = variavel_escolha
        
    jogador_1 = [[100]]
    jogador_2 = [[100]]
    oponente_0 = [15, 5, 10]
    oponente_1 = [10, 10, 10]
    oponente_2 = [5, 15, 10]
    oponente_3 = [5, 5, 20]
    global contador
    contador = 0
    global conta
    def conta():
        global contador
        contador += 1
    botao = Button(root, font=fontStyle, text="Iniciar luta", command=lambda: apaga_tudo(ataque_1=int(entryAtaque.get()), defesa_1=int(entryDefesa.get()), sorte_1=int(entrySorte.get()), oponente=int(adversario)))
    botao.grid(row=10, column=0)
{% endhighlight %}



![Tela inicial do projeto](/assets/img_posts/tela_round_1.jpg)


<br>


Agora, ainda simples:
- Deleto a tela anterior utilizando aquele mesmo for de antes para começar uma nova
- Insiro os atributos aos jogadores com o .insert
- Crio uma função diferente para cada tipo de oponente que pode ser escolhido, para atribuir as imagens do oponente vivo e morto (caso ele morra)


{% highlight python %}
    global apaga_tudo
    def apaga_tudo(ataque_1, defesa_1, sorte_1, oponente):            
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
{% endhighlight %}


![Tela inicial do projeto](/assets/img_posts/tela_meio_luta.jpg)


<br>


Agora, o que cria esse resultado da imagem acima, é uma enorme função que:
- Destrói a tela anterior
- Cria 11 imagens mostrando a vida para cada jogador, mais uma imagem de cada jogador vivo e outra morto.
- Inicia um cabeçalho mostrando o ROUND, as imagens a serem mostradas, dois botões, uma função para cada botão e uma terceira função 
para a jogada do Jogador 2. Dentro de cada função já é considerado se o oponente está defendendo, se houve crítico, se houve e qual o valor de dano causado.
- Por último, verifica se houve alguma morte.
- Ao fim do duelo, apaga a tela e exibe uma nova anunciando o resultado.
- É liberado um botão para voltar para a tela inicial.



{% highlight python %}
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
                    main_button = Button(root, font=fontStyle, text="Reiniciar", command=lambda: main()).grid(row=10, column=0)
                    
        lutinha()
main()

root.mainloop()
{% endhighlight %}


<br>


Como é possível notar, deixei ali no finalzinho a chamada do main() e depois da lutinha(), pois são as duas funções que, no primeiro uso, não são chamadas através de botões.


![Tela inicial do projeto](/assets/img_posts/tela_final.jpg)


<br>


## Curiosidades inúteis


- Eu mesmo fiz os desenhos no paint. Sei que não parece pois são incríveis desenhos dotados das mais altas técnicas de design moderno, mas acredite. Foi no paint.
- Cada oponente possui um desenho próprio
- Meu favorito é o *Sortudo* (última imagem do post)
- É possível empatar
- Coloquei quase tudo global porque não aguentava mais ler *"UnboundLocalError: local variable 'contador' referenced before assignment"*
- O colega do meu colega nunca retornou dizendo se foi bem no trabalho ou não :(


<br>


![Tela inicial do projeto](/assets/img_posts/tela_final_defesa.jpg)


<br>


![Tela inicial do projeto](/assets/img_posts/tela_final_empate.jpg)


<br>
<br>


### Considerações finais


Me diverti muito com essa brincadeira. Ri demais com o desenrolar do código, com cada desenho que fiz e até com os bugs.<br>Recomendo
esses trabalhos de engenharia química pois, apesar deste ser simples, foi bem interessante e estimulador. Ajudem colegas de colegas que é uma coisa boa, você pratica um pouco de coisas aleatórias, aprende enquanto ensina e pode fazer amigos para trocar códigos, experiências e conhecimentos. Não foi o meu caso, mas paciência.


![Tela inicial do projeto](/assets/img_posts/personagem_sorte.png)


<br>
<br>


<i>Obrigado por ter lido até aqui, você é uma ótima pessoa! Tenha uma boa semana. :heart:


<br>


<hr>