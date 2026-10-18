import os
import time
import subprocess
import requests
import config

def baixar_url(url, ext=".mp4"):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=60)
        if not r.ok:
            return None
        ts = int(time.time())
        path = os.path.join(config.TEMP_DIR, f"dm_{ts}{ext}")
        with open(path, "wb") as f:
            f.write(r.content)
        return path
    except:
        return None

def pegar_midia(msg):
    """Retorna (url, tipo) da mídia na mensagem."""
    try:
        media = getattr(msg, "media", None)
        if media:
            v = getattr(media, "video_url", None)
            if v:
                return v, "video"
            t = getattr(media, "thumbnail_url", None)
            if t:
                return t, "foto"
        return None, None
    except:
        return None, None

def cortar_quadrado(entrada, tamanho=512):
    """Corta o centro e deixa quadrado (não é figurinha, é recorte)."""
    ts = int(time.time())
    ext = os.path.splitext(entrada)[1].lower()
    saida = os.path.join(config.TEMP_DIR, f"crop_{ts}{ext}")

    try:
        if ext in (".mp4", ".mov", ".webm"):
            subprocess.run([
                "ffmpeg", "-y", "-i", entrada,
                "-vf", f"crop=min(iw\\,ih):min(iw\\,ih),scale={tamanho}:{tamanho}:flags=lanczos",
                "-c:v", "libx264", "-pix_fmt", "yuv420p",
                "-preset", "ultrafast", "-c:a", "aac",
                saida
            ], capture_output=True, check=True)
        else:
            from PIL import Image
            img = Image.open(entrada).convert("RGB")
            w, h = img.size
            lado = min(w, h)
            left = (w - lado) // 2
            top = (h - lado) // 2
            img = img.crop((left, top, left + lado, top + lado))
            img = img.resize((tamanho, tamanho), Image.LANCZOS)
            saida = os.path.join(config.TEMP_DIR, f"crop_{ts}.jpg")
            img.save(saida, "JPEG", quality=92)
        return saida
    except Exception as e:
        print(f"Erro cortar: {e}")
        return None

def silenciar(entrada):
    """Remove o áudio do vídeo."""
    ts = int(time.time())
    saida = os.path.join(config.TEMP_DIR, f"mudo_{ts}.mp4")
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", entrada,
            "-an", "-c:v", "copy",
            saida
        ], capture_output=True, check=True)
        return saida
    except Exception as e:
        print(f"Erro silenciar: {e}")
        return None