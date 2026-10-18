import os
import time
from datetime import datetime, timezone
from instagrapi import Client
from instagrapi.exceptions import LoginRequired

import config
from modules.banner import banner_inicio, banner_online, log_erro, log_info
from modules.login import fazer_login
from modules.comandos import (
    cmd_menu, cmd_ping, cmd_perfil, cmd_id,
    cmd_dado, cmd_moeda, cmd_play, cmd_corta, cmd_mudo,
)

os.makedirs(config.TEMP_DIR, exist_ok=True)

banner_inicio()
cl = Client()

if not fazer_login(cl, config.USERNAME, config.PASSWORD,
                   config.SESSIONID, config.SESSION_FILE):
    log_erro("Falha ao conectar.")
    exit()

banner_online(config.USERNAME, config.BOT_NOME)

respondidos = set()
ultima_resposta = {}

def strip_prefixo(txt):
    for p in config.PREFIXOS:
        if txt.startswith(p):
            return txt[len(p):].strip()
    return txt

while True:
    try:
        threads = cl.direct_threads(amount=5)

        for thread in threads:
            if not thread.messages:
                continue

            for msg in thread.messages:
                if str(msg.user_id) == str(cl.user_id):
                    continue

                texto = (msg.text or "").strip().lower()
                if not texto:
                    continue

                if msg.id in respondidos:
                    continue

                if msg.timestamp:
                    try:
                        idade = (datetime.now(timezone.utc) - msg.timestamp).total_seconds()
                        if idade > config.IDADE_MAX_MSG:
                            respondidos.add(msg.id)
                            continue
                    except: pass

                chave = (thread.id, texto)
                agora = time.time()
                if chave in ultima_resposta and (agora - ultima_resposta[chave]) < config.JANELA_DEDUP:
                    respondidos.add(msg.id)
                    continue
                ultima_resposta[chave] = agora

                cmd_txt = strip_prefixo(texto)
                if not cmd_txt:
                    continue

                partes = cmd_txt.split(maxsplit=1)
                cmd = partes[0]
                arg = partes[1].strip() if len(partes) > 1 else ""

                log_info(f"Nova: '{texto}' | thread: {thread.id}")

                if cmd in ("menu", "help", "start"):
                    cmd_menu(cl, thread.id, msg, respondidos)
                elif cmd == "ping":
                    cmd_ping(cl, thread.id, msg, respondidos)
                elif cmd == "perfil":
                    cmd_perfil(cl, thread.id, msg, respondidos)
                elif cmd == "id":
                    cmd_id(cl, thread.id, msg, respondidos)
                elif cmd == "dado":
                    cmd_dado(cl, thread.id, msg, respondidos)
                elif cmd == "moeda":
                    cmd_moeda(cl, thread.id, msg, respondidos)
                elif cmd == "play":
                    cmd_play(cl, thread.id, msg, arg, respondidos)
                elif cmd in ("corta", "crop"):
                    cmd_corta(cl, thread.id, msg, respondidos)
                elif cmd in ("mudo", "mute", "silencio"):
                    cmd_mudo(cl, thread.id, msg, respondidos)
                else:
                    respondidos.add(msg.id)

        time.sleep(15)

    except LoginRequired:
        log_info("Sessão caiu. Relogando...")
        if fazer_login(cl, config.USERNAME, config.PASSWORD,
                       config.SESSIONID, config.SESSION_FILE):
            continue
        break
    except KeyboardInterrupt:
        log_info("Encerrando...")
        break
    except Exception as e:
        log_erro(f"Erro no loop: {e}")
        time.sleep(30)