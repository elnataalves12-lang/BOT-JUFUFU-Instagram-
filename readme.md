🤖 JUFUFU-zzz — Bot para Instagram DM

<p align="center">
  <img src="file_00000000be08820e9946e6ddefd56f98.png" alt="JUFUFU-zzz Banner" width="100%">
</p>

<p align="center">
  <b>Bot gratuito para Instagram Direct</b> · Comandos de música, edição de mídia, brincadeiras e mais.
</p>

<p align="center">
  <a href="https://github.com/elnataalves12-lang/BOT-JUFUFU-zzz/tree/main">
    <img src="https://img.shields.io/badge/WhatsApp-Bot%20Gratuito-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp Bot">
  </a>
  <a href="https://whatsapp.com/channel/0029VbDHw0fAO7RBFTJ3rn1e">
    <img src="https://img.shields.io/badge/Canal%20Oficial-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="Canal">
  </a>
  <a href="https://wa.me/5591985500390">
    <img src="https://img.shields.io/badge/Desenvolvedor-Contato-FFB300?style=for-the-badge&logo=whatsapp&logoColor=black" alt="Contato">
  </a>
</p>

---

⚠️ AVISO IMPORTANTE — LEIA ANTES DE USAR

Este bot usa a API privada do Instagram (instagrapi), que NÃO é oficial.

Isso significa que o Instagram pode detectar o uso, bloquear temporariamente ou banir permanentemente a conta que estiver rodando o bot. Use por sua conta e risco.

O desenvolvedor não se responsabiliza por contas banidas, perdidas ou bloqueadas. O bot é 100% gratuito e entregue no estado em que se encontra ("as is"), sem garantias.

🛡️ Como reduzir (muito) o risco de ban

Siga estas recomendações antes de colocar o bot pra rodar:

1. NUNCA use sua conta principal. Use uma conta secundária, velha, que você não usa mais — ou crie uma nova.
2. Se criar uma conta nova, "aqueça" ela antes.
   · Deixe a conta parada por 3 a 7 dias.
   · Depois, use manualmente por mais alguns dias: assista Reels, curta vídeos, comente, siga pessoas, mande mensagens para amigos.
   · Isso cria um "histórico humano" que reduz drasticamente a chance de o Instagram achar que é bot.
3. Não rode o bot 24h no primeiro dia. Comece com poucas horas, aumente aos poucos.
4. Não use o bot para spam. Mandar a mesma mensagem para dezenas de pessoas é o caminho mais rápido para o ban.
5. Se aparecer ChallengeRequired, pare o bot imediatamente e resolva a verificação manualmente no app do Instagram.

💡 Regra de ouro: conta nova + bot rodando direto = ban quase garantido. Conta velha + uso humano + bot = risco baixo.

---

✨ Comandos disponíveis

Comando O que faz
/menu Mostra o menu com imagem
/play <música> Baixa do YouTube e envia como áudio (≤60s) ou vídeo (>60s)
/corta (responder mídia) Recorta o centro da foto/vídeo e deixa quadrado 512x512
/mudo (responder vídeo) Remove o áudio do vídeo
/ping Mostra status do bot
/perfil Perfil de brincadeira
/id Mostra seu ID e o ID da conversa
/dado Rola um dado (1–6)
/moeda Cara ou coroa

Todos os comandos aceitam os prefixos !, / ou . (editável em config.py).

---

📦 Instalação completa (Termux)

1. Instalar dependências do sistema

```bash
pkg update && pkg upgrade -y
pkg install python ffmpeg git nodejs -y
```

O nodejs é necessário para o yt-dlp funcionar bem com o YouTube.
O ffmpeg é necessário para converter áudio/vídeo.

2. Instalar dependências do Python

```bash
pip install instagrapi requests pillow colorama yt-dlp
```

3. Baixar o projeto

```bash
cd ~
git clone https://github.com/SEU-USUARIO/jufufu-bot.git
cd jufufu-bot
```

4. Editar o config.py

```bash
nano config.py
```

Preencha:

· USERNAME — usuário da conta do bot
· PASSWORD — senha da conta
· BOT_NOME — nome que aparece no banner
· MENU_IMAGE_URL — link da imagem do menu

Salve com Ctrl+O, Enter, Ctrl+X.

5. Rodar o bot

```bash
python bot.py
```

Na primeira execução, o Instagram pode pedir um código de verificação. Digite o código de 6 dígitos que chegar no e-mail/telefone da conta e pressione Enter. A sessão fica salva em jufufu_session.json — nas próximas vezes não precisa digitar de novo.

---

🔧 Solução de problemas

Erro Solução
ModuleNotFoundError: No module named 'X' Falta instalar o pacote: pip install X
IndentationError Abra o arquivo no nano e confira se há tabs misturados com espaços. Use só espaços.
Invalid sessionid Delete jufufu_session.json e rode de novo.
ChallengeRequired Resolva a verificação manualmente no app do Instagram antes de rodar de novo.
direct_send_voice falha Normal. O Instagram descontinuou voice notes. O bot cai automaticamente para vídeo.
yt-dlp não baixa Instale o nodejs: pkg install nodejs -y
/corta não funciona O Instagram precisa que você responda a uma mídia (foto ou vídeo) com o comando.
Bot não responde Confira se você mandou o comando com prefixo (/, ! ou .) e se a conta não está em ChallengeRequired.

---

🌐 Links oficiais

 Link
🤖 Bot WhatsApp (gratuito) github.com/elnataalves12-lang/BOT-JUFUFU-zzz
📢 Canal oficial (WhatsApp) whatsapp.com/channel/0029VbDHw0fAO7RBFTJ3rn1e
💬 Contato do desenvolvedor +55 91 98550-0390

---

💛 Licença e gratuidade

Este projeto é 100% gratuito e open source. Você pode usar, modificar e compartilhar à vontade.

· ❌ Não venda o bot.
· ❌ Não remova os créditos do desenvolvedor.
· ✅ Compartilhe com quem quiser.
· ✅ Contribua com melhorias via pull request.

---

📌 Créditos

· Desenvolvedor: @elnataalves12-lang
· Biblioteca principal: instagrapi
· Download de mídia: yt-dlp
· Comunidade: todos os membros do canal oficial 💛

---

<p align="center">
  <b>Feito com 💛 pela comunidade JUFUFU-zzz</b><br>
  <i>Se este bot te ajudou, compartilha com os amigos e entra no canal!</i>
</p>

<p align="center">
  <a href="https://whatsapp.com/channel/0029VbDHw0fAO7RBFTJ3rn1e">
    <img src="https://img.shields.io/badge/Entrar%20no%20Canal-Oficial-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="Canal">
  </a>
</p>