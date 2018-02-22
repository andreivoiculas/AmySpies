from PIL import Image
from HueFormulas import nameOfHue,rgbToHls,colorNeighbour
import operator
import sys
im = Image.open(str(sys.argv[1]))
im = im.convert('RGB')

#returns a dictionary of colors and the percentage the color exists in the photo
def getColours(image):
  pixel = image.load()
  x,y = image.size
  allPixels = x*y
  #print(x,y)
  labels = list()
  values = list()
  colorToY = dict()
  counter = 0
  for row in range(0,x):
    for column in range(0,y):
      rgb = list(pixel[row,column])
      try:
        dump = rgb[3] #tests for alpha
        rgb.pop()     #and removes it if it exists
      except:
        pass
      rgb = tuple(rgb)
      hls = rgbToHls(rgb)
      if(nameOfHue(hls) not in labels):
      	labels.append(nameOfHue(hls))
      	colorToY[nameOfHue(hls)] = counter
      	values.append(1)
      	counter = counter+1
      else:
      	values[colorToY[nameOfHue(hls)]] += 1
  colorStats = dict()
  for color in range(0,len(values)):
    colorStats[labels[color]] = values[color]/float(allPixels)*100
  return colorStats

def reduceColors(colorStats):
  for color in colorStats.keys():
    col1,col2 = colorNeighbour(color)
    if(col1 in colorStats.keys()):
      biggerThanNeighbour = colorStats[col1] < colorStats[color]
      try:
        biggerThanCompetingNeighbour = (colorStats[colorNeighbour(col1)[0]] 
                                      < colorStats[color])
      #if competing neighbour doesn't exist,color is by default
      except Exception:
        biggerThanCompetingNeighbour = True

      if( biggerThanNeighbour and biggerThanCompetingNeighbour):
        colorStats[color] +=colorStats[col1]
        colorStats[col1] = 0

    if(col2 in colorStats.keys()):
      biggerThanNeighbour = colorStats[col2] < colorStats[color]
      try:
        biggerThanCompetingNeighbour = (colorStats[colorNeighbour(col2)[1]] 
                                      < colorStats[color])
      #if competing neighbour doesn't exist,color is by default
      except Exception:
        biggerThanCompetingNeighbour = True

      if( biggerThanNeighbour and biggerThanCompetingNeighbour):

        colorStats[color] +=colorStats[col2]
        colorStats[col2] = 0
  return colorStats

colorDict = dict()
picStats = getColours(im)
picStats = reduceColors(picStats)
picStats = reversed(sorted(picStats.items(), key=lambda x:x[1]))
picStats = filter(lambda x:x[1] > 5,picStats)
for color in picStats:
  color = list(color)
  color[1] = round(color[1],2)
  colorDict[color[0]] = color[1]
print colorDict
  

