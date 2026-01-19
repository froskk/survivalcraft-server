#!/usr/bin/env python3
"""
Survivalcraft Server Shield (Blindagem)
Impede que o servidor desligue e o reinicia instantaneamente se tentar encerrar
"""

import os
import sys
import subprocess
import time
import socket
import signal
import threading
from pathlib import Path
from datetime import datetime

# Configurações
SERVER_DIR = Path(__file__).parent
JAVA_PATH = "/usr/lib/jvm/java-21-openjdk-amd64/bin/java"
SERVER_JAR = SERVER_DIR / "paper-1.21.1.jar"
SERVER_PORT = 25565
MEMORY = "2G"
LOG_FILE = SERVER_DIR / "shield.log"
EULA_FILE = SERVER_DIR / "eula.txt"
SERVER_PROPERTIES = SERVER_DIR / "server.properties"

# Variáveis globais
server_process = None
shield_active = True
restart_count = 0
last_restart_time = 0

def log_message(message):
    """Registra mensagem com timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_text = f"[{timestamp}] {message}"
    print(log_text)
    
    try:
        with open(LOG_FILE, "a") as f:
            f.write(log_text + "\n")
    except:
        pass

def setup_server():
    """Configura o servidor inicialmente"""
    log_message("[*] Configurando servidor...")
    
    # EULA
    if not EULA_FILE.exists():
        EULA_FILE.write_text("eula=true\n")
        log_message("[✓] EULA aceito")
    
    # server.properties
    if not SERVER_PROPERTIES.exists():
        properties = """server-name=Survivalcraft
server-port=25565
server-ip=0.0.0.0
online-mode=false
gamemode=survival
difficulty=2
max-players=20
pvp=true
enable-command-blocks=true
spawn-protection=0
motd=§6Survivalcraft §e- §bSao Paulo, Brasil
level-name=world
enable-rcon=false
query.port=25565
enable-query=true
view-distance=10
simulation-distance=8
network-compression-threshold=256
max-tick-time=60000"""
        SERVER_PROPERTIES.write_text(properties)
        log_message("[✓] server.properties criado")
    
    # Baixa Paper se necessário
    if not SERVER_JAR.exists():
        log_message("[*] Baixando Paper 1.21.1...")
        try:
            subprocess.run([
                "curl", "-L", "-o", str(SERVER_JAR),
                "https://api.papermc.io/v2/projects/paper/versions/1.21.1/builds/128/downloads/paper-1.21.1-128.jar"
            ], check=True, timeout=300, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            log_message("[✓] Paper baixado")
        except Exception as e:
            log_message(f"[✗] Erro ao baixar Paper: {e}")
            return False
    
    return True

def is_server_running():
    """Verifica se o servidor está respondendo"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', SERVER_PORT))
        sock.close()
        return result == 0
    except:
        return False

def start_server():
    """Inicia o servidor Minecraft"""
    global server_process, restart_count, last_restart_time
    
    # Evita reinicializações muito rápidas (mínimo 2 segundos entre tentativas)
    now = time.time()
    if now - last_restart_time < 2:
        time.sleep(2 - (now - last_restart_time))
    
    restart_count += 1
    last_restart_time = time.time()
    
    log_message(f"[*] Iniciando servidor (reinicialização #{restart_count})...")
    
    cmd = [
        JAVA_PATH,
        f"-Xmx{MEMORY}",
        f"-Xms{MEMORY}",
        "-XX:+UseG1GC",
        "-XX:MaxGCPauseMillis=200",
        "-XX:+UnlinkSymbolsOnError",
        "-XX:G1NewCollectionHeuristicPercent=30",
        "-XX:G1ReservePercent=20",
        "-XX:G1HeapRegionSize=32M",
        "-XX:+ParallelRefProcEnabled",
        "-XX:MaxGCPauseMillis=200",
        "-jar",
        str(SERVER_JAR),
        "nogui"
    ]
    
    try:
        server_process = subprocess.Popen(
            cmd,
            cwd=str(SERVER_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        log_message(f"[✓] Servidor iniciado (PID: {server_process.pid})")
        return True
    except Exception as e:
        log_message(f"[✗] Erro ao iniciar servidor: {e}")
        return False

def monitor_server_output():
    """Monitora a saída do servidor em background"""
    global server_process
    
    if not server_process:
        return
    
    try:
        for line in server_process.stdout:
            log_message(f"[SERVER] {line.rstrip()}")
    except:
        pass

def shield_loop():
    """Loop principal de proteção (Shield)"""
    global server_process, shield_active
    
    log_message("[✓] SHIELD ATIVADO - Servidor protegido contra desligamentos!")
    
    check_interval = 2  # Verifica a cada 2 segundos
    
    while shield_active:
        try:
            time.sleep(check_interval)
            
            # Verifica se o processo ainda está rodando
            if server_process and server_process.poll() is not None:
                log_message("[!] ⚠️ ALERTA: Processo do servidor encerrou!")
                log_message("[!] 🛡️ SHIELD ATIVADO: Reiniciando servidor IMEDIATAMENTE...")
                
                time.sleep(1)
                if not start_server():
                    log_message("[✗] Falha ao reiniciar - tentando novamente...")
                    time.sleep(2)
                    start_server()
                
                # Aguarda o servidor iniciar
                for i in range(60):
                    if is_server_running():
                        log_message("[✓] Servidor voltou online!")
                        break
                    time.sleep(1)
            
            # Verifica se o servidor está respondendo
            elif not is_server_running():
                log_message("[!] ⚠️ ALERTA: Servidor não está respondendo!")
                log_message("[!] 🛡️ SHIELD ATIVADO: Tentando restaurar...")
                
                # Tenta matar e reiniciar o processo
                if server_process:
                    try:
                        server_process.terminate()
                        server_process.wait(timeout=5)
                    except:
                        server_process.kill()
                
                time.sleep(2)
                if not start_server():
                    log_message("[✗] Falha ao reiniciar - tentando novamente...")
                    time.sleep(2)
                    start_server()
            
            else:
                # Servidor está ok - log periódico
                pass
        
        except KeyboardInterrupt:
            break
        except Exception as e:
            log_message(f"[!] Erro no Shield: {e}")
            time.sleep(5)

def signal_handler(sig, frame):
    """Manipula sinais de interrupção"""
    global shield_active
    
    log_message("\n[!] Encerrando Shield...")
    shield_active = False
    
    if server_process:
        server_process.terminate()
        try:
            server_process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            server_process.kill()
    
    log_message("[✓] Shield encerrado")
    sys.exit(0)

def main():
    """Função principal"""
    log_message("=" * 70)
    log_message("🎮 Survivalcraft Server Shield (Blindagem)")
    log_message("=" * 70)
    log_message("[*] Este script impede que o servidor desligue")
    log_message("[*] Se o servidor tentar encerrar, será reiniciado IMEDIATAMENTE")
    log_message("=" * 70)
    
    # Registra manipulador de sinais
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Configuração inicial
    if not setup_server():
        log_message("[✗] Falha na configuração")
        sys.exit(1)
    
    # Inicia o servidor
    if not start_server():
        log_message("[✗] Falha ao iniciar servidor")
        sys.exit(1)
    
    # Aguarda o servidor iniciar completamente
    log_message("[*] Aguardando servidor iniciar...")
    for i in range(120):
        if is_server_running():
            log_message("[✓] Servidor está respondendo!")
            break
        time.sleep(1)
    
    # Inicia o loop de proteção em thread separada
    shield_thread = threading.Thread(target=shield_loop, daemon=False)
    shield_thread.start()
    
    # Monitora a saída do servidor
    try:
        monitor_server_output()
    except KeyboardInterrupt:
        signal_handler(None, None)

if __name__ == "__main__":
    main()
