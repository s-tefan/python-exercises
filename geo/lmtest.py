import requests

from PIL import Image
#from io import BytesIO
import io
#from StringIO import StringIO




# Värden att testa med
N = 6455796
E = 295955
Z = 9


'''
URL = "https://api.lantmateriet.se/historiska-ortofoton/wms/v1"
#URL = 'http://api.lantmateriet.se/historiska-ortofoton/wms/v1?request=GetCapabilities&version=1.1.1'
bbox = '{},{},{},{}'.format(E-512,N-512,E+512,N+512)
refsys = 'EPSG:3006'
wpx = '1024' # antal px, max 4096
hpx = '1024' # antal px, max 4096
fmt = 'image/png' # png, jpeg, tiff
PARAMS = {'REQUEST': 'GetMap',\
    'SERVICE': 'WMS',\
    'VERSION': '1.1.1',\
    'LAYERS' : 'OI.Histortho_60',\
    'BBOX': bbox,\
    'SRS': refsys,\
    'WIDTH': wpx,\
    'HEIGHT': hpx,\
    'FORMAT': fmt
        }
r = requests.get(url = URL, params = PARAMS)
print(r)
'''

def LM_tile_URL(N,E,Z):
    origo3006 = (8500000, -1200000)
    res3006 = (4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8 ) # m/px
    origo3857 = (-20037508.342789, 20037508.342789)
    res3857 = ( \
    156543.0339280410, 78271.51696402048, \
    39135.75848201023, 19567.87924100512, \
    9783.939620502561, 4891.969810251280, \
    2445.984905125640, 1222.992452562820, \
    611.4962262814100, 305.7481131407048, \
    152.8740565703525, 76.43702828517624, \
    38.21851414258813, 19.10925707129406, \
    9.554628535647032, 4.777314267823516 )

    NN = origo3006[0] - N
    EE = - origo3006[1] + E
    W = 256*res3006[Z]
    X = NN//W
    Y = EE//W


    token = "eaa01c4f-4dec-3afa-a4cf-5120f183bee0"
    URLmall = \
    '''https://api.lantmateriet.se/open/topowebb-ccby/v1/wmts/\
token/{}/?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&\
LAYER=topowebb&STYLE=default&TILEMATRIXSET=3006&\
TILEMATRIX={}&TILEROW={}&TILECOL={}&FORMAT=image/png'''
    URL = URLmall.format(token,Z,X,Y)
    return URL
    
url = LM_tile_URL(N,E,Z)
print(url)
response = requests.get(url)
print(type(response.content))
#print(response.text)
f = io.BytesIO(response.content)
print(type(f))
img = Image.open(f)
img.show()
#img = Image.open(response.raw)

## authheader = "Authorization: Bearer eaa01c4f-4dec-3afa-a4cf-5120f183bee0"



"""
https://api.lantmateriet.se/open/topowebb-ccby/v1/wmts/token/eaa01c4f-4dec-3afa-a4cf-5120f183bee0/?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=t
opowebb&STYLE=default&TILEMATRIXSET=3006&TILEMATRIX=9&TILEROW=862&TILECOL=887&FORMAT=image/png
"""