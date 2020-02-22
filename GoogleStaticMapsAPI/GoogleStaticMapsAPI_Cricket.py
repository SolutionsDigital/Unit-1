# Python program to get a google map
# image of specified location using
# Google Static Maps API

# importing required modules
import requests

# Enter your api key here
api_key = "MyAPIkey"

# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"

# center defines the center of the map,
# equidistant from all edges of the map.
LatLong = "-28.061411, 153.364882"
Pin_A = "color:blue|label:A|-28.061146,153.364009"
Pin_E = "color:red|label:E|-28.060706, 153.363161"
Path = "color:0x000fff|weight:6|-28.061100, 153.363900|-28.060975, 153.363704"
PathFill = "color:0x000fff|weight:4|fillcolor:0xFFFF0033|-28.060975, 153.363704|-28.061177, 153.363269|"\
    "-28.061128, 153.362811|-28.060706, 153.362521|-28.060332, 153.362684|"\
    "-28.060102, 153.363173|-28.060227, 153.363629|-28.060572, 153.363812|"\
    "-28.060878, 153.363791|-28.060975, 153.363704"


# zoom defines the zoom level of the map
zoom = 17

# size in pixels free max is 640 x 640
size = "640x640"

# scale 1 or 2 or 4
scale = 2

# maptype terrain hybride satellite roads
maptype = "satellite"

# get method of requests module
# return response object ie URL
r = requests.get(url +
                 "center=" + LatLong +
                 "&zoom=" + str(zoom) +
                 "&size=" + size +
                 "&scale=" + str(scale) +
                 "&maptype=" + maptype +
                 "&maptype=" + maptype +
                 "&markers=" + Pin_A +
                 "&markers=" + Pin_E +
                 "&path=" + Path +
                 "&path=" + PathFill +
                 "&key=" + api_key)

# wb mode is stand for write binary mode
f = open('image_10.png ', 'wb')

# r.content gives content,
# in this case gives image
f.write(r.content)

# close method of file object
# save and close the file
f.close()
