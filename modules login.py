import os
from instagrapi import Client
from instagrapi.exceptions import ChallengeRequired
from modules.banner import log_ok, log_erro, log_info

def fazer_login(cl: Client, username, password, sessionid, session_file):
    if os.path.exists(session_file):
        try:
            cl.load_settings(session_file)
            cl.login(username, password)
            log_ok("Sessão restaurada")
            return True
        except Exception as e:
            log_info(f"Sessão expirada: {e}")
            try: os.remove(session_file)
            except: pass

    try:
        if sessionid:
            cl.login_by_sessionid(sessionid)
            log_ok("Logado via sessionid")
        else:
            cl.login(username, password)
            log_ok("Logado via senha")
        cl.dump_settings(session_file)
        return True
    except ChallengeRequired:
        log_erro("Instagram pediu verificação. Resolva manualmente no app.")
        return False
    except Exception as e:
        log_erro(f"Erro no login: {e}")
        return False