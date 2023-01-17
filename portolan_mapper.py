import math
import json

def getPortolan(x, y, size, layout):
    anglesFull = [360, 22.5, 45, 67.5, 180, 202.5, 225, 247.5, 90, 112.5, 135, 157.5, 270, 292.5, 315, 337.5]
    anglesLeft = [360, 22.5, 45, 67.5, 90, 337.5, 315, 292.5, 270]
    anglesRight = [180, 270, 247.5, 225, 202.5, 157.5, 135, 112.5, 90]
    
    if(layout == "oo"):
        getGeometries(x+size, y, anglesFull, "left", size)
        getGeometries(x-size, y, anglesFull, "right", size)  
    elif(layout == '(o)'):
        getGeometries(x, y, anglesFull, "center", size)
        getGeometries(x+size, y, anglesLeft, "left", size)
        getGeometries(x-size, y, anglesRight, "right", size)
    elif(layout == ')o('):
        getGeometries(x, y, anglesFull, "center", size)
        getGeometries(x+2*size, y, anglesRight, "left", size)
        getGeometries(x-2*size, y, anglesLeft, "right", size)
    
    
def getGeometries(x, y, angles, name, size):
    
    point = {
      "type": "Feature",
      "properties": {"angle": 0},
      "geometry": {
        "coordinates": [
          x,
          y
        ],
        "type": "Point"
      }}
    
    points = []
    points.append(point)
    
    for i in angles:
        px = x + (size * math.cos(i*(math.pi/180)))  
        py = y + (size * math.sin(i*(math.pi/180)))
        
        
        point = {
          "type": "Feature",
          "properties": {"angle": i},
          "geometry": {
            "coordinates": [
              px,
              py
            ],
            "type": "Point"
          }}
        
        points.append(point)
        
    pointsData = {
          "type": "FeatureCollection",
          "features": points
        }
    
    out_file = open(name + "pointsData.json", "w")
    json.dump(pointsData, out_file, indent = 6)
    out_file.close()
    
    lines = []
    id = 0
    for i in points:
        for y in points:
            line = {
             "type": "Feature",
             "properties": {'id': id},
             "geometry": {
               "coordinates": [
                 [
                   i["geometry"]["coordinates"][0],
                   i["geometry"]["coordinates"][1]
                 ],
                 [
                   y["geometry"]["coordinates"][0],
                   y["geometry"]["coordinates"][1]
                 ]
               ],
               "type": "LineString"
             }
           }
            lines.append(line)
            id += 1
            
    linesData = {
          "type": "FeatureCollection",
          "features": lines
        }
            
    out_file = open(name + "linesData.json", "w")
    json.dump(linesData, out_file, indent = 6)
    out_file.close()
        
    return True

#getPortolan(0, 0, 90, 'oo')
#getPortolan(0, 0, 90, '(o)')
getPortolan(0, 0, 90, ')o(')
#Types: oo, (o), )o(
