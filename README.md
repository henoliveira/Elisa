SOBRE OS CÓDIGOS
----------------

Os códigos disponibilizados na disciplina foram desenvolvidos em sistema Linux nas linguagens C++ e PYTHON (python3).

Na sequência serão descritas as bibliotecas necessárias para executar os códigos em Linux e também um exemplo de como executar os programas.

Os tutoriais disponibilizados na disciplina cobrem instalação do OpenGL para outros sistemas operacionais. Você pode segui-los caso prefira usar outro SO para desenvolver seus programas.


SOBRE EXERCÍCIOS E ATIVIDADES AVALIATIVAS ENTREGUES PARA O PROFESSOR  
--------------------------------------------------------------------

Todas as atividades entregues durante a disciplina devem compilar e executar em ambiente Linux.

Os códigos em C devem ser acompanhados de um Makefile para a compilação.

IMPORTANTE: No caso de usar outro SO para desenvolver as atividades, você deve se certificar que qualquer exercício ou avaliação entregue deve compilar e executar em sistema Linux sem problemas. Verifique antes de entregar.

Qualquer falha ao compilar ou executar os programas será penalizado como um programa que não funciona.


BIBLIOTECAS NECESSÁRIAS
-----------------------

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


COMPILAÇÃO E/OU EXECUÇÃO
------------------------

Para compilar e executar o código em window.cpp em C++ (certifique-se que está no diretório do arquivo):

- compilação

$ make

- execução

$ ./window


Para executar o programa em python basta executar o comando window.py (certifique-se que o arquivo é executável, tem permissão de execução):

$ ./window.py

OBS: Caso não tenha permissão para executar o arquivo, use o seguinte comando para obter permissão: 

$ chmod u+x window.py


