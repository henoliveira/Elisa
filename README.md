## SOBRE OS CÓDIGOS

Os códigos disponibilizados na disciplina foram desenvolvidos em sistema Linux nas linguagens C++ e PYTHON (python3).

Na sequência serão descritas as bibliotecas necessárias para executar os códigos em Linux e também um exemplo de como executar os programas.

Os tutoriais disponibilizados na disciplina cobrem instalação do OpenGL para outros sistemas operacionais. Você pode segui-los caso prefira usar outro SO para desenvolver seus programas.

## SOBRE EXERCÍCIOS E ATIVIDADES AVALIATIVAS ENTREGUES PARA O PROFESSOR

Todas as atividades entregues durante a disciplina devem compilar e executar em ambiente Linux.

Os códigos em C devem ser acompanhados de um Makefile para a compilação.

IMPORTANTE: No caso de usar outro SO para desenvolver as atividades, você deve se certificar que qualquer exercício ou avaliação entregue deve compilar e executar em sistema Linux sem problemas. Verifique antes de entregar.

Qualquer falha ao compilar ou executar os programas será penalizado como um programa que não funciona.

## BIBLIOTECAS NECESSÁRIAS

Para compilar e executar os programas você precisará ter instaladas as seguintes bibliotecas no seu sistema. Os passos mostrados na sequência permitem que execute os programas disponibilizados durante a disciplina.

Todos os passos cobrem sistemas Linux baseados na distribuição Debian. Não serão cobertos outros sistemas. Fica a seu cargo a instalação e correta execução caso escolha um sistema diferente.

Serão necessários os seguintes pacotes:

- freeglut3-dev
- libglew-dev
- libglm-dev

Para sistemas baseados em Debian, como o Ubuntu, o gerenciador de pacotes synaptic pode auxiliar na instalação desses pacotes.

Para instalar o synaptic:

$ sudo apt-get install synaptic

Abra o programa synaptic e procure o pacote freeglut3-dev. Marque o pacote e instale (aplicar no menu do synaptic). O synaptic irá listar as dependências, basta aceitar que elas sejam instaladas também.

Depois procure e instale o pacote libglew-dev, da mesma forma feita para o freeglut3-dev.

Faça o mesmo para o pacote libglm-dev.

Para os códigos em python você precisará dos pacotes:

- libpython3-dev
- python3-pip
- numpy
- pyopengl

Os pacotes libpython3-dev e python3-pip podem ser instalados pelo synaptic, como nos pacotes anteriores.

Para instalar o numpy e o pyopengl, você deve executar os comandos (certifique-se que o PIP esteja atualizado):

$ pip3 install numpy
$ pip3 install pyopengl

OBS: Caso o PIP esteja desatualizado, use o seguinte comando para atualizar:

$ python -m pip install --upgrade pip

## COMPILAÇÃO E/OU EXECUÇÃO

Para compilar e executar o código em window.cpp em C++ (certifique-se que está no diretório do arquivo):

- compilação

$ make

- execução

$ ./window

Para instalar as dependencias do código em python (certifique-se que está no diretório do arquivo):

$ pip3 install -r requirements.txt

Para executar o programa em python basta executar o comando window.py (certifique-se que o arquivo é executável, tem permissão de execução):

$ ./window.py

OBS: Caso não tenha permissão para executar o arquivo, use o seguinte comando para obter permissão:

$ chmod u+x window.py

# Avaliação Prática 2

- Valor: 10,0 pontos
- Peso 8 na nota N2

#### Observações:

- Equipe: de 2 a 4 alunos.
- Na submissão da tarefa (SIGAA) submeta apenas um arquivo ZIP.
- ATENÇÃO! As entregas que não seguirem as descrições deste enunciado terão desconto na nota!

## Descrição

Este trabalho tem como objetivo desenvolver uma animação 3D de um algoritmo para grafos como por exemplo: Busca em Largura, Busca em Profundidade, Dijkstra, Bellman-Ford, Prim, Kruskal etc. A ideia é usar elementos lúdicos em um cenário 3D e simular a execução de um algoritmo sobre um grafo. A simulação de outros algoritmos estudados em cursos de Computação também podem ser sugeridos pelo grupo. Use a criatividade!

## Código _(valor: 4,0 pontos)_

A aplicação gráfica pode ser desenvolvida na linguagem desejada desde que seja utilizada a biblioteca OpenGL Moderna para as funcionalidades gráficas. (Sugestão: linguagem C/C++ ou Python). O código deve compilar no Sistema Operacional Linux (caso contrário, deve ser informado um manual para execução).

## Relatório _(valor: 3,0 pontos)_

Um documento escrito deve ser elaborado com o objetivo de descrever, de forma completa e sucinta, a implementação desenvolvida. O relatório deve conter os seguintes itens:

- Introdução sobre a aplicação desenvolvida.
- Apresentação das ferramentas, linguagens e bibliotecas utilizadas na implementação.
- Explicação dos detalhes importantes da implementação usando a biblioteca gráfica OpenGL.
  - Quais as técnicas utilizadas na implementação e onde foram usadas:
    - Imagens ou modelos 3D utilizados (item obrigatório).
    - Transformações geométricas como translação, rotação e escala (item obrigatório).
    - Projeções ortográficas ou perspectivas (item obrigatório).
    - Iluminação (item obrigatório).
    - Outras técnicas como texturas, por exemplo.
- Funcionalidades da aplicação semelhante a um manual do usuário.
- Conclusões sobre as dificuldades encontradas, problemas não resolvidos e conhecimentos adquiridos.
- Citação das referências utilizadas.

## Apresentação _(valor: 3,0 pontos)_

O grupo deverá preparar uma apresentação com o objetivo de mostrar o relatório elaborado e a execução do programa desenvolvido (**OBS:** todos os membros do grupo **DEVEM** participar da apresentação. Em caso de exceções, conversar com a professora.).

A apresentação deverá ser feita presencialmente durante o horário de aula do dia 29/11/2023, e deverá
ter duração entre 10 e 20 minutos, no máximo.

## Entregas

A entrega deverá ser realizada através da Tarefa definida no SIGAA até às **23h59** do dia **28/11/2023.**

- DEVE ser entregue um arquivo ZIP contendo:
  - Código: todos os arquivos necessários para executar o programa em Linux.
    - Incluir as bibliotecas utilizadas.
    - Incluir um arquivo README.txt com as instruções para execução do programa.
    - Incluir o arquivo Makefile para códigos em linguagem C/C++.
  - Relatório: documento de texto em formato PDF
