import matplotlib.pyplot as plt
from PIL import Image
from io import StringIO
from urllib.request import urlopen

def getImage():
    url = "http://maps.googleapis.com/maps/api/staticmap?center=-30.027489,-51.229248&size=800x800&zoom=14&sensor=false"
    im = Image.open(StringIO(urlopen(url).read()))
    return(im)

if __name__ == "__main__":
    im = getImage()
    plt.imshow(im)
    plt.show()