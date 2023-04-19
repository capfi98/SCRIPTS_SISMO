# Autor: Carlos Perez, cept.
# Fecha: 18/04/2023
# Versión:
#       v.1: Creacion.


## PROCEDIMIENTO PARA LA OBTENCION DE PSD Y HELICORDER, ORGANIZADOR DE LOS MISMOS Y PLANTILLA DE LATEX

Para la obtencion de imagenes especializadas de sismologia fue necesario la implementacion de SCRIPTS para el facil manejo,
manipulacion y obtencion de distintos productos que contribuyen a un ahorro de tiempo. Sin embargo, se hace un llamado a 
PRESTAR ATENCION en la manipulacion de los scripts, modificar las HORAS, IPS, DIRECTORIOS, y demas cosas de utilidad, para 
un buen manejo de su entorno con los scripts.

## REQUISITOS

Ninguno, mas que instalar python3 y tener bash.

## INSTALACION

Ninguna.

## USO 

1. Ejecutar: PSD_HELI_GEN.py, notar que se debe modificar la IP del FDSW y los tiempos.
2. Ejecutar: CHANNEL_SORTER.sh, permite la organizacion por canales HHZ, HNZ y EHZ.
3. Ejecutar: MAKE_LATEX.sh, para obtener una plantilla de \latex, para cualquier tipo de informe. 
Sientase libre de modificar las subfiguras manipulando '\scale', o bien, la plantilla a su conveniencia. 
Considere modificar los directorios necesarios

## LICENCIA

Uso Libre

## CONTACTO

Carlos Perez, cept
c4rpt001@gmail.com
