#! /bin/bash

# Installation der Abhängigkeiten für PiHomie
# auf einem Raspian Stretch (Lite)

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

# =============================
# Start der zusätzlichen Module:
# =============================
for m in "${modules[@]}"
do
	echo
	echo "=> Starte Modul $m"
	echo
done