# Python program to get a google map  
# image of specified location using  
# Google Static Maps API 
  
# importing required modules 
import requests 
  
# Enter your api key here 
api_key ="Your API Key"
  
# url variable store url 
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map, 
# equidistant from all edges of the map.  
LatLong = "-28.061411, 153.364882"
Pin_A =  "color:blue|label:A|-28.061146,153.364009"
Pin_B =  "color:green|label:B|-28.059699,153.36372"
Path = "color:0x000fff|weight:4|-28.060968,153.363841|-28.060897,153.363757|-28.059927,153.363479"

# zoom defines the zoom level of the map 
zoom=17

# size in pixels free max is 640 x 640
size="640x640"

# scale 1 or 2 or 4
scale=2

# maptype terrain hybride satellite roads
maptype="satellite"
  
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
                 "&markers=" + Pin_B +
                 "&path=" + Path +
                 "&key=" + api_key) 
  
# wb mode is stand for write binary mode 
f = open('image_10.png ', 'wb') 
  
# r.content gives content, 
# in this case gives image 
f.write(r.content) 
  
# close method of file object 
# save and close the file 
f.close() 
