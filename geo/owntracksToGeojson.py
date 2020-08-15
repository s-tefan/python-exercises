#!/usr/bin/env python

import paho.mqtt.client as mqtt
import json
import time
from pyproj import CRS, Transformer, Geod

# The callback for when the client successfully connects to the broker
# Verkar inte funka, prenumererar manuellt nedan i stället
def on_connect(client, userdata, rc):
    ''' We subscribe on_connect() so that if we lose the connection
        and reconnect, subscriptions will be renewed. '''

    client.subscribe("owntracks/+/+")
    print("Prenumererar!")

# The callback for when a PUBLISH message is received from the broker
def on_message(client, userdata, msg):

    topic = msg.topic

    try:
        data = json.loads(msg.payload)       
        print(data)
        lat, lon = float(data['lat']), float(data['lon'])
        print(lat,lon)
        tm_coords = transformer.transform(lat, lon)
        tm_n, tm_e = int(tm_coords[0]), int(tm_coords[1])
        print(tm_coords)
        #'''
        print('TID = {0} is currently ({1}, {2}) at'.format(\
            data['tid'], data['tst'], \
            time.ctime(int(data['tst']), \
                )))
        print('WGS 84: {0} N, {1} E, {2} möh'.format(\
            data['lat'], data['lon'], data['alt']))
        print('SWEREF99 TM: N{0}, E{1}'.format(\
            tm_n, tm_e))
        away = geod_wgs84.line_length([hem_lat, lat], [hem_lon, lon])
        print('{0} meter hemifrån'.format(away))
        print(translate(msg.payload))
        #        '''
        #print(str(msg.payload))
    except:
        print("Cannot decode data on topic {0}".format(topic))

def translate(ot_data):
    ot = json.loads(ot_data)
    point =     {'type': 'Point',\
        'coordinates': [ot['lon'], ot['lat']]}
    props = ot
    geo = {'type': 'Feature',\
        'geometry': point,
        'properties': props }
    return json.dumps(geo)






client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Try to connect ...")
client.connect("localhost", 1883, 60)
print("Finished connecting")

client.subscribe("owntracks/+/+")

crs_4326 = CRS.from_epsg(4326) # WGS 84
crs_3006 = CRS.from_epsg(3006) # SWEREF99 TM
transformer = Transformer.from_crs(crs_4326, crs_3006)
geod_wgs84 = crs_4326.get_geod()
geod_sweref99 = crs_3006.get_geod()
hem_tm_N, hem_tm_E = 6472375, 433996
hem_lat, hem_lon = Transformer.from_crs(crs_3006,crs_4326).transform(hem_tm_N, hem_tm_E)
print(crs_3006.axis_info)
print(crs_4326.axis_info)

print('Hemma: {lat} N, {lon} E; N {n}, E {e}'.format(\
    lat = hem_lat, lon = hem_lon, n = hem_tm_N, e = hem_tm_E))
# Blocking call which processes all network traffic and dispatches
# callbacks (see on_*() above). It also handles reconnecting.





client.loop_forever()
