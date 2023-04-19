#!/bin/env bash

# Nombre del script: CHANNEL_SORTER.sh
# Descripción: enfocado en la funcionalidad de mover las imágenes según su canal (HHZ, HNZ, EHZ) para PSD y HELI del programa PSD_HELI_GEN.py.
# Autor: Carlos Perez, cept.
# Fecha: 17/04/2023
# Versión:
#	v.1: Ver Descripcion.

# Depositamos imagenes en OBJECTS_PNG?
echo 'depositamos las imagenes en OBJECTS_PNG? Y|N'
read ANSW

if [[ $ANSW == Y ]]; then
	rm -rf OBJECTS_PNG
	mkdir ./OBJECTS_PNG
	cp *".png" ./OBJECTS_PNG
else
	echo "Adios"
	echo "Procedimiento: presiona Y para acceder, sino cualquier otra letra para salir"
	exit 1
fi

IMAGENES=./OBJECTS_PNG/

# Eliminar carpetas (en caso existieran) y crear nuevas

rm -rf ./PSD ./HELI
mkdir ./PSD ./HELI
rm -rf ./PSD/HHZ ./PSD/HNZ ./PSD/EHZ
mkdir ./PSD/HHZ ./PSD/HNZ ./PSD/EHZ


# Buscar archivos con la terminación "_HNZ.png" y moverlos a la carpeta "HNZ"
	# -type f busca archivos, no director11111111111111111111111111111111111111111111111111111111111ios
	# -exec pertenece a find, ejecuta x accion con lo encontrado
	# la accion de recolectar y escribir todos los archivos se realiza en {}, \; es el fin de -exec.
find "$IMAGENES" -type f -name "*_HNZ.png" -exec cp {} ./PSD/HNZ \;

# Buscar archivos con la terminación "_HHZ.png" y moverlos a la carpeta "HHZ"
find "$IMAGENES" -type f -name "*_HHZ.png" -exec cp {} ./PSD/HHZ \;


# Buscar archivos con la terminación "_EHZ.png" y moverlos a la carpeta "EHZ"
find "$IMAGENES" -type f -name "*_EHZ.png" -exec cp {} ./PSD/EHZ \;

rm -rf ./HELI/HHZ ./HELI/HNZ ./HELI/EHZ
mkdir ./HELI/HHZ ./HELI/HNZ ./HELI/EHZ

# Buscar archivos con la terminación "_HNZ_heli.png" y moverlos a la carpeta "HNZ"
        # -type f busca archivos, no directorios
        # -exec pertenece a find, ejecuta x accion con lo encontrado
        # la accion de recolectar y escribir todos los archivos se realiza en {}, \; es el fin de -exec.
find "$IMAGENES" -type f -name "*_HNZ_heli.png" -exec cp {} ./HELI/HNZ \;

# Buscar archivos con la terminación "_HHZ_heli.png" y moverlos a la carpeta "HHZ"
find "$IMAGENES" -type f -name "*_HHZ_heli.png" -exec cp {} ./HELI/HHZ \;


# Buscar archivos con la terminación "_EHZ_heli.png" y moverlos a la carpeta "EHZ"
find "$IMAGENES" -type f -name "*_EHZ_heli.png" -exec cp {} ./HELI/EHZ \;

