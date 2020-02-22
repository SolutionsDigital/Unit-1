# Python program to get a google map  
# image of specified location using  
# Google Static Maps API 
  
# importing required modules 
import requests 
  
# Enter your api key here 
api_key ="Use your Own API KEY HERE"
  
# url variable store url 
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map, 
# equidistant from all edges of the map.  
LatLong = "-28.061411, 153.364882"
Pin_A =  "color:blue|label:A|-28.061146,153.364009"
Pin_B =  "color:red|label:D|-28.060255,153.365522"
Path = "color:0x000fff|weight:6|-28.061120,153.364036|-28.061025,153.364359|-28.060274,153.364940"
PathFill="color:0x000fff|weight:4|fillcolor:0xFFFF0033|-28.060274,153.364940|-28.059885,153.364951|" \
"-28.059676,153.365296|-28.059761,153.365769|-28.059999,153.366168 |" \
"-28.060407,153.366319|-28.060664,153.365866|-28.060274,153.364940"


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
                 "&path=" + PathFill +
                 "&key=" + api_key) 
  
# wb mode is stand for write binary mode 
f = open('image_11.png ', 'wb') 
  
# r.content gives content, 
# in this case gives image 
f.write(r.content)

print(url +
                 "center=" + LatLong + 
                 "&zoom=" + str(zoom) + 
                 "&size=" + size + 
                 "&scale=" + str(scale) +
                 "&maptype=" + maptype +
                 "&maptype=" + maptype +
                 "&markers=" + Pin_A +
                 "&markers=" + Pin_B +
                 "&path=" + Path +
                 "&path=" + PathFill +
                 "&key=" + api_key)



# close method of file object 
# save and close the file 
f.close() 
