#!/usr/bin/python3

import sys
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.core.event import Catalog, Event
from obspy.signal import PPSD
from obspy import read

if len(sys.argv) < 5:
    print("Error: se requieren cuatro argumentos: NET, STAT, LOC y CHAN")
    print("Uso: python3 generar_helicorder.py NET STAT LOC CHAN")
    sys.exit(1)

# Crear cliente para el servicio web FDSN
client = Client("http://190.151.176.99:8080")

# Definir los parámetros de entrada
network = sys.argv[1]
station = sys.argv[2]
location = sys.argv[3]
channel = sys.argv[4]

# Definir el intervalo de tiempo de la descarga de datos
start_time = UTCDateTime("2023-04-16T00:00:00.000")
end_time = UTCDateTime("2023-04-17T00:00:00.000")

try:
    # Descargar los datos del sismo
    stream = client.get_waveforms(network, station, location, channel, start_time, end_time)
    stream.filter("bandpass", freqmin=0.3, freqmax=25, corners=4)

    # Crear un archivo PNG con el helicorder de la estación
    stream.plot(type="dayplot", interval=15, right_vertical_labels=False, vertical_scaling_range=5e3,
                one_tick_per_line=True, color=['black', 'darkblue'], show_y_UTC_label=False,
                outfile=station + '_' + channel + '_heli.png')

    print('El helicorder de {} {} está listo.'.format(station, channel))

except Exception as e:
    print('No se pudo crear el helicorder de {} {}. Error: {}'.format(station, channel, str(e)))
    print(e)

try:
    # Calcular la PPSD de los datos del sismo
    tr = stream[0]
    inv = client.get_stations(endafter=end_time, level="response", network=network, channel=channel)
    ppsd = PPSD(tr.stats, metadata=inv)
    ppsd.add(stream)
    ppsd.plot(station + '_' + channel + ".png")

    print('La PPSD de {} {} está lista.'.format(station, channel))

except Exception as e:
    print('No se pudo crear la PPSD de {} {}. Error: {}'.format(station, channel, str(e)))
