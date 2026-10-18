import os
import time
import subprocess
import config

def duracao(path):
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
            capture_output=True, text=True
        )
        return float(r.stdout.strip())
    except:
        return 0.0

def converter_m4a(audio_path):
    ts = int(time.time())
    out = os.path.join(config.TEMP_DIR, f"voice_{ts}.m4a")
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", audio_path,
            "-c:a", "aac", "-profile:a", "aac_low",
            "-b:a", "128k", "-ar", "44100", "-ac", "2",
            out
        ], capture_output=True, check=True)
        return out
    except Exception as e:
        print(f"Erro m4a: {e}")
        return None

def montar_video(audio_path, fundo_img, dur):
    """Vídeo com fundo (thumbnail ou preto) + áudio."""
    ts = int(time.time())
    out = os.path.join(config.TEMP_DIR, f"vid_{ts}.mp4")

    if fundo_img and os.path.exists(fundo_img):
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", fundo_img,
            "-i", audio_path,
            "-t", str(dur),
            "-vf", "scale=720:720:force_original_aspect_ratio=decrease,"
                   "pad=720:720:(ow-iw)/2:(oh-ih)/2:black",
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-preset", "ultrafast", "-r", "1",
            "-c:a", "aac", "-b:a", "128k",
            "-shortest", out
        ]
    else:
        cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", "color=c=black:s=720x720:r=1",
            "-i", audio_path,
            "-t", str(dur),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "ultrafast",
            "-c:a", "aac", "-b:a", "128k",
            out
        ]

    try:
        subprocess.run(cmd, capture_output=True, check=True)
        return out
    except Exception as e:
        print(f"Erro vídeo: {e}")
        return None