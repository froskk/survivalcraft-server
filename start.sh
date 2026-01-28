#!/bin/bash

# Configurável - Memória usada pelo servidor
MEMORY=${MEMORY:-2G}

# Inicia o servidor Minecraft
java -Xmx$MEMORY -jar paper-1.21.1.jar nogui
