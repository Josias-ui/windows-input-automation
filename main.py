import ctypes ## biblioteca do Python que permite chamar funções da API do sistema operacional
import time

SendInput = ctypes.windll.user32.SendInput ##função da API do Windows é usada para inserir comandos no sistema operacional, 
##simulando entradas de teclado e mouse. Estamos vinculando essa função ao Python.

# =========================
# Configurações
# =========================
KEY_Q = 0x10
KEY_E = 0x12
VK_ESCAPE = 0x1B

INTERVAL = 0.095
REPETITIONS = 1000

# =========================
# Estruturas da Windows API
# =========================

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class MouseInput(ctypes.Structure): #mouse
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union): # diz para o Windows qual input será
    _fields_ = [("ki", KeyBdInput), #input do teclado
                ("mi", MouseInput)]

class Input(ctypes.Structure): #os dados desse tipo de input
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)] #detalhes do input, perceba que aqui é chamado o Input_I

def press_key(hexKeyCode): ##funcao que pressiona a tecla 
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x)) ##SendIpunt faz parte da API nativa do Windows e interage diretamente com o sistema operacional 
    ##para simular eventos de entrada

def release_key(hexKeyCode): ##solta a tecla 
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# =========================
# Automação
# =========================

print('3 segundos para começar')
time.sleep(3)

for _ in range(REPETITIONS):
    if ctypes.windll.user32.GetAsyncKeyState(0x1B) & 0x8000:
        print("Encerrado")
        break
    press_key(KEY_Q)
    release_key(KEY_Q)
    press_key(KEY_E)
    release_key(KEY_E)

    time.sleep(INTERVAL)
