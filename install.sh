if [ ! -d "venv" ]; then
    echo "Venv not found. Creating one with dependencies"
    python3 -m venv "venv"
    ./venv/bin/pip install discord
    ./venv/bin/pip install requests
fi

USER_HOME=$(eval echo ~$USER)

cat << 'EOF' > discord-bot.sh
#!/bin/bash
if [ "$1" = "wlo1" ] && [ "$2" = "up" ]; then
    cd "${PROJ_DIR}"
    ./venv/bin/python3 ipbot.py
fi
EOF

PROJ_DIR=$(pwd)
sed -i "s|\${PROJ_DIR}|$PROJ_DIR|g" discord-bot.sh

sudo chmod 755 discord-bot.sh
sudo chown root:root discord-bot.sh
sudo mv "${PROJ_DIR}/discord-bot.sh" /etc/NetworkManager/dispatcher.d/99-discord-bot.sh

