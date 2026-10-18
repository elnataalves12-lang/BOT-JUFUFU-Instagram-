import os
import time
import random
import requests
import config
from modules.tema import bloco
from modules.ytdlp import baixar_musica
from modules.audio import duracao, converter_m4a, montar_video
from modules.edits import baixar_url, pegar_midia, cortar_quadrado, silenciar

def responder(cl, thread_id, texto):
    try:
        cl.direct_send(texto, thread_ids=[thread_id])
        print(f"✅ {texto[:40].splitlines()[0]}...")
    except Exception as e:
        print(f"❌ Erro ao responder: {e}")

# ==================== MENU ====================

def cmd_menu(cl, thread_id, msg, respondidos):
    try:
        img_path = os.path.join(config.TEMP_DIR, "menu.jpg")
        if not os.path.exists(img_path):
            r = requests.get(config.MENU_IMAGE_URL, timeout=30)
            with open(img_path, "wb") as f:
                f.write(r.content)
        cl.direct_send_photo(img_path, thread_ids=[thread_id])
    except Exception as e:
        print(f"Erro imagem menu: {e}")

    responder(cl, thread_id, bloco("MENU", [
        "♪ /play <música>",
        "✂️ /corta (responder foto/vídeo)",
        "🔇 /mudo (responder vídeo)",
        "🏓 /ping",
        "👤 /perfil",
        "🎲 /dado",
        "🪙 /moeda",
        "🆔 /id",
    ]))
    respondidos.add(msg.id)

# ==================== SIMPLES ====================

def cmd_ping(cl, thread_id, msg, respondidos):
    responder(cl, thread_id, bloco("PING", [
        "🏓 Pong!",
        "⏱️ Online",
        f"🕒 {time.strftime('%H:%M:%S')}",
    ]))
    respondidos.add(msg.id)

def cmd_perfil(cl, thread_id, msg, respondidos):
    responder(cl, thread_id, bloco("PERFIL", [
        f"📛 ID: {msg.user_id}",
        f"🎮 Usos: {len(respondidos)}",
        "🏆 Nível: Guerreiro",
    ]))
    respondidos.add(msg.id)

def cmd_id(cl, thread_id, msg, respondidos):
    responder(cl, thread_id, bloco("ID", [
        f"🆔 Seu ID: {msg.user_id}",
        f"🧵 Thread: {thread_id}",
    ]))
    respondidos.add(msg.id)

def cmd_dado(cl, thread_id, msg, respondidos):
    n = random.randint(1, 6)
    responder(cl, thread_id, bloco("DADO", [f"🎲 Resultado: *{n}*"]))
    respondidos.add(msg.id)

def cmd_moeda(cl, thread_id, msg, respondidos):
    r = random.choice(["Cara 👑", "Coroa 🪙"])
    responder(cl, thread_id, bloco("MOEDA", [f"🪙 {r}"]))
    respondidos.add(msg.id)

# ==================== PLAY ====================

def cmd_play(cl, thread_id, msg, query, respondidos):
    if not query:
        responder(cl, thread_id, bloco("PLAY", "❌ Digite: /play nome da música"))
        respondidos.add(msg.id)
        return

    responder(cl, thread_id, bloco("PLAY", f"🔍 Buscando: {query}"))

    audio, titulo, thumb = baixar_musica(query)

    if not audio or not os.path.exists(audio):
        responder(cl, thread_id, bloco("PLAY", "❌ Não achei essa música."))
        respondidos.add(msg.id)
        return

    dur = duracao(audio)
    m4a = converter_m4a(audio)

    enviado = False

    if m4a and os.path.exists(m4a) and dur <= 60:
        try:
            cl.direct_send_voice(m4a, thread_ids=[thread_id])
            responder(cl, thread_id, bloco("PLAY", [
                f"🎵 {titulo}",
                f"⏱️ {int(dur)}s",
            ]))
            enviado = True
        except:
            pass

    video_path = None
    if not enviado:
        video_path = montar_video(m4a or audio, thumb, dur)
        if video_path and os.path.exists(video_path):
            try:
                cl.direct_send_video(video_path, thread_ids=[thread_id])
                responder(cl, thread_id, bloco("PLAY", [
                    f"🎵 {titulo}",
                    f"⏱️ {int(dur)}s",
                ]))
                enviado = True
            except Exception as e:
                print(f"Vídeo falhou: {e}")

    if not enviado:
        responder(cl, thread_id, bloco("PLAY", "❌ Não consegui enviar."))

    for p in (audio, m4a, thumb, video_path):
        if p and isinstance(p, str):
            try: os.remove(p)
            except: pass

    respondidos.add(msg.id)

# ==================== CORTA ====================

def cmd_corta(cl, thread_id, msg, respondidos):
    reply = getattr(msg, "reply", None)
    if not reply:
        responder(cl, thread_id, bloco("CORTA", ["❌ Responda uma foto/vídeo com /corta"]))
        respondidos.add(msg.id)
        return

    url, tipo = pegar_midia(reply)
    if not url:
        responder(cl, thread_id, bloco("CORTA", "❌ Não achei mídia na mensagem."))
        respondidos.add(msg.id)
        return

    responder(cl, thread_id, bloco("CORTA", "🔄 Cortando..."))

    ext = ".mp4" if tipo == "video" else ".jpg"
    local = baixar_url(url, ext)
    if not local:
        responder(cl, thread_id, bloco("CORTA", "❌ Não consegui baixar."))
        respondidos.add(msg.id)
        return

    saida = cortar_quadrado(local)

    if saida and os.path.exists(saida):
        try:
            if tipo == "video":
                cl.direct_send_video(saida, thread_ids=[thread_id])
            else:
                cl.direct_send_photo(saida, thread_ids=[thread_id])
            responder(cl, thread_id, bloco("CORTA", "✅ Cortado quadrado!"))
        except Exception as e:
            responder(cl, thread_id, bloco("CORTA", f"❌ Erro: {e}"))
        finally:
            try: os.remove(saida)
            except: pass
    else:
        responder(cl, thread_id, bloco("CORTA", "❌ Falha ao cortar."))

    try: os.remove(local)
    except: pass
    respondidos.add(msg.id)

# ==================== MUDO ====================

def cmd_mudo(cl, thread_id, msg, respondidos):
    reply = getattr(msg, "reply", None)
    if not reply:
        responder(cl, thread_id, bloco("MUDO", ["❌ Responda um vídeo com /mudo"]))
        respondidos.add(msg.id)
        return

    url, tipo = pegar_midia(reply)
    if not url or tipo != "video":
        responder(cl, thread_id, bloco("MUDO", "❌ Só funciona com vídeo."))
        respondidos.add(msg.id)
        return

    responder(cl, thread_id, bloco("MUDO", "🔄 Removendo áudio..."))

    local = baixar_url(url, ".mp4")
    if not local:
        responder(cl, thread_id, bloco("MUDO", "❌ Não consegui baixar."))
        respondidos.add(msg.id)
        return

    saida = silenciar(local)

    if saida and os.path.exists(saida):
        try:
            cl.direct_send_video(saida, thread_ids=[thread_id])
            responder(cl, thread_id, bloco("MUDO", "✅ Áudio removido!"))
        except Exception as e:
            responder(cl, thread_id, bloco("MUDO", f"❌ Erro: {e}"))
        finally:
            try: os.remove(saida)
            except: pass
    else:
        responder(cl, thread_id, bloco("MUDO", "❌ Falha ao processar."))

    try: os.remove(local)
    except: pass
    respondidos.add(msg.id)