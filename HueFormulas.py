"""Using the color dict provided,it creates a variable 
colorList which contains dictionaries with the form 
name(str),rgb(tuple),hls(tuple)"""

def rgbToHls(rgb):
  red = rgb[0]/255.0;
  green = rgb[1]/255.0;
  blue = rgb[2]/255.0;
  maxC = max(red,green,blue)
  minC = min(red,green,blue)
  delta = maxC - minC
  light = (maxC + minC)/2.0
  if delta == 0:
    return (0,round(light,2),0)
  elif maxC == red:
    return (round(60*(((green - blue)/delta) % 6),2),
           round(light,2),
           round(delta/(1-abs(2*light-1)),2))
  elif maxC == green:
    return (round(60*(((blue - red)/delta) + 2),2),
           round(light,2),
           round(delta/(1-abs(2*light-1)),2))
  else: 
    return (round(60*(((red - green)/delta) + 4),2),
           round(light,2),
           round(delta/(1-abs(2*light-1)),2))
hueList = ["red","red-orange","orange-brown","orange-yellow","yellow",
            "yellow-green","green","green-cyan","cyan","cyan-blue","blue",
            "blue-magenta","magenta","magenta-pink","pink","pink-red"]

def colorNeighbour(color):
  if(color in hueList):
    try:
      return (hueList[hueList.index(color)-1],
             hueList[hueList.index(color)+1])
    except Exception:
      try:
        return (hueList[hueList.index(color)-1],"red")
      except Exception:
        return("red-orange","pink-red")
  else:
    return "i don't","care"


    
  

def nameOfHue(hls):
  hue = hls[0]
  light = hls[1]
  saturation = hls[2]
  if(light <= 0.05):
    return "black"
  elif(light >= 0.9):
    return "white"
  else:
    if(saturation <= 0.1):
      return "grey"
    else: 
      if hue > 355 or hue <= 10:
        return "red"
      elif hue > 10 and hue <= 20:
        return "red-orange"
      elif hue > 20 and hue <= 40:
        return "orange-brown"
      elif hue > 40 and hue <= 50:
        return "orange-yellow"
      elif hue > 50 and hue <= 60:
        return "yellow"
      elif hue > 60 and hue <= 80:
        return "yellow-green"
      elif hue > 80 and hue <= 140:
        return "green"
      elif hue > 140 and hue <= 169:
        return "green-cyan"
      elif hue > 169 and hue <= 200:
        return "cyan"
      elif hue > 200 and hue <= 220:
        return "cyan-blue"
      elif hue > 220 and hue <= 240:
        return "blue"
      elif hue > 240 and hue <= 280:
        return "blue-magenta"
      elif hue > 280 and hue <= 320:
        return "magenta"
      elif hue > 320 and hue <= 330:
        return "magenta-pink"
      elif hue > 330 and hue <= 345:
        return "pink"
      elif hue > 345 and hue <= 355:
        return "pink-red"
