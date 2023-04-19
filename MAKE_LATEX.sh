#!/bin/bash


FILE=ESTACIONES.txt
if [ -e $FILE ]; then
	rm -rf $FILE
	echo 'Archivo '$FILE' eliminado con exito. Creando nuevo '$FILE'.'
        find ./PSD/ -name "*.png" -type f  > $FILE
	sed -i -e 's/.png//g' -e 's/_/ /g' $FILE
	sed -i 's/\.\?\/PSD\/\(EHZ\|HNZ\|HHZ\)\///' $FILE


else
	echo 'Archivo $FILE no existe. Creando lista de estaciones.'
	find ./PSD/ -name "*.png" -type f  > $FILE
	sed -i -e 's/.png//g' -e 's/_/ /g' $FILE
	sed -i 's/\.\?\/PSD\/\(EHZ\|HNZ\|HHZ\)\///' $FILE
fi



(while read var1 var2;
do

echo '%                          STATION '$var1'  CHAN  '$var2'                              '
echo '\subsubsection{'$var1' '$var2'}'
echo ''
echo ''
echo '\begin{figure}[H]'
echo '\centering'
echo '\subfloat[PSD de la estación '$var1' '$var2']{\label{'$var1'_'$var2'_a}{\includegraphics[width=0.55\textwidth, height=0.55\textwidth]{ANALI/PSD/'$var2'/'$var1'_'$var2'.png}}}\hfill'
echo '\subfloat[Helicorder de la estación '$var1' '$var2']{\label{'$var1'_'$var2'_b}{\includegraphics[width=0.45\textwidth, height=0.7\textwidth]{ANALI/HELI/'$var2'/'$var1'_'$var2'_heli.png}}}'
echo '\caption{Gráficos de \textit{Power Spectral Distribution} (PSD) y helicorder para la estación '$var1' '$var2' \ref{'$var1'_'$var2'_a} y \ref{'$var1'_'$var2'_b} respectivamente}'
echo '\label{'$var1'_'$var2'_STAT}'
echo '\end{figure}'
echo '\newpage'
echo ''
echo ''
done  < $FILE) > LATEX_STATS.txt
