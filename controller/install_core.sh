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
SCRIPT_PATH="`dirname \"$0\"`"
SCRIPT_PATH="`( cd \"$SCRIPT_PATH\" && pwd )`"
ROOT_PATH="`( cd \"$SCRIPT_PATH/..\" && pwd )`"


# =============================
# Start des Core-Moduls
# =============================

echo
echo "=> Starte Modul Core"
echo

# Pakete
apt update && apt upgrade -y
apt install -y \
	python3-flask python3-requests \
	apache2 libapache2-mod-wsgi-py3
apt autoremove -y


# Benutzer und Rechte für PiHomie
addgroup pihomie
adduser --no-create-home --disabled-login --ingroup pihomie --gecos "" pihomie
usermod -a -G www-data pihomie
chown pihomie:www-data -R $ROOT_PATH
cd $ROOT_PATH


# Konfigurationen

# -- Hostname
hostname -b PiHomie
sed -i -e '/127\.0\.1\.1/ s/.*/127\.0\.1\.1\tPiHomie/g' /etc/hosts

# -- Apache2
a2enmod wsgi
sed -i -e "s|%%PIHOMIE_ROOT%%|${ROOT_PATH}|" $SCRIPT_PATH/apache_vhost.conf
sed -i -e "s|%%PIHOMIE_GATEWAY%%|${SCRIPT_PATH}/gateway.wsgi|" $SCRIPT_PATH/apache_vhost.conf
mv $SCRIPT_PATH/apache_vhost.conf /etc/apache2/sites-available/pihomie.conf
a2ensite pihomie
service apache2 reload


# =============================
# Start der zusätzlichen Module:
# =============================
for m in "${modules[@]}"
do
	echo
	echo "=> Starte Modul $m"
	echo
done