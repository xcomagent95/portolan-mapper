import math
import json

def getPortolan(bbox, layout):
    anglesInner = [360, 22.5, 45, 67.5, 180, 202.5, 225, 247.5, 90, 112.5, 135, 157.5, 270, 292.5, 315, 337.5]
    anglesOuter = [11.25, 22.5, 33.75, 45.0, 56.25, 67.5, 78.75, 90.0, 101.25, 112.5, 123.75, 135.0, 146.25, 157.5, 168.75, 180.0, 191.25, 202.5, 213.75, 225.0, 236.25, 247.5, 258.75, 270.0, 281.25, 292.5, 303.75, 315.0, 326.25, 337.5, 348.75, 360.0]
    anglesLeft = [360, 22.5, 45, 67.5, 90, 337.5, 315, 292.5, 270]
    anglesRight = [180, 270, 247.5, 225, 202.5, 157.5, 135, 112.5, 90]
    

        
    
    xCenter = abs(bbox[0][0]) - abs(bbox[1][0])
    yCenter = abs(bbox[0][1]) - abs(bbox[1][1])
    
    sizeX = abs(bbox[0][0])
    sizeY = abs(bbox[0][1])
    
    if(layout == 'o'):
        getGeometries(xCenter, yCenter, anglesInner, anglesOuter, "center", sizeX, sizeY)
        
def getGeometries(x, y, anglesInner, anglesOuter, name, sizeX, sizeY):    
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
    
    for i in anglesInner:
        px = x + (sizeX * math.cos(i*(math.pi/180)))  
        py = y + (sizeY * math.sin(i*(math.pi/180)))
        
        
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
    '''
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
    '''
    for p in points:
        
        x1 = p["geometry"]["coordinates"][0]
        y1 = p["geometry"]["coordinates"][1]
        for a in anglesOuter:
            x2 = x1 + (180 * math.cos(a*(math.pi/180)))  
            y2 = y1 + (180 * math.sin(a*(math.pi/180)))
            line = {
             "type": "Feature",
             "properties": {'id': id, 'angle': a},
             "geometry": {
               "coordinates": [
                 [
                   x1,
                   y1
                 ],
                 [
                   x2,
                   y2
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

getPortolan([(-90, 90), (90, -90)], 'o')

