# Windows Input Automation

Projeto desenvolvido em Python para estudar automação de entradas
de teclado no Windows utilizando `ctypes` e a API Win32.

## Sobre o projeto

O programa simula pressionamentos de teclas em intervalos
configuráveis utilizando a função `SendInput` da API do Windows.

O projeto foi desenvolvido como forma de estudo sobre:

- Automação com Python
- Interação com APIs do Windows
- Estruturas compatíveis com C utilizando `ctypes`
- Simulação de entradas de teclado
- Controle de intervalos e execução de tarefas repetitivas

## Tecnologias utilizadas

- Python 3
- `ctypes`
- Windows API (Win32)
- `SendInput`

## Funcionalidades

- Simulação de pressionamento e liberação de teclas
- Intervalo entre comandos configurável
- Número de repetições configurável
- Contagem regressiva antes da execução
- Interrupção da automação utilizando a tecla ESC

## Configuração

As principais configurações podem ser alteradas no início
do arquivo `main.py`:

```python
INTERVAL = 0.095
REPETITIONS = 1000
START_DELAY = 3