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
LatLong = "-28.061235, 153.364107"
Pin_A =  "color:blue|label:A|-28.061235, 153.364107"
Pin_B =  "color:red|label:B|-28.060705, 153.363179"
Path = "color:0x000fff|weight:6|-28.061235, 153.364107|-28.061050, 153.363308"
PathFill="color:0x000fff|weight:4|fillcolor:0xFFFF0033|-28.061050, 153.363308|-28.060823, 153.362697|" \
"-28.060255, 153.363066|-28.060482, 153.363657|-28.061050, 153.363308"


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
f = open('roy01.png ', 'wb') 
  
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
