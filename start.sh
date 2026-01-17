#!/bin/bash

# Survivalcraft Server Startup Script
# This script downloads and starts the Minecraft server

set -e

echo "========================================="
echo "Survivalcraft Server - Startup Script"
echo "========================================="

# Create necessary directories
mkdir -p server
mkdir -p plugins
mkdir -p world
mkdir -p logs

cd server

# Download Paper server JAR (latest 1.21)
if [ ! -f "paper-1.21.jar" ]; then
    echo "Downloading Paper 1.21 server..."
    curl -L -o paper-1.21.jar "https://api.papermc.io/v2/projects/paper/versions/1.21.1/builds/128/downloads/paper-1.21.1-128.jar" || {
        echo "Error downloading Paper server. Trying alternative source..."
        wget -O paper-1.21.jar "https://papermc.io/api/v2/projects/paper/versions/1.21.1/builds/128/downloads/paper-1.21.1-128.jar"
    }
fi

# Download Geyser plugin
if [ ! -f "../plugins/Geyser-Spigot.jar" ]; then
    echo "Downloading Geyser plugin..."
    curl -L -o "../plugins/Geyser-Spigot.jar" "https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/Geyser-Spigot.jar" || {
        echo "Error downloading Geyser. Trying alternative..."
        wget -O "../plugins/Geyser-Spigot.jar" "https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/Geyser-Spigot.jar"
    }
fi

# Download Floodgate plugin
if [ ! -f "../plugins/floodgate-spigot.jar" ]; then
    echo "Downloading Floodgate plugin..."
    curl -L -o "../plugins/floodgate-spigot.jar" "https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/floodgate-spigot.jar" || {
        echo "Error downloading Floodgate. Trying alternative..."
        wget -O "../plugins/floodgate-spigot.jar" "https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/floodgate-spigot.jar"
    }
fi

# Download HeadDrop plugin (for player heads on death)
if [ ! -f "../plugins/HeadDrop.jar" ]; then
    echo "Downloading HeadDrop plugin..."
    curl -L -o "../plugins/HeadDrop.jar" "https://hangar.papermc.io/vedokoush/HeadBounty/versions/latest/PAPER/download" || {
        echo "Note: HeadDrop plugin download failed. You may need to add it manually."
    }
fi

# Download LagFixer plugin
if [ ! -f "../plugins/LagFixer.jar" ]; then
    echo "Downloading LagFixer plugin..."
    curl -L -o "../plugins/LagFixer.jar" "https://cdn.modrinth.com/data/Yd7qDQc7/versions/latest/download" || {
        echo "Note: LagFixer plugin download failed. You may need to add it manually."
    }
fi

# Copy configuration files
echo "Copying configuration files..."
cp ../server.properties ./ || echo "server.properties not found"
cp ../geyser-config.yml ../plugins/ || echo "geyser-config.yml not found"
cp ../floodgate-config.yml ../plugins/ || echo "floodgate-config.yml not found"
cp ../paper-global.yml ../config/ || echo "paper-global.yml not found"
cp ../ops.json ./ || echo "ops.json not found"
cp ../whitelist.json ./ || echo "whitelist.json not found"

# Accept EULA
echo "eula=true" > eula.txt

# Start the server with optimized JVM arguments
echo "Starting Survivalcraft server..."
java -Xmx28G -Xms28G \
    -XX:+UseG1GC \
    -XX:MaxGCPauseMillis=200 \
    -XX:+UnlockExperimentalVMOptions \
    -XX:G1NewCollectionPercentage=30 \
    -XX:G1MaxNewGenPercent=40 \
    -XX:InitiatingHeapOccupancyPercent=35 \
    -XX:+DisableExplicitGC \
    -XX:+AlwaysPreTouch \
    -XX:+ParallelRefProcEnabled \
    -Dusing.aikars.flags=true \
    -jar paper-1.21.jar nogui

