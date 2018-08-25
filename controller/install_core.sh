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

apt update && apt upgrade -y
apt install -y \
	git

# =============================
# Start der zusätzlichen Module:
# =============================
for m in "${modules[@]}"
do
	echo
	echo "=> Starte Modul $m"
	echo
done