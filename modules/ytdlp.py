import os
import time
import subprocess
import config

def baixar_musica(query):
    """Baixa áudio do YouTube via yt-dlp. Retorna (path, título, thumb)."""
    try:
        ts = int(time.time())
        base = os.path.join(config.TEMP_DIR, f"yt_{ts}")
        subprocess.run([
            "yt-dlp",
            f"ytsearch:{query}",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            "-o", base + ".%(ext)s",
            "--no-playlist",
            "--no-warnings",
            "-q",
            "--write-thumbnail",
            "--convert-thumbnails", "jpg",
        ], capture_output=True, text=True, timeout=180)

        audio, thumb = None, None
        for ext in ["mp3", "m4a", "webm"]:
            p = f"{base}.{ext}"
            if os.path.exists(p):
                audio = p
                break
        for ext in ["jpg", "png", "webp"]:
            p = f"{base}.{ext}"
            if os.path.exists(p):
                thumb = p
                break

        if audio:
            return audio, query, thumb
        return None, None, None
    except Exception as e:
        print(f"Erro yt-dlp: {e}")
        return None, None, None