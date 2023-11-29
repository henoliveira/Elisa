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

Para instalar as dependencias do código em python (certifique-se que está no diretório do arquivo):

$ pip3 install -r requirements.txt

Para executar o programa em python basta executar o comando window.py (certifique-se que o arquivo é executável, tem permissão de execução):

$ ./window.py

OBS: Caso não tenha permissão para executar o arquivo, use o seguinte comando para obter permissão:

$ chmod u+x window.py

## Descrição

Este trabalho tem como objetivo a implementação do algoritmo DFS (busca em profundidade) utilizando OpenGL e Python.
