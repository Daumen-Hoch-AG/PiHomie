#! /bin/bash

# Installation der Abhängigkeiten für PiHomie
# auf einem Raspian Stretch (Lite)

# Sudo Check:
if [ "$(whoami)" != "root" ]; then
	echo "Dieses Skript muss mit 'sudo' oder als 'root' ausgeführt werden !"
	exit 1
fi

echo
echo "=== PiHomie Basisinstalltion ==="
echo

echo "Module:"
echo "- Core"

# Zusätzliche Konfigurationsmodule können hier eingehängt werden:
modules=()


# =============================
# Start des Core-Moduls
# =============================

echo
echo "=> Starte Modul Core"
echo

addgroup pihomie
adduser --no-create-home --disabled-login --ingroup pihomie --gecos "" pihomie

git clone https://github.com/Daumen-Hoch-AG/PiHomie.git
chown pihomie:pihomie -R /opt/PiHomie

apt update && apt upgrade -y
apt install -y \
	git
	python3-pip

# =============================
# Start der zusätzlichen Module:
# =============================
for m in "${modules[@]}"
do
	echo
	echo "=> Starte Modul $m"
	echo
done