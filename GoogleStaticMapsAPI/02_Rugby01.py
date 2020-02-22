# Python program to get a google map  
# image of specified location using  
# Google Static Maps API 
  
# importing required modules 
import requests 
  
# Enter your api key here 
api_key ="AIzaSyAhxGjmC2jWqLT95EU9B7f67J7Y0jAwXCU"
  
# url variable store url 
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map, 
# equidistant from all edges of the map.  
LatLong = "-28.060866, 153.364423"
Pin_A =  "color:blue|label:A|-28.061173, 153.364010"
Pin_B =  "color:red|label:C|-28.061718, 153.364584"
Path = "color:0x000fff|weight:6|-28.061173, 153.364010|-28.061718, 153.364584"
PathFill="color:0x000fff|weight:4|fillcolor:0xFFFF0033|-28.061718, 153.364584|" \
"-28.061798, 153.365061|-28.060932, 153.365244|-28.060866, 153.364729|" \
"-28.061718, 153.364584"


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
f = open('02_Rugby01.png ', 'wb') 
  
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
