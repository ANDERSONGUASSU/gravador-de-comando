# Gravador de comandos do mouse e teclado

Este projeto é um gravador de eventos de mouse e teclado que permite gravar e reproduzir ações do usuário. É uma ferramenta útil para automação de tarefas repetitivas. 

## Tecnologias Utilizadas

- **PyQt5**: Biblioteca para construção da interface gráfica do usuário.
- **pyautogui**: Biblioteca para automação de eventos de mouse e teclado.
- **pynput**: Biblioteca para escuta e controle de dispositivos de entrada como mouse e teclado.

## Instalação

### Clone o Repositório

Para baixar o projeto em sua máquina local, execute o comando abaixo no seu terminal:

```
git clone https://github.com/username/repository.git
```
### Crie um Ambiente Virtual
Navegue até o diretório do projeto e crie um ambiente virtual utilizando venv:
```
python3 -m venv venv
```
### Ative o Ambiente Virtual
- No Windows:
```
venv\Scripts\activate
```
- No macOS e Linux:
```
source venv/bin/activate
```
### Instale as Dependências
Com o ambiente virtual ativo, instale as dependências necessárias utilizando o arquivo requirements.txt:

```
pip install -r requirements.txt
```
### Executando o Projeto
Para iniciar a aplicação, execute o seguinte comando:

```
python3 app.py
```
## Como Utilizar
### Iniciar Gravação:

- Pressione o botão "Start Recording" na interface ou use a combinação de teclas Ctrl + Alt + R para começar a gravar os eventos de mouse e teclado.

### Parar Gravação:

- Pressione o botão "Stop Recording" na interface ou use a combinação de teclas Ctrl + Alt + S para parar a gravação dos eventos.

###Reproduzir Gravação:

- Utilize o botão "Play Recording" na interface ou a combinação de teclas Ctrl + Alt + P para reproduzir os eventos gravados.
- Ajuste o número de repetições usando o QSpinBox fornecido na interface.

## Funcionalidades
- **Gravação de Eventos**: Captura e grava eventos de mouse e teclado.
- **Reprodução de Eventos**: Reproduz os eventos gravados conforme o número de repetições definido.
- **Hotkeys Globais**: Controla a gravação e reprodução utilizando combinações de teclas rápidas.

##Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.


Feito com ❤️ por Anderson Guassú para Glaúcia Guassú.


