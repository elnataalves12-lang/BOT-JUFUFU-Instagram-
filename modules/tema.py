LINHA = "│"
RODAPE = "─────  𝙹𝚄𝙵𝚄𝙵𝚄-ᶻᶻᶻ  ─────"

def bloco(titulo, linhas):
    """Monta resposta simples e bonita."""
    if isinstance(linhas, str):
        linhas = [linhas]

    topo = f"╭─────── ✦ {titulo} ✦ ───────╮"
    corpo = "\n".join(f"{LINHA}  {l}" for l in linhas)
    fim = "╰───────────────────────────╯"
    return f"{topo}\n{corpo}\n{fim}\n\n{RODAPE}"