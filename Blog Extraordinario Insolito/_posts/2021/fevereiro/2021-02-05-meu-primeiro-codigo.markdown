---
layout: post
title: "Meu primeiro programa em Python"
description: "Uma explosão de entusiasmo, orgulho, dor, frustração e satisfação. Cada linha é uma emoção diferente."
---

---


<br>


Não tem como negar que Python é uma linguagem bem simples e cativante.

Iniciei meus estudos com o VisualG, que foi uma forma de começar a desenvolver um pensamento computacional, depois passei para a linguagem C e por ultimo (até agora) o Python.

De cara me apaixonei por Python, pela simplicidade, objetividade, códigos limpos e curtos, nossa não tive dúvidas de que iria focar nisso.


Resolvi criar meu primeiro programa útil. Algo que eu realmente fosse usar. Como eu já possuo este trabalho em que eu gerencio uma espécie de hostel/república, aproveitei para tentar facilitar parte do trabalho e decidi fazer uma calculadora de divisão de contas. Okay, a princípio parecia fácil:
- Soma as contas
- Divide pelo número de hospedes
- Fim


Parte de mim sabia que não seria assim tão simples, mas também não imaginei que seria tão complicado quanto realmente foi. Na verdade eu tinha que considerar diversos fatores e colocar diversos *ifs*:
- Um inquilino poderia entrar ou sair antes da data de pagamento, neste caso as contas não deveriam ser divididas da mesma forma que foi com os que estão o mês inteiro na casa
- A casa possui medidores de consumo individual em metade dos quartos (os que possuem ar-condicionado), a outra metade não possui, logo, é preciso retirar essa diferença do valor total que seria dividido
- Alguns inquilinos entram em casal, o que aumenta o consumo de recursos e, por isso, devem ser cobrados com valores adicionais
- Não consegui pensar numa forma de remover todos os consumos diretamente de uma única variável (como uma 'conta_total'). Cada diferença na situação de um quarto para o outro, afetava o valor das contas de todos os demais. Cada situação (como a divisão de quarto e entrada ou saída antes da hora) criava toda uma nova complexidade e bagunçava todo o resto do código.


Foi um inferno.


Como eu estava ainda engatinhando nos estudos de Python, a primeira versão desta calculadora ficou com mais de 800 linhas, não possuía interface gráfica e tinha diversos bugs, limitações de uso e erros em determinadas situações (caso houvesse 2 quartos vazios, 2 pessoas dividindo quarto ou coisas desse tipo). Conforme fui aprendendo novas coisas, fui fazendo atualizações até que comecei a ver um código mais organizado, mais eficiente e com menos bugs, até que finalmente saiu uma versão que está funcionando bem e que ainda não identifiquei uma falha nos cálculos. Tenho certeza de que este código ainda pode ser melhorado, simplificado e resolver o mesmo problema com menos linhas, mas utilizei todo o conhecimento de Python que possuía para chegar nessa versão. Daqui a uns meses, quando estarei mais evoluído nos meus estudos, pretendo voltar nele e ver se consigo utilizar novos conhecimentos para aprimorar a LazyCapybara!




<details>
    <summary>Clique aqui para ver o código</summary>

{% highlight python %}


# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.ttk as ttk


# Configs iniciais da interface gráfica
root = Tk()
root.title('Lazy Cabypara Calculator')
root.geometry('700x980')

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)


# Essa canvas foi necessária para poder criar um scrollbar, já que o tkinter possui essa limitação com o scrollbar
my_canvas = Canvas(main_frame, bg='#131313')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))


# Agora todo o resto da interface será escrita neste segundo frame, já que o mainframe foi basicamente dedicado ao canvas/scrollbar
second_frame = Frame(my_canvas, bg='#131313')

my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

myColor = '#313140'
root.configure(bg=myColor)
s = ttk.Style()
s.configure('Wild.TRadiobutton', background=myColor, foreground='white')

title = Label(second_frame, text='Casa 06', bg='greenyellow').grid(row=0, column=0)


# Aqui começa o código. Fiz uma função única com todas as entradas e marcações na interface para ficar tudo em um único botão
def casa_6(valor_conta_luz, valor_conta_agua, dias_mes,
           valor_Q1, divide_Q1, situacao_Q1, medi_ant_Q1, medi_atu_Q1,
           valor_Q2, divide_Q2, situacao_Q2, medi_ant_Q2, medi_atu_Q2,
           valor_Q3, divide_Q3, situacao_Q3, medi_ant_Q3, medi_atu_Q3,
           valor_Q4, divide_Q4, situacao_Q4,
           valor_Q5, divide_Q5, situacao_Q5,
           valor_Q6, divide_Q6, situacao_Q6,
           entrada_Q1, entrada_Q2, entrada_Q3, entrada_Q4, entrada_Q5, entrada_Q6):
    

    # Variáves
    # Uma lista com 6 tuplas. Os quartos com medidores possuem 2 posições a mais
    quartos = [
        (float(valor_Q1), divide_Q1, situacao_Q1, entrada_Q1, (medi_ant_Q1), (medi_atu_Q1)),
        (float(valor_Q2), divide_Q2, situacao_Q2, entrada_Q2, (medi_ant_Q2), (medi_atu_Q2)),
        (float(valor_Q3), divide_Q3, situacao_Q3, entrada_Q3, (medi_ant_Q3), (medi_atu_Q3)),
        (float(valor_Q4), divide_Q4, situacao_Q4, entrada_Q4),
        (float(valor_Q5), divide_Q5, situacao_Q5, entrada_Q5),
        (float(valor_Q6), divide_Q6, situacao_Q6, entrada_Q6)
    ]

    
    # Algumas outras variáveis que serão úteis ao longo do código (possível que tenha algum a mais aqui que ainda não tirei)
    contas = []
    delta_luz = valor_conta_luz
    quartos_ocupados = 0
    diferenca1 = 0
    ocupados = 0
    conta_pronta = []
    dividindo = 0
    desconto = 0

    
    # Operações
    # Calcular os gastos individuais (delta_luz) e contar os quartos que estão ocupados
    for y in range(0, 6):
        if y < 3:
            if quartos[y][2] == 1 or quartos[y][2] == 2 or quartos[y][2] == 3:
                delta_luz -= quartos[y][5] - quartos[y][4]
                conta_pronta.append(quartos[y][5] - quartos[y][4])
                quartos_ocupados += 1
            else:
                conta_pronta.append(0)
        if y == 3:
            if quartos[y][2] == 1 or quartos[y][2] == 2 or quartos[y][2] == 3:
                delta_luz -= 15
                conta_pronta.append(15)
                quartos_ocupados += 1
            else:
                conta_pronta.append(0)
        if y > 3:
            if quartos[y][2] == 1 or quartos[y][2] == 2 or quartos[y][2] == 3:
                delta_luz -= 10
                conta_pronta.append(10)
                quartos_ocupados += 1
            else:
                conta_pronta.append(0)

    
    # Calculando o consumo diário para os casos em que o inquilino não ficou o mês inteiro na casa
    consumo_casa_total = valor_conta_agua + delta_luz
    try:
        consumo_casa_dia_parcial = (consumo_casa_total / int(dias_mes)) / quartos_ocupados
    except:
        pass

    
    # Calculando o consumo parcial dos quartos que estão entrando ou saindo
    for i in range(0, 6):
        if quartos[i][2] == 2 or quartos[i][2] == 3:
            contas.append(consumo_casa_dia_parcial * int(quartos[i][3]))  # quartos[i][3] = dias que usou
        elif quartos[i][2] == 0:
            contas.append(0)
        else:
            contas.append(consumo_casa_total / quartos_ocupados)
            ocupados += 1

            
    # Quando reduzido o valor dos quartos acima, fica sobrando um valor a ser pago
    # Acrescentando a diferença aos inquilinos que passaram o mês inteiro
    diferenca = sum(contas)
    if ocupados > 0 and ocupados < 6:
        diferenca1 = (consumo_casa_total - diferenca) / ocupados
        for x in range(0, 6):
            if quartos[x][2] == 1:
                contas[x] += diferenca1

    for v in range(0, 6):
        conta_pronta[v] += contas[v]

        
    # Adicionando valores nas contas dos quartos que estão com mais de uma pessoa
    for z in range(0, 6):
        if quartos[z][1] == 1:          
            dividindo += 1
            conta_pronta[z] += 100

    if dividindo >= 1:
        try:
            desconto = (100 * dividindo) / (quartos_ocupados - dividindo)
        
                
            # Essa diminuição do valor é necessária para evitar que os valores das contas de outros quartos fiquem negativos
            if dividindo < (quartos_ocupados - dividindo):
                desconto = (100 * dividindo) / (quartos_ocupados - dividindo)
            else:
                desconto = ((100 * dividindo) / (quartos_ocupados - dividindo)) / 2
        except:
            pass

        
    # Dando desconto nas contas proporcional ao tempo de uso do quarto
    try:
        for w in range(0, 6):
            if quartos[w][2] == 1 or quartos[w][2] == 2 or quartos[w][2] == 3:
                if quartos[w][1] == 0:
                    if quartos[w][2] == 1:
                        conta_pronta[w] -= desconto
                    else:
                        conta_pronta[w] -= (int(quartos[w][3]) / 30) * desconto
    except:
        pass                
                
    # Após os cálculos diferenciados para quartos divididos, muitas das vezes o valor acaba bugando (provavelmente algum erro no código)
    # Como o valor acaba ficando muito alto, todo valor extra, por causa do bug, é convertido em desconto
    try:
        recalculando = (sum(conta_pronta) - (valor_conta_luz + valor_conta_agua)) / dividindo
        for w in range(0, 6):
            if quartos[w][2] == 1 or quartos[w][2] == 2 or quartos[w][2] == 3:
                if quartos[w][1] == 1:
                    conta_pronta[w] -= recalculando
    except:
        pass                
    
                
    # Preparando a ultima lista para mensagebox. Aqui são corrigidos valores de aluguéis para quartos que não passaram o mês inteiro
    aluguel = [x[0] for x in quartos]
    for x in range(0, 6):
        if quartos[x][2] == 0 or quartos[x][2] == 1:
            continue
        else:
            aluguel[x] = (aluguel[x] / 30) * int(quartos[x][3])

            
    # Mensagem final com todas as infos de pagamento
    messagebox.showinfo('Aluguéis',
                        f'Valor da conta de luz: R${valor_conta_luz}\nValor da conta de água: R${valor_conta_agua}\n\n   Quarto 1\nConta : R${round(conta_pronta[0], 2)}\nAluguel: R${round(quartos[0][0], 2)}\nTotal: R${round(conta_pronta[0] + aluguel[0], 2)}\n\n   Quarto 2\nConta: R${round(conta_pronta[1], 2)}\nAluguel: R${round(quartos[1][0], 2)}\nTotal: R${round(conta_pronta[1] + aluguel[1], 2)}\n\n   Quarto 3\nConta: R${round(conta_pronta[2], 2)}\nAluguel: R${round(quartos[2][0], 2)}\nTotal: R${round(conta_pronta[2] + aluguel[2], 2)}\n\n   Quarto 4\nConta: R${round(conta_pronta[3], 2)}\nAluguel: R${round(quartos[3][0], 2)}\nTotal: R${round(conta_pronta[3] + aluguel[3], 2)}\n\n   Quarto 5\nConta: R${round(conta_pronta[4], 2)}\nAluguel: R${round(quartos[4][0], 2)}\nTotal: R${round(conta_pronta[4] + aluguel[4], 2)}\n\n   Quarto 6\nConta: R${round(conta_pronta[5], 2)}\nAluguel: R${round(quartos[5][0], 2)}\nTotal: R${round(conta_pronta[5] + aluguel[5], 2)}')


# Frame para adicionar as contas
frameCasa = LabelFrame(second_frame, text='Contas', bg='#313140', fg='white', bd=4, padx=5, pady=5)
frameCasa.grid(padx=5, pady=5)

labelLuz = Label(frameCasa, text='Valor da conta de luz', bg='#313140', fg='white').grid(row=0, column=0)
entryLuz = Entry(frameCasa, borderwidth=4)
entryLuz.grid(row=0, column=1)

labelAgua = Label(frameCasa, text='Valor da conta de água', bg='#313140', fg='white').grid(row=1, column=0)
entryAgua = Entry(frameCasa, borderwidth=4)
entryAgua.grid(row=1, column=1)

labelDias = Label(frameCasa, text='Quantos dias possui o mês anterior', bg='#313140', fg='white').grid(row=2, column=0)
entryDias = Entry(frameCasa, borderwidth=4)
entryDias.grid(row=2, column=1)


# Label e Entrys Quarto 1
frameQuarto1 = LabelFrame(second_frame, text='Quarto 1', fg='white', bg='#313140', bd=4, padx=10, pady=10)
frameQuarto1.grid(padx=5, pady=5)

labelMedicaoAnteriorQ1 = Label(frameQuarto1, text='Digite a medição anterior', bg='#313140', fg='white').grid(row=0, column=0)
entryMedicaoAnteriorQ1 = Entry(frameQuarto1, borderwidth=4)
entryMedicaoAnteriorQ1.grid(row=0, column=1)

labelMedicaoAtualQ1 = Label(frameQuarto1, text='Digite a medição atual', bg='#313140', fg='white').grid(row=1, column=0)
entryMedicaoAtualQ1 = Entry(frameQuarto1, borderwidth=4)
entryMedicaoAtualQ1.grid(row=1, column=1)

labelValorCombinadoQ1 = Label(frameQuarto1, text='Digite o valor combinado', bg='#313140', fg='white').grid(row=2, column=0)
entryValorCombinadoQ1 = Entry(frameQuarto1, borderwidth=4)
entryValorCombinadoQ1.grid(row=2, column=1)

divideQ1 = IntVar()
checkQ1 = Checkbutton(frameQuarto1, text='Divide quarto?', bg='greenyellow', variable=divideQ1).grid(row=0, column=3)


# Radios Quarto 1
def parcial1(parcial_Q1):
    if parcial_Q1 == 0 or parcial_Q1 == 1:
        entradaQ1.config(state='disable')
        entradaQ1.grid(row=3, column=3)
    else:
        entradaQ1.config(state='normal')
        entradaQ1.grid(row=3, column=3)


situacaoQ1 = IntVar(0)
ttk.Radiobutton(frameQuarto1, text='Desocupado (mais de 30 dias)', style='Wild.TRadiobutton', variable=situacaoQ1,
                value=0, command=lambda: parcial1(situacaoQ1.get())).grid(row=0, column=2)
ttk.Radiobutton(frameQuarto1, text='Ocupado (mês inteiro)', style='Wild.TRadiobutton', variable=situacaoQ1, value=1,
                command=lambda: parcial1(situacaoQ1.get())).grid(row=1, column=2)
ttk.Radiobutton(frameQuarto1, text='Ocupado (parcialmente)', style='Wild.TRadiobutton', variable=situacaoQ1, value=2,
                command=lambda: parcial1(situacaoQ1.get())).grid(row=2, column=2)
ttk.Radiobutton(frameQuarto1, text='Saindo', style='Wild.TRadiobutton', variable=situacaoQ1, value=3,
                command=lambda: parcial1(situacaoQ1.get())).grid(row=3, column=2)
dias_efetivos = Label(frameQuarto1, text='Quantos dias utilizados?', bg='#313140', fg='white')
dias_efetivos.grid(row=2, column=3)
entradaQ1 = Entry(frameQuarto1, state='disable')
entradaQ1.grid(row=3, column=3)


# Label e Entrys Quarto 2
frameQuarto2 = LabelFrame(second_frame, text='Quarto 2', fg='white', bg='#313140', bd=4, padx=10, pady=10)
frameQuarto2.grid(padx=10, pady=10)

labelMedicaoAnteriorQ2 = Label(frameQuarto2, text='Digite a medição anterior', bg='#313140', fg='white').grid(row=0, column=0)
labelMedicaoAtualQ2 = Label(frameQuarto2, text='Digite a medição atual', bg='#313140', fg='white').grid(row=1, column=0)
labelValorCombinadoQ2 = Label(frameQuarto2, text='Digite o valor combinado', bg='#313140', fg='white').grid(row=2, column=0)

entryMedicaoAnteriorQ2 = Entry(frameQuarto2, borderwidth=4)
entryMedicaoAnteriorQ2.grid(row=0, column=1)

entryMedicaoAtualQ2 = Entry(frameQuarto2, borderwidth=4)
entryMedicaoAtualQ2.grid(row=1, column=1)

entryValorCombinadoQ2 = Entry(frameQuarto2, borderwidth=4)
entryValorCombinadoQ2.grid(row=2, column=1)

divideQ2 = IntVar()
checkQ2 = Checkbutton(frameQuarto2, text='Divide quarto?', bg='greenyellow', variable=divideQ2).grid(row=0, column=3)


# Radios Quarto 2
def parcial2(parcial_Q2):
    if parcial_Q2 == 0 or parcial_Q2 == 1:
        entradaQ2.config(state='disable')
        entradaQ2.grid(row=3, column=3)
    else:
        entradaQ2.config(state='normal')
        entradaQ2.grid(row=3, column=3)


situacaoQ2 = IntVar()
ttk.Radiobutton(frameQuarto2, text='Desocupado (mais de 30 dias)', style='Wild.TRadiobutton', variable=situacaoQ2,
                value=0, command=lambda: parcial2(situacaoQ2.get())).grid(row=0, column=2)
ttk.Radiobutton(frameQuarto2, text='Ocupado (mês inteiro)', style='Wild.TRadiobutton', variable=situacaoQ2, value=1,
                command=lambda: parcial2(situacaoQ2.get())).grid(row=1, column=2)
ttk.Radiobutton(frameQuarto2, text='Ocupado (parcialmente)', style='Wild.TRadiobutton', variable=situacaoQ2, value=2,
                command=lambda: parcial2(situacaoQ2.get())).grid(row=2, column=2)
ttk.Radiobutton(frameQuarto2, text='Saindo', style='Wild.TRadiobutton', variable=situacaoQ2, value=3,
                command=lambda: parcial2(situacaoQ2.get())).grid(row=3, column=2)
dias_efetivos = Label(frameQuarto2, text='Quantos dias utilizados?', bg='#313140', fg='white')
dias_efetivos.grid(row=2, column=3)
entradaQ2 = Entry(frameQuarto2, state='disable')
entradaQ2.grid(row=3, column=3)


# Label e Entrys Quarto 3
frameQuarto3 = LabelFrame(second_frame, text='Quarto 3', fg='white', bg='#313140', bd=4, padx=10, pady=10)
frameQuarto3.grid(padx=10, pady=10)

labelMedicaoAnteriorQ3 = Label(frameQuarto3, text='Digite a medição anterior', bg='#313140', fg='white').grid(row=0, column=0)
labelMedicaoAtualQ3 = Label(frameQuarto3, text='Digite a medição atual', bg='#313140', fg='white').grid(row=1, column=0)
labelValorCombinadoQ3 = Label(frameQuarto3, text='Digite o valor combinado', bg='#313140', fg='white').grid(row=2, column=0)

entryMedicaoAnteriorQ3 = Entry(frameQuarto3, borderwidth=4)
entryMedicaoAnteriorQ3.grid(row=0, column=1)

entryMedicaoAtualQ3 = Entry(frameQuarto3, borderwidth=4)
entryMedicaoAtualQ3.grid(row=1, column=1)

entryValorCombinadoQ3 = Entry(frameQuarto3, borderwidth=4)
entryValorCombinadoQ3.grid(row=2, column=1)

divideQ3 = IntVar()
checkQ3 = Checkbutton(frameQuarto3, text='Divide quarto?', bg='greenyellow', variable=divideQ3).grid(row=0, column=3)


# Radios Quarto 3
def parcial3(parcial_Q3):
    if parcial_Q3 == 0 or parcial_Q3 == 1:
        entradaQ3.config(state='disable')
        entradaQ3.grid(row=3, column=3)
    else:
        entradaQ3.config(state='normal')
        entradaQ3.grid(row=3, column=3)


situacaoQ3 = IntVar()
ttk.Radiobutton(frameQuarto3, text='Desocupado (mais de 30 dias)', style='Wild.TRadiobutton', variable=situacaoQ3,
                value=0, command=lambda: parcial3(situacaoQ3.get())).grid(row=0, column=2)
ttk.Radiobutton(frameQuarto3, text='Ocupado (mês inteiro)', style='Wild.TRadiobutton', variable=situacaoQ3, value=1,
                command=lambda: parcial3(situacaoQ3.get())).grid(row=1, column=2)
ttk.Radiobutton(frameQuarto3, text='Ocupado (parcialmente)', style='Wild.TRadiobutton', variable=situacaoQ3, value=2,
                command=lambda: parcial3(situacaoQ3.get())).grid(row=2, column=2)
ttk.Radiobutton(frameQuarto3, text='Saindo', style='Wild.TRadiobutton', variable=situacaoQ3, value=3,
                command=lambda: parcial3(situacaoQ3.get())).grid(row=3, column=2)
dias_efetivos = Label(frameQuarto3, text='Quantos dias utilizados?', bg='#313140', fg='white')
dias_efetivos.grid(row=2, column=3)
entradaQ3 = Entry(frameQuarto3, state='disable')
entradaQ3.grid(row=3, column=3)


# Label e Entrys Quarto 4
frameQuarto4 = LabelFrame(second_frame, text='Quarto 4', bg='#313140', fg='white', bd=4, padx=10, pady=10)
frameQuarto4.grid(padx=10, pady=10)
labelValorCombinadoQ4 = Label(frameQuarto4, text='Digite o valor combinado', bg='#313140', fg='white').grid(row=0, column=0)

entryValorCombinadoQ4 = Entry(frameQuarto4, borderwidth=4)
entryValorCombinadoQ4.grid(row=0, column=1)

divideQ4 = IntVar()
checkQ4 = Checkbutton(frameQuarto4, text='Divide quarto?', bg='greenyellow', variable=divideQ4).grid(row=0, column=3)


# Radios Quarto 4
def parcial4(parcial_Q4):
    if parcial_Q4 == 0 or parcial_Q4 == 1:
        entradaQ4.config(state='disable')
        entradaQ4.grid(row=3, column=3)
    else:
        entradaQ4.config(state='normal')
        entradaQ4.grid(row=3, column=3)


situacaoQ4 = IntVar()
ttk.Radiobutton(frameQuarto4, text='Desocupado (mais de 30 dias)', style='Wild.TRadiobutton', variable=situacaoQ4,
                value=0, command=lambda: parcial4(situacaoQ4.get())).grid(row=0, column=2)
ttk.Radiobutton(frameQuarto4, text='Ocupado (mês inteiro)', style='Wild.TRadiobutton', variable=situacaoQ4, value=1,
                command=lambda: parcial4(situacaoQ4.get())).grid(row=1, column=2)
ttk.Radiobutton(frameQuarto4, text='Ocupado (parcialmente)', style='Wild.TRadiobutton', variable=situacaoQ4, value=2,
                command=lambda: parcial4(situacaoQ4.get())).grid(row=2, column=2)
ttk.Radiobutton(frameQuarto4, text='Saindo', style='Wild.TRadiobutton', variable=situacaoQ4, value=3,
                command=lambda: parcial4(situacaoQ4.get())).grid(row=3, column=2)
dias_efetivos = Label(frameQuarto4, text='Quantos dias utilizados?', bg='#313140', fg='white')
dias_efetivos.grid(row=2, column=3)
entradaQ4 = Entry(frameQuarto4, state='disable')
entradaQ4.grid(row=3, column=3)


# Label e Entrys Quarto 5
frameQuarto5 = LabelFrame(second_frame, text='Quarto 5', bg='#313140', fg='white', bd=4, padx=10, pady=10)
frameQuarto5.grid(padx=10, pady=10)
labelValorCombinadoQ5 = Label(frameQuarto5, text='Digite o valor combinado', bg='#313140', fg='white').grid(row=0, column=0)

entryValorCombinadoQ5 = Entry(frameQuarto5, borderwidth=4)
entryValorCombinadoQ5.grid(row=0, column=1)

divideQ5 = IntVar()
checkQ5 = Checkbutton(frameQuarto5, text='Divide quarto?', bg='greenyellow', variable=divideQ5).grid(row=0, column=3)


# Radios Quarto 5
def parcial5(parcial_Q5):
    if parcial_Q5 == 0 or parcial_Q5 == 1:
        entradaQ5.config(state='disable')
        entradaQ5.grid(row=3, column=3)
    else:
        entradaQ5.config(state='normal')
        entradaQ5.grid(row=3, column=3)


situacaoQ5 = IntVar()
ttk.Radiobutton(frameQuarto5, text='Desocupado (mais de 30 dias)', style='Wild.TRadiobutton', variable=situacaoQ5,
                value=0, command=lambda: parcial5(situacaoQ5.get())).grid(row=0, column=2)
ttk.Radiobutton(frameQuarto5, text='Ocupado (mês inteiro)', style='Wild.TRadiobutton', variable=situacaoQ5, value=1,
                command=lambda: parcial5(situacaoQ5.get())).grid(row=1, column=2)
ttk.Radiobutton(frameQuarto5, text='Ocupado (parcialmente)', style='Wild.TRadiobutton', variable=situacaoQ5, value=2,
                command=lambda: parcial5(situacaoQ5.get())).grid(row=2, column=2)
ttk.Radiobutton(frameQuarto5, text='Saindo', style='Wild.TRadiobutton', variable=situacaoQ5, value=3,
                command=lambda: parcial5(situacaoQ5.get())).grid(row=3, column=2)
dias_efetivos = Label(frameQuarto5, text='Quantos dias utilizados?', bg='#313140', fg='white')
dias_efetivos.grid(row=2, column=3)
entradaQ5 = Entry(frameQuarto5, state='disable')
entradaQ5.grid(row=3, column=3)


# Label e Entrys Quarto 6
frameQuarto6 = LabelFrame(second_frame, text='Quarto 6', bg='#313140', fg='white', bd=4, padx=10, pady=10)
frameQuarto6.grid(padx=10, pady=10)
labelValorCombinadoQ6 = Label(frameQuarto6, text='Digite o valor combinado', bg='#313140', fg='white').grid(row=0, column=0)

entryValorCombinadoQ6 = Entry(frameQuarto6, borderwidth=4)
entryValorCombinadoQ6.grid(row=0, column=1)

divideQ6 = IntVar()
checkQ6 = Checkbutton(frameQuarto6, text='Divide quarto?', bg='greenyellow', variable=divideQ6).grid(row=0, column=3)


# Radios Quarto 6
def parcial6(parcial_Q6):
    if parcial_Q6 == 0 or parcial_Q6 == 1:
        entradaQ6.config(state='disable')
        entradaQ6.grid(row=3, column=3)
    else:
        entradaQ6.config(state='normal')
        entradaQ6.grid(row=3, column=3)


situacaoQ6 = IntVar()
ttk.Radiobutton(frameQuarto6, text='Desocupado (mais de 30 dias)', style='Wild.TRadiobutton', variable=situacaoQ6,
                value=0, command=lambda: parcial6(situacaoQ6.get())).grid(row=0, column=2)
ttk.Radiobutton(frameQuarto6, text='Ocupado (mês inteiro)', style='Wild.TRadiobutton', variable=situacaoQ6, value=1,
                command=lambda: parcial6(situacaoQ6.get())).grid(row=1, column=2)
ttk.Radiobutton(frameQuarto6, text='Ocupado (parcialmente)', style='Wild.TRadiobutton', variable=situacaoQ6, value=2,
                command=lambda: parcial6(situacaoQ6.get())).grid(row=2, column=2)
ttk.Radiobutton(frameQuarto6, text='Saindo', style='Wild.TRadiobutton', variable=situacaoQ6, value=3,
                command=lambda: parcial6(situacaoQ6.get())).grid(row=3, column=2)
dias_efetivos = Label(frameQuarto6, text='Quantos dias utilizados?', bg='#313140', fg='white')
dias_efetivos.grid(row=2, column=3)
entradaQ6 = Entry(frameQuarto6, state='disable')
entradaQ6.grid(row=3, column=3)


# Botão coletando todas Entrys, Radios e Checkboxs
calcularButton = Button(second_frame, text='Calcular', bg='greenyellow', command=lambda: casa_6(float(entryLuz.get()),
                float(entryAgua.get()),
                entryDias.get(),
                float(entryValorCombinadoQ1.get()),
                divideQ1.get(),
                situacaoQ1.get(),
                float(entryMedicaoAnteriorQ1.get()),
                float(entryMedicaoAtualQ1.get()),
                float(entryValorCombinadoQ2.get()),
                divideQ2.get(),
                situacaoQ2.get(),
                float(entryMedicaoAnteriorQ2.get()),
                float(entryMedicaoAtualQ2.get()),
                float(entryValorCombinadoQ3.get()),
                divideQ3.get(),
                situacaoQ3.get(),
                float(entryMedicaoAnteriorQ3.get()),
                float(entryMedicaoAtualQ3.get()),
                float(entryValorCombinadoQ4.get()),
                divideQ4.get(),
                situacaoQ4.get(),
                float(entryValorCombinadoQ5.get()),
                divideQ5.get(),
                situacaoQ5.get(),
                float(entryValorCombinadoQ6.get()),
                divideQ6.get(),
                situacaoQ6.get(),
                entradaQ1.get(),
                entradaQ2.get(),
                entradaQ3.get(),
                entradaQ4.get(),
                entradaQ5.get(),
                entradaQ6.get(),
                )).grid(row=8, column=0)

marca = Label(second_frame, text='Lazy Capybara \u00AE', bg='#131313', fg='white').place(relx=0.03, rely=0.98)

root.mainloop()


{% endhighlight %}

</details>


<br><br>

#### Resultado:


![Imagem da interface gráfica do programa](/assets/img_posts/programa_1.jpg)

<br>


![Imagem do resultado dos cálculos](/assets/img_posts/resultado.jpg)


<br>
<br>

<i>Obrigado por ter lido até aqui, você é uma pessoa sensacional. Tenha uma boa semana e bons estudos!</i> :heart:


<br>


<hr>