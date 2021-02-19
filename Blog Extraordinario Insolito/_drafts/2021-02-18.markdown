---
layout: post
title: "Conhecendo a biblioteca Pandas"
description: "O resultado de um projeto pessoal utilizando o Pandas pela primeira vez"
---

---


<br>


## Analisando e tratando dados com Pandas


Após um rápido curso de 10 horas que fiz na Alura[^1], resolvi testar meus novos conhecimentos e aproveitar para adiantar um projeto pessoal que já tinha com uns amigos. O projeto trata-se de um jogo de terror, e para acrescentar o máximo de qualidade ao projeto, resolvi pesquisar o máximo possível sobre jogos, filmes, livros e outros conteúdos de terror.


<br>


### Filmes


Como sempre gostei muito de filmes de terror, resolvi começar a pesquisar quais são os melhores filmes de terror de todos os tempos, considerando tanto avaliações de críticos profissionais quanto do público em geral. A princípio pensei em pegar o conjunto de dados (dataset) direto da IMDb[^2], mas devido ao altíssimo número de dados, quase todos os arquivos passavam de 100mb que é o limite permitido pelo GitHub. Como ainda se trata de um estudo, utilizei um dataset retirado do Kaggle[^3].


<br>


### Sobre o Dataset


A primeira coisa que notei ao iniciar meu projeto foi a diferença entre a quantidade de dados que eu estava lidando durante as aulas com o dataset da Kaggle. Enquanto no curso eu trabalhei com 259 linhas e 8 colunas em apenas 1 arquivo csv de 56kb, neste primeiro passo dos meus estudos eu me deparei com dois arquivos csv de 85.855 linhas e dezenas de colunas colunas, um aumento absurdo na quantidade de dados. Para ser sincero, eu imagino que isso seja uma quantidade pequena perto do que eu ainda encontrarei pelo meu caminho.

A segunda coisa que percebi foi que é bem mais simples do que eu pensei. Claro que eu utilizei apenas alguns recursos pois tratava-se apenas de um primeiro contato com a biblioteca e meu conhecimento ainda estava limitado apenas ao que havia sido passado no curso.


<br>


### O código


O código abaixo foi escrito utilizando o Jupyter Lab


Primeiro eu faço os imports e depois começo a abrir os arquivos:

<br>
{% highlight python %}
# -*- coding: utf-8 -*- 
import pandas as pd

data_filmes = pd.read_csv('IMDb_Movies/IMDb movies.csv')

data_filmes
{% endhighlight %}


<br>
Logo de cara já é possível ver a quantidade de dados e do que se trata algumas das colunas:

<br>

![](/assets/img_posts/dados_filmes_01.jpg)


![](/assets/img_posts/dados_filmes_01_ampliado_cima.jpg)


![](/assets/img_posts/dados_filmes_01_ampliado_baixo.jpg)


<br>
Então já abro o segundo arquivo e já dá para ver um número bem maior de colunas:


{% highlight python %}
data_notas = pd.read_csv('IMDb_Movies/IMDb ratings.csv')
data_notas
{% endhighlight %}

![](/assets/img_posts/dados_notas_01.jpg)


<br>


Então começo os trabalhos. Como muitos filmes possuem mais de um gênero (genre) e estão como uma única string, preciso separa-los em uma lista contendo cada gênero separado. Para isso utilizo o split, separando-os pela vírgula. Também reduzo a quantidade de colunas, deixando apenas o que é importante para esta pesquisa:


{% highlight python %}
data_filmes.genre = data_filmes.genre.str.split(',')
data_filmes = data_filmes[['original_title','year', 'genre']]
data_filmes
{% endhighlight %}


![](/assets/img_posts/dados_filmes_02_split.jpg)


<br>


Agora já separo as colunas importantes do arquivo com as notas e faço a concatenação entre os dois arquivos .csv, criando a variável dataset que reduz as colunas de 71 para apenas 5:


{% highlight python %}
data_notas = data_notas[['weighted_average_vote', 'mean_vote']]
dataset = pd.concat([data_filmes, data_notas], axis = 1)
{% endhighlight %}


![](/assets/img_posts/dataset_01.jpg)


<br>


Pronto. Finalmente a hora de separar apenas os filmes de terror.


Nessas próximas linhas eu utilizo um laço for do tamanho do dataset para poder passar por todos os gêneros e separar apenas os de Horror. Utilizo o strip() para remover os possíveis espaços que restaram após o split(','). Também crio uma nova variável que contém apenas os filmes que possuam o gênero Horror e utilizo o iloc[z].values para acrescentar a linha completa de cada um desses filmes, baseado no index e logo que termina o laço, transformo o novo dataset_horror em um DataFrame:


{% highlight python %}
dataset_horror = []
for z in range(len(dataset)):
    for y in dataset.genre[z]:
        if y.strip() == 'Horror':
            dataset_horror.append(dataset.iloc[z].values)
            
dataset_horror = pd.DataFrame(dataset_horror)

dataset_horror
{% endhighlight %}


![](/assets/img_posts/dataset_horror_01.jpg)


<br>


Uau! Depois de filtrar 85.855 filmes, terminamos com 'apenas' 9.557 que possua Horror entre os gêneros.


Agora é hora de separar somente os melhores avaliados para poder assistir.


Novamente, mais uma variável que utiliza outro for para varrer todos os 9,557 filmes buscando somente aqueles que possuem médias ponderadas E aritméticas com o valor 8 para cima. Mas acontece algo interessante... fiquei sem saber qual das duas médias eu iria utilizar como critério para ordenar os filmes, então resolvi criar mais uma coluna com uma terceira média que é a média aritmética das médias. Ficou confuso? Dá uma olhada nas linhas:


{% highlight python %}
filmes_para_assistir = []

for x in range(len(dataset_horror)):
    if dataset_horror[3][x] >= 8 and dataset_horror[4][x] >= 8:
        filmes_para_assistir.append(dataset_horror.iloc[x].values)
        
filmes_para_assistir = pd.DataFrame(filmes_para_assistir)


for index, row in filmes_para_assistir.iterrows():
    filmes_para_assistir.loc[index, 5] = (row[3] + row[4]) / 2
    
filmes_para_assistir
{% endhighlight %}


![](/assets/img_posts/filmes_para_assistir_01.jpg)


<br>


Pronto!!! Simples assim.


É importante notar que os gêneros dos filmes podem acabar não significando exatamente o que a gente gostaria, então podemos ver alguns filmes como 'Post' (The Post: A Guerra Secreta), 'Concrete Shark' e alguns outros filmes que não são o que se pretende ver quando se faz este tipo de pesquisa pensando em tomar sustos e ficar horrorizado.


Outra coisa importante de se levar em consideração é que não foi feito nenhum tipo de consideração em outras variáveis como a região dos filmes, a quantidade de avaliações que o filme possui, a época em que foi lançado e outras coisas que poderiam alterar totalmente essa lista. Por exemplo : Um filme com 1 avaliação nota 10, terá esse valor como média, e como saberemos se essa avaliação foi legítima ou apenas de uma pessoa querendo colocar qualquer nota? Nessa lista vemos muitos filmes que não são tão conhecidos ou até totalmente desconhecidos pelo público estrangeiro. Isso pode inclusive explicar parte considerável dessa lista é de filmes da Ásia Meridional, onde a densidade populacional é enorme e o cinema nacional é extremamente popular.


<br>
Bom, para dar o acabamento do bolo, simplesmente nomeio e traduzo as colunas e ordeno os filmes pela nova média que criei. Por último, salvo o arquivo em csv:

{% highlight python %}
filmes_para_assistir.columns = ['Título', 'Ano', 'Gênero', 'Média ponderada', 'Média Aritmética', 'Média']
filmes_para_assistir.sort_values(by = 'Média', ascending = False, inplace = True)
filmes_para_assistir.index = range(filmes_para_assistir.shape[0])

filmes_para_assistir.to_csv('IMDb_Movies/Filmes_terror_para_assistir.csv', index = False, encoding = 'utf-8')
{% endhighlight %}

![](/assets/img_posts/filmes_para_assistir_02.jpg)


<br>


### Continuação...


Agora está na hora de continuar estudando e evoluir este trabalho para que fique cada vez melhor e mais interessante. Adicionar uns gráficos, fazer outros tipos de filtragens de dados, trazer informações mais precisas e interessantes para diversos públicos, quem sabe eu não faça um programa com uma interface gráfica?


Me diverti muito com esse estudo, por mais breve e simples que tenha sido, me mostrou que aprendi bem o conteúdo, abriu a minha cabeça para diversas outras coisas que precisam ser levadas em consideração na hora de se analisar dados e tive uma melhor direção de pontos que quero e que preciso melhorar.


<br>
<br>


<i>Obrigado por ter lido até aqui, você é o máximo! Tenha uma ótima semana. :heart:


<br>


<hr>
Referências:


[^1]:[Python para Data Science: Funções, Pacotes e Pandas básico](https://cursos.alura.com.br/course/python-funcoes-pacotes-pandas)
[^2]:[Dataset oficial da IMDb](https://datasets.imdbws.com/)
[^3]:[Dataset de filmes da IMDb Kaggle](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset)