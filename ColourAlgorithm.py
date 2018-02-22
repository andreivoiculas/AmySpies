from PIL import Image
from HueFormulas import colourList,nameOfHue,rgbToHls
import matplotlib.pyplot as plt
#im_path = input("Enter the path of the image: ")
im = Image.open("./../colours/romania.png")
im = im.convert('RGB')
def getColours(image):
  pixel = image.load()
  x,y = image.size
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

  #print(labels,values)
  plt.bar(labels,values,1/3.0,color = "red")
  plt.show()

getColours(im)


