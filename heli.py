
#!/usr/bin/python3

#
#
#

import sys
from obspy.signal import PPSD
from obspy import read
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.core.event import read_events , Catalog , Event

#client = Client("http://172.20.9.20:8080")
#client = Client("http://172.20.8.4:8080")
client = Client("http://190.151.176.99:8080") #sv
#client_events = Client("http://172.20.9.11:8080")


NET=sys.argv[1]

STAT=sys.argv[2]
LOC=sys.argv[3]
CHAN=sys.argv[4]



STARTTIME = UTCDateTime("2023-03-28T00:00:00.000")
ENDTIME = UTCDateTime("2023-03-29T00:00:00.000")

try:


	st = client.get_waveforms(NET , STAT , LOC , CHAN , STARTTIME , ENDTIME )
	st.filter("bandpass", freqmin=.3, freqmax=25 , corners=4)

#st.plot(type="dayplot", interval=15, right_vertical_labels=False,
#        vertical_scaling_range=5e3, one_tick_per_line=True,
#        color=['black' , 'darkblue'], show_y_UTC_label=False )



	st.plot(type="dayplot", interval=15, right_vertical_labels=False,
        	vertical_scaling_range=5e3, one_tick_per_line=True,
        	color=['black' , 'darkblue'], show_y_UTC_label=False,outfile=STAT+'_'+CHAN+'_heli.png' )

	print('El helicorder de {} {}'.format(STAT,CHAN)+' lista c:')

except IndexError:
        print('El helicorder {} {}'.format(STAT,CHAN)+' no se creo :c')

try:
	tr=st[0]

	inv = client.get_stations(endafter=ENDTIME,level="response",network=NET,channel=CHAN)

	ppsd = PPSD(tr.stats, metadata=inv)
	ppsd.add(st)
#ppsd.plot()
	ppsd.plot(STAT+'_'+CHAN+ ".png")

	print('La PPSD de {} {}'.format(STAT,CHAN)+' lista c:')

except IndexError:
	print('La PPSD {} {}'.format(STAT,CHAN)+' no se creo :c')



#st.plot(type="dayplot", interval=15, right_vertical_labels=False,
#        vertical_scaling_range=7e3, one_tick_per_line=True,
#        color=['#000e34' , 'darkviolet'], show_y_UTC_label=True ,  events=cat , show_location_label=False)


#st.plot(type='dayplot',
#	interval = 15,
#	right_vertical_labels=True,
#	vertical_scaling_range=5e2,
#	one_tick_per_line=True,
#	color['brown', 'darkblue'],
#	show_y_UTC_label=True, events=cat)




##        color=['k', 'r', 'b', 'g'], show_y_UTC_label=False ,	events=[{"time": UTCDateTime("2023/01/23T01:14"), "text": "FELT"}] )
#        color=['k', 'r', 'b', 'g'], show_y_UTC_label=False ,	events=[ { 'text': 'FELT', 'time': UTCDateTime("2023/01/15T23:07") },{'text': 'FELT', 'time': UTCDateTime("2023/01/15T23:35") } , {'text': 'FELT', 'time': UTCDateTime("2023/01/16T01:54") } ] )



