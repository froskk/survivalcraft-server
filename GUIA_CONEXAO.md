# 🎮 Guia de Conexão - Servidor Survivalcraft

## 📍 Informações do Servidor

| Informação | Valor |
|-----------|-------|
| **Nome do Servidor** | Survivalcraft |
| **Versão** | Paper 1.21 |
| **Tipo** | Java + Bedrock (Crossplay) |
| **Donos** | N0vakt e você |
| **Repositório** | https://github.com/froskk/survivalcraft-server |
| **Status** | 24/7 no GitHub Actions |

---

## 🌐 Como Conectar ao Servidor

### ⚠️ IMPORTANTE: Configuração Necessária

Como o servidor está rodando no **GitHub Actions** (que é um ambiente de CI/CD), ele **não tem um IP público direto**. Para acessar o servidor remotamente, você precisa configurar um **túnel de rede**.

### Opção 1: Usando playit.gg (Recomendado)

**playit.gg** é um serviço gratuito que cria um túnel para seu servidor.

#### Passo 1: Criar conta no playit.gg
1. Acesse https://playit.gg/
2. Clique em "Sign Up"
3. Crie uma conta com seu email

#### Passo 2: Obter o token
1. Após criar a conta, vá para https://playit.gg/account/tokens
2. Clique em "Create Token"
3. Copie o token

#### Passo 3: Adicionar o token ao GitHub
1. Vá para https://github.com/froskk/survivalcraft-server/settings/secrets/actions
2. Clique em "New repository secret"
3. Nome: `PLAYIT_TOKEN`
4. Valor: Cole o token que você copiou
5. Clique em "Add secret"

#### Passo 4: Ativar o workflow
1. Vá para https://github.com/froskk/survivalcraft-server/actions
2. Clique no workflow "Survivalcraft Server 24/7"
3. Clique em "Run workflow"

Após alguns minutos, o servidor estará online e você receberá um endereço público no playit.gg!

### Opção 2: Usando ngrok

**ngrok** também oferece um serviço gratuito de tunelamento.

#### Passo 1: Criar conta no ngrok
1. Acesse https://ngrok.com/
2. Clique em "Sign Up"
3. Crie uma conta

#### Passo 2: Obter o token
1. Após criar a conta, vá para https://dashboard.ngrok.com/get-started/your-authtoken
2. Copie seu token de autenticação

#### Passo 3: Adicionar o token ao GitHub
1. Vá para https://github.com/froskk/survivalcraft-server/settings/secrets/actions
2. Clique em "New repository secret"
3. Nome: `NGROK_AUTHTOKEN`
4. Valor: Cole o token que você copiou
5. Clique em "Add secret"

#### Passo 4: Ativar o workflow
1. Vá para https://github.com/froskk/survivalcraft-server/actions
2. Clique no workflow "Survivalcraft Server 24/7"
3. Clique em "Run workflow"

---

## 🎮 Conectando ao Servidor

### Java Edition

1. Abra o Minecraft Java Edition
2. Clique em "Multiplayer"
3. Clique em "Add Server"
4. Preencha:
   - **Server Name**: Survivalcraft
   - **Server Address**: `seu-endereco-publico:25565`
   
   (Substitua `seu-endereco-publico` pelo endereço que você recebeu do playit.gg ou ngrok)

5. Clique em "Done"
6. Clique em "Join Server"

### Bedrock Edition

1. Abra o Minecraft Bedrock Edition
2. Vá para "Play"
3. Clique em "Friends"
4. Clique em "Add Server"
5. Preencha:
   - **Server Name**: Survivalcraft
   - **Server Address**: `seu-endereco-publico`
   - **Port**: `19132`
   
   (Substitua `seu-endereco-publico` pelo endereço que você recebeu do playit.gg ou ngrok)

6. Clique em "Save"
7. Clique em "Join Server"

---

## 🔑 Credenciais de Acesso

| Jogador | Tipo | Permissão |
|---------|------|-----------|
| N0vakt | OP (Operador) | Controle total |
| Você | OP (Operador) | Controle total |

**Como usar comandos de OP:**
- `/op <nome-do-jogador>` - Tornar um jogador OP
- `/deop <nome-do-jogador>` - Remover OP de um jogador
- `/whitelist add <nome-do-jogador>` - Adicionar à whitelist
- `/whitelist remove <nome-do-jogador>` - Remover da whitelist

---

## 📊 Especificações do Servidor

### Hardware
- **RAM**: 28GB
- **CPU**: 4 cores
- **Armazenamento**: SSD (GitHub Actions)

### Software
- **Servidor**: Paper 1.21
- **Java**: OpenJDK 21
- **Plugins**:
  - **Geyser**: Permite conexão de Bedrock Edition
  - **Floodgate**: Autenticação para Bedrock
  - **HeadDrop**: Jogadores dropam cabeças ao morrer
  - **LagFixer**: Otimização de performance

### Configurações de Jogo
- **Modo**: Survival
- **Dificuldade**: Normal
- **PvP**: Ativado
- **Máximo de Jogadores**: 20
- **Distância de Visualização**: 10 chunks
- **Distância de Simulação**: 8 chunks

---

## 🎯 Comandos Úteis

### Gerenciamento de Jogadores
```
/op <jogador>              # Tornar jogador OP
/deop <jogador>            # Remover OP
/whitelist add <jogador>   # Adicionar à whitelist
/whitelist remove <jogador> # Remover da whitelist
/ban <jogador>             # Banir jogador
/unban <jogador>           # Desbanir jogador
/kick <jogador>            # Expulsar jogador
```

### Gerenciamento do Servidor
```
/save-all                  # Salvar mundo
/stop                      # Parar servidor
/reload                    # Recarregar configurações
/say <mensagem>            # Enviar mensagem global
/time set <hora>           # Mudar hora do dia
/weather <clear|rain|thunder> # Mudar clima
```

### Informações
```
/list                      # Listar jogadores online
/seed                      # Ver seed do mundo
/difficulty                # Ver dificuldade
/gamemode <modo> <jogador> # Mudar modo de jogo
/tp <jogador1> <jogador2>  # Teleportar jogador
```

### Mod de Cabeças
```
/give @s player_head{SkullOwner:"<nome-do-jogador>"} # Dar cabeça de um jogador
```

---

## 🚀 Iniciando o Workflow

### Método 1: Automático (Recomendado)
O workflow inicia automaticamente:
- A cada 6 horas (para manter o servidor online)
- Quando você faz push no repositório
- Manualmente (você clica em "Run workflow")

### Método 2: Manual
1. Vá para https://github.com/froskk/survivalcraft-server/actions
2. Clique em "Survivalcraft Server 24/7"
3. Clique em "Run workflow"
4. Selecione a branch "main"
5. Clique em "Run workflow"

---

## 📈 Monitorando o Servidor

### Ver Logs do Workflow
1. Vá para https://github.com/froskk/survivalcraft-server/actions
2. Clique no workflow em execução
3. Clique em "minecraft-server"
4. Veja os logs em tempo real

### Fazer Download de Backups
1. Vá para https://github.com/froskk/survivalcraft-server/actions
2. Clique no workflow que completou
3. Vá para "Artifacts"
4. Faça download de:
   - `server-logs` - Logs do servidor
   - `world-backup` - Backup do mundo

---

## 🐛 Troubleshooting

### Problema: Não consigo conectar ao servidor

**Solução:**
1. Verifique se o workflow está em execução: https://github.com/froskk/survivalcraft-server/actions
2. Verifique se o túnel (playit.gg/ngrok) está ativo
3. Verifique o endereço e porta que você está usando
4. Tente novamente em alguns minutos

### Problema: Bedrock não consegue conectar

**Solução:**
1. Verifique se o Geyser está carregado (veja nos logs)
2. Tente usar a porta 19132
3. Reinicie o workflow

### Problema: Lag alto

**Solução:**
1. Reduza a distância de visualização em `server.properties`
2. Reduza o número máximo de jogadores
3. Reinicie o servidor

### Problema: Servidor desligou

**Solução:**
1. O GitHub Actions tem limite de 6 horas por workflow
2. O workflow reinicia automaticamente a cada 6 horas
3. Você também pode iniciar manualmente clicando em "Run workflow"

---

## 📝 Arquivos Importantes

| Arquivo | Descrição |
|---------|-----------|
| `server.properties` | Configurações principais do servidor |
| `geyser-config.yml` | Configuração do Geyser (Bedrock) |
| `floodgate-config.yml` | Configuração do Floodgate (autenticação) |
| `paper-global.yml` | Otimizações de performance |
| `ops.json` | Lista de OPs (N0vakt) |
| `whitelist.json` | Lista branca de jogadores |
| `.github/workflows/minecraft-server.yml` | Workflow do GitHub Actions |

---

## 🔒 Segurança

- **Whitelist**: Ativada (apenas jogadores autorizados podem entrar)
- **Firewall**: Configure seu firewall para permitir as portas 25565 (TCP) e 19132 (UDP)
- **Backup**: Backups automáticos são feitos a cada workflow
- **Logs**: Todos os logs são salvos e podem ser auditados

---

## 📞 Suporte

Para problemas ou dúvidas:
1. Verifique os logs do workflow no GitHub Actions
2. Consulte a documentação do Paper: https://docs.papermc.io/
3. Consulte a documentação do Geyser: https://wiki.geysermc.org/

---

## 🎉 Pronto!

Seu servidor **Survivalcraft** está pronto para usar! Compartilhe o endereço do servidor com seus amigos e aproveite o jogo!

**Divirta-se!** 🎮

---

**Última atualização**: 17 de Janeiro de 2026
**Versão**: 1.0
