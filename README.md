# Survivalcraft - Minecraft Server

Um servidor de Minecraft com suporte para **Java Edition** e **Bedrock Edition** (crossplay), otimizado para performance e com mods especiais.

## 🎮 Características

- **Crossplay Java & Bedrock**: Jogadores de Java Edition e Bedrock Edition podem jogar juntos
- **Otimização de Lag**: Configurações otimizadas do PaperMC e plugins de performance
- **Mod de Cabeças**: Jogadores dropam suas cabeças ao morrer
- **24/7**: Servidor rodando continuamente
- **Donos**: N0vakt e você têm acesso total de administrador

## 📋 Requisitos

- Java 21 ou superior
- 28GB de RAM (configurável)
- Conexão com a internet estável

## 🚀 Instalação Rápida

### Opção 1: Script Automático

```bash
chmod +x start.sh
./start.sh
```

O script irá:
1. Criar os diretórios necessários
2. Baixar o servidor Paper 1.21
3. Baixar os plugins (Geyser, Floodgate, HeadDrop, LagFixer)
4. Copiar as configurações
5. Iniciar o servidor

### Opção 2: Manual

1. Baixe o Paper 1.21 de https://papermc.io/
2. Coloque o JAR na pasta `server/`
3. Baixe os plugins:
   - Geyser: https://download.geysermc.org/
   - Floodgate: https://download.geysermc.org/
   - HeadDrop: https://hangar.papermc.io/
   - LagFixer: https://modrinth.com/
4. Coloque os JARs na pasta `plugins/`
5. Execute: `java -Xmx28G -Xms28G -jar paper-1.21.jar nogui`

## 📁 Estrutura de Arquivos

```
survivalcraft-server/
├── server/                    # Pasta do servidor
│   ├── paper-1.21.jar        # Servidor Paper
│   ├── server.properties      # Configurações do servidor
│   ├── eula.txt              # Aceitar EULA
│   ├── ops.json              # Donos do servidor
│   └── whitelist.json        # Lista branca
├── plugins/                   # Pasta de plugins
│   ├── Geyser-Spigot.jar     # Plugin de crossplay
│   ├── floodgate-spigot.jar  # Autenticação Bedrock
│   ├── HeadDrop.jar          # Plugin de cabeças
│   └── LagFixer.jar          # Plugin de otimização
├── world/                     # Pasta do mundo
├── logs/                      # Pasta de logs
├── server.properties          # Configurações principais
├── geyser-config.yml          # Configuração do Geyser
├── floodgate-config.yml       # Configuração do Floodgate
├── paper-global.yml           # Configuração de performance
├── ops.json                   # Donos (N0vakt)
├── whitelist.json             # Lista branca
├── start.sh                   # Script de inicialização
└── README.md                  # Este arquivo
```

## 🔌 Conexão ao Servidor

### Java Edition
- **Endereço**: `localhost:25565` (local) ou seu domínio/IP público
- **Porta**: `25565`

### Bedrock Edition
- **Endereço**: `localhost` (local) ou seu domínio/IP público
- **Porta**: `19132`

## ⚙️ Configurações Principais

### server.properties
- **Modo de Jogo**: Survival
- **Dificuldade**: Normal
- **PvP**: Ativado
- **Máximo de Jogadores**: 20
- **Distância de Visualização**: 10 chunks
- **Distância de Simulação**: 8 chunks

### Plugins Instalados

#### Geyser + Floodgate
Permite que jogadores de Bedrock Edition se conectem ao servidor Java Edition.

#### HeadDrop
Quando um jogador morre, sua cabeça é dropada no chão. Pode ser coletada e colocada como decoração.

#### LagFixer
Otimiza o servidor para reduzir lag:
- Otimização de chunk loading
- Otimização de entidades
- Otimização de redstone
- Otimização de partículas

## 🎛️ Comandos Úteis

### Gerenciamento de Donos
```
/op N0vakt              # Tornar N0vakt dono
/deop <jogador>         # Remover dono
/whitelist add <nome>   # Adicionar à whitelist
/whitelist remove <nome> # Remover da whitelist
```

### Gerenciamento do Servidor
```
/save-all               # Salvar mundo
/stop                   # Parar servidor
/reload                 # Recarregar configurações
/say <mensagem>         # Enviar mensagem global
```

### Informações
```
/list                   # Listar jogadores online
/seed                   # Ver seed do mundo
/difficulty             # Ver dificuldade
```

## 🌐 Domínio e IP Público

Para acessar o servidor remotamente, você precisa de:

1. **IP Público**: Seu endereço IP externo (pode ser dinâmico)
2. **Domínio**: Opcional, mas recomendado para facilitar o acesso

### Opções de Domínio Gratuito
- **DuckDNS**: https://www.duckdns.org/ (atualiza IP dinâmico automaticamente)
- **No-IP**: https://www.noip.com/ (domínio dinâmico gratuito)

### Exemplo com DuckDNS
1. Crie uma conta em https://www.duckdns.org/
2. Crie um domínio (ex: `survivalcraft.duckdns.org`)
3. Configure o script de atualização com seu IP
4. Compartilhe `survivalcraft.duckdns.org:25565` com seus amigos

## 🔧 Otimizações de Performance

O servidor está configurado com:
- **JVM Flags Otimizadas**: G1GC com configurações de Aikar
- **Chunk Loading**: 4 chunks por tick
- **Entity Activation Range**: Otimizado para reduzir lag
- **Async Operations**: Carregamento assíncrono de chunks e entidades
- **Cache**: Sistema de cache para chunks e entidades

## 📊 Requisitos de Hardware

| Componente | Mínimo | Recomendado | Ideal |
|-----------|--------|-------------|-------|
| RAM | 8GB | 16GB | 28GB+ |
| CPU | 2 cores | 4 cores | 8+ cores |
| Armazenamento | 20GB SSD | 50GB SSD | 100GB+ SSD |
| Banda | 10 Mbps | 50 Mbps | 100+ Mbps |

## 🐛 Troubleshooting

### Servidor não inicia
- Verifique se Java 21+ está instalado: `java -version`
- Verifique se há espaço em disco
- Verifique os logs em `logs/`

### Lag alto
- Reduza a distância de visualização em `server.properties`
- Reduza o número máximo de jogadores
- Verifique a CPU e RAM disponível

### Bedrock não consegue conectar
- Verifique se a porta 19132 está aberta (UDP)
- Verifique se o Geyser está carregado: `/plugins`
- Verifique os logs do Geyser

### Problemas de autenticação
- Verifique se o Floodgate está carregado
- Reinicie o servidor
- Verifique o arquivo `floodgate-config.yml`

## 📝 Logs

Os logs do servidor são salvos em:
- `server/logs/latest.log` - Log mais recente
- `server/logs/` - Todos os logs

## 🔐 Segurança

- **Whitelist**: Ativada para controlar quem pode entrar
- **Firewall**: Configure seu firewall para permitir as portas 25565 (TCP) e 19132 (UDP)
- **Backup**: Faça backup regular da pasta `world/`

## 📞 Suporte

Para problemas ou dúvidas:
1. Verifique os logs
2. Consulte a documentação do Paper: https://docs.papermc.io/
3. Consulte a documentação do Geyser: https://wiki.geysermc.org/

## 📜 Licença

Este servidor usa:
- **Paper**: AGPL 3.0
- **Geyser**: MIT
- **Floodgate**: MIT
- **Plugins**: Verifique as licenças individuais

## 🎉 Divirta-se!

Bem-vindo ao Survivalcraft! Aproveite o servidor com seus amigos!

---

**Donos**: N0vakt e você
**Versão do Servidor**: Paper 1.21
**Última Atualização**: 17 de Janeiro de 2026
