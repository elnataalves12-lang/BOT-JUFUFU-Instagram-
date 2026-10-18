from colorama import Fore, Style, init
init(autoreset=True)

AMARELO = Fore.YELLOW
VERDE = Fore.GREEN
VERMELHO = Fore.RED
RESET = Style.RESET_ALL

ARTE = r"""
   ██╗██╗   ██╗    ██╗███╗   ██╗███████╗████████╗ █████╗
   ██║██║   ██║    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗
   ██║██║   ██║    ██║██╔██╗ ██║███████╗   ██║   ███████║
██ ██║██║   ██║    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║
╚█████╔╝╚██████╔╝   ██║██║ ╚████║███████║   ██║   ██║  ██║
 ╚════╝  ╚═════╝    ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
"""

def banner_inicio():
    print(AMARELO + "━" * 40)
    print(AMARELO + "  🤖 JUFUFU INSTAGRAM BOT")
    print(AMARELO + "  Iniciando conexão...")
    print(AMARELO + "━" * 40)
    print(RESET)

def banner_online(username, bot_nome):
    print(AMARELO + ARTE)
    print(AMARELO + f"        🤖 {bot_nome}")
    print(AMARELO + "  " + "━" * 35)
    print(AMARELO + f"  🟡 Conectado como: @{username}")
    print(AMARELO + "  🟡 Bot online!")
    print(AMARELO + "  🟡 Aguardando mensagens...")
    print(AMARELO + "  " + "━" * 35)
    print(RESET)

def log_ok(msg): print(VERDE + f"✅ {msg}" + RESET)
def log_erro(msg): print(VERMELHO + f"❌ {msg}" + RESET)
def log_info(msg): print(AMARELO + f"🟡 {msg}" + RESET)