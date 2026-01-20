#!/bin/bash

# Script de Instalação e Configuração do Servidor Survivalcraft para AWS EC2
# Autor: Manus AI
# Data: 2026-01-19

# --- Variáveis de Configuração ---
REPO_URL="https://github.com/froskk/survivalcraft-server.git"
SERVER_DIR="/home/ubuntu/survivalcraft-server"
PAPER_URL="https://api.papermc.io/v2/projects/paper/versions/1.21.1/builds/128/downloads/paper-1.21.1-128.jar"
PAPER_JAR="paper.jar"
GEYSER_URL="https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/Geyser-Spigot.jar"
FLOODGATE_URL="https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/Floodgate-Spigot.jar"
HEAD_DROP_URL="https://github.com/Andre601/HeadDrop/releases/download/v1.0.0/HeadDrop-1.0.0.jar" # Exemplo de plugin HeadDrop
SWAP_SIZE="4G" # 4GB de Swap para compensar 1GB de RAM

echo "====================================================="
echo "  Survivalcraft Server - Instalação Automatizada AWS "
echo "====================================================="

# 1. Atualizar o sistema e instalar dependências
echo "1. Atualizando o sistema e instalando dependências..."
sudo apt update -y
sudo apt install -y openjdk-21-jdk git screen

# 2. Configurar Swap Memory (essencial para instâncias com pouca RAM)
echo "2. Configurando Swap Memory de $SWAP_SIZE..."
if [ ! -f /swapfile ]; then
    sudo fallocate -l $SWAP_SIZE /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
    echo "Swap configurado com sucesso."
else
    echo "Swapfile já existe. Pulando configuração."
fi

# 3. Clonar o repositório GitHub
echo "3. Clonando o repositório GitHub..."
if [ -d "$SERVER_DIR" ]; then
    echo "Diretório $SERVER_DIR já existe. Removendo e clonando novamente."
    rm -rf "$SERVER_DIR"
fi
git clone "$REPO_URL" "$SERVER_DIR"
cd "$SERVER_DIR"

# 4. Baixar o PaperMC
echo "4. Baixando PaperMC 1.21.1..."
curl -L -o "$PAPER_JAR" "$PAPER_URL"

# 5. Baixar Plugins
echo "5. Baixando Plugins (Geyser, Floodgate, HeadDrop)..."
mkdir -p plugins
curl -L -o "plugins/Geyser-Spigot.jar" "$GEYSER_URL"
curl -L -o "plugins/floodgate-spigot.jar" "$FLOODGATE_URL"
curl -L -o "plugins/HeadDrop.jar" "$HEAD_DROP_URL"

# 6. Configurações Finais
echo "6. Aplicando configurações finais..."
echo "eula=true" > eula.txt
chmod +x start.sh

# 7. Criar script de inicialização (start.sh)
echo "7. Criando script de inicialização (start.sh)..."
cat > start.sh << EOF
#!/bin/bash
java -Xmx1G -Xms1G -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -jar $PAPER_JAR nogui
EOF
chmod +x start.sh

# 8. Instruções de Execução
echo "====================================================="
echo "✓ Instalação concluída!"
echo "Para iniciar o servidor, execute:"
echo "cd $SERVER_DIR"
echo "screen -S minecraft ./start.sh"
echo ""
echo "Para sair da sessão do screen (manter o servidor rodando), pressione Ctrl+A, depois D."
echo "Para retornar à sessão, execute: screen -r minecraft"
echo "====================================================="
