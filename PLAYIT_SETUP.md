# 🎮 Configuração Survivalcraft com playit.gg

## ✅ Servidor Pronto!

Seu servidor **Survivalcraft** está configurado e pronto para usar com **playit.gg**!

---

## 🚀 Como Conectar

### Opção 1: Usando playit.gg (Recomendado)

**playit.gg** é um serviço gratuito que cria um túnel para seu servidor sem precisar de CAPTCHA.

#### Passo 1: Criar Conta no playit.gg

1. Vá para https://playit.gg/
2. Clique em **"Login"** (canto superior direito)
3. Clique em **"Use Guest Account"** (para não precisar de email)
4. Você será redirecionado para o dashboard

#### Passo 2: Configurar o Servidor

1. No dashboard, clique em **"Agents"**
2. Clique em **"Setup a new agent"**
3. Clique em **"Yes, it's running"**
4. Clique em **"here"** para obter o código de claim
5. Copie o **código de claim** que aparece na tela

#### Passo 3: Adicionar o Token ao GitHub

1. Vá para seu repositório: https://github.com/froskk/survivalcraft-server
2. Clique em **Settings** → **Secrets and variables** → **Actions**
3. Clique em **"New repository secret"**
4. Preencha:
   - **Name**: `PLAYIT_CLAIM_TOKEN`
   - **Secret**: Cole o código de claim que você copiou
5. Clique em **"Add secret"**

#### Passo 4: Iniciar o Servidor

1. Vá para https://github.com/froskk/survivalcraft-server/actions
2. Clique em **"Survivalcraft Server - playit.gg 24/7"**
3. Clique em **"Run workflow"**
4. Selecione **"main"**
5. Clique em **"Run workflow"**

#### Passo 5: Obter o Endereço

1. Aguarde o workflow começar
2. Vá para o dashboard do playit.gg
3. Você verá um endereço como: `survivalcraft.at.ply.gg`
4. Anote esse endereço!

---

## 🎮 Conectando ao Servidor

### Java Edition

1. Abra **Minecraft Java Edition**
2. Clique em **"Multiplayer"**
3. Clique em **"Add Server"**
4. Preencha:
   - **Server Name**: `Survivalcraft`
   - **Server Address**: `seu-endereco.at.ply.gg:25565`
5. Clique em **"Done"**
6. Clique em **"Join Server"**

### Bedrock Edition

1. Abra **Minecraft Bedrock Edition**
2. Vá para **"Play"**
3. Clique em **"Friends"**
4. Clique em **"Add Server"**
5. Preencha:
   - **Server Name**: `Survivalcraft`
   - **Server Address**: `seu-endereco.at.ply.gg`
   - **Port**: `19132`
6. Clique em **"Save"**
7. Clique em **"Join Server"**

---

## 📊 Informações do Servidor

| Informação | Valor |
|-----------|-------|
| **Nome** | Survivalcraft |
| **Versão** | Paper 1.21.1 |
| **Modo** | Offline (Pirata) |
| **Localização** | São Paulo, Brasil 🇧🇷 |
| **Máximo de Jogadores** | 20 |
| **Porta Java** | 25565 |
| **Porta Bedrock** | 19132 |
| **Donos** | N0vakt e froskk |
| **Whitelist** | Desativada |
| **PvP** | Ativado |

---

## 🎛️ Comandos Úteis

### Gerenciamento de Jogadores

```
/op <jogador>              # Tornar jogador OP
/deop <jogador>            # Remover OP
/ban <jogador>             # Banir jogador
/unban <jogador>           # Desbanir jogador
/kick <jogador>            # Expulsar jogador
```

### Gerenciamento do Servidor

```
/save-all                  # Salvar mundo
/stop                      # Parar servidor
/say <mensagem>            # Mensagem global
/time set <hora>           # Mudar hora
/weather <clear|rain>      # Mudar clima
```

### Informações

```
/list                      # Listar jogadores
/seed                      # Ver seed do mundo
/difficulty                # Ver dificuldade
```

---

## ⚙️ Configurações Aplicadas

✅ **Modo Offline** - Aceita qualquer nome de usuário
✅ **Crossplay** - Java e Bedrock juntos
✅ **Otimização** - Configurado para melhor performance
✅ **São Paulo** - Otimizado para jogadores brasileiros
✅ **24/7** - Reinicia automaticamente a cada 6 horas
✅ **Sem Whitelist** - Qualquer um pode entrar

---

## 🌐 Endereço de Conexão

Assim que você configurar o playit.gg, você receberá um endereço como:

```
survivalcraft-XXXXX.at.ply.gg
```

**Use este endereço para conectar ao servidor!**

---

## 📞 Troubleshooting

### Não consigo conectar

1. Verifique se o workflow está em execução
2. Verifique se o playit.gg está ativo no dashboard
3. Tente novamente em alguns minutos
4. Verifique o firewall

### Bedrock não conecta

1. Tente usar a porta 19132
2. Verifique se o Geyser está carregado
3. Reinicie o servidor

### Lag alto

1. Reduza a distância de visualização
2. Reduza o número máximo de jogadores
3. Reinicie o servidor

---

## 📁 Arquivos Importantes

- **Repositório**: https://github.com/froskk/survivalcraft-server
- **Workflow**: `.github/workflows/minecraft-playit-final.yml`
- **Configuração**: `server.properties`
- **OPs**: `ops.json`

---

## 🎉 Pronto!

Seu servidor **Survivalcraft** está pronto para usar!

**Divirta-se!** 🚀🎮

---

**Criado em**: 17 de Janeiro de 2026
**Localização**: São Paulo, Brasil 🇧🇷
**Versão**: 1.21.1 (Paper)
