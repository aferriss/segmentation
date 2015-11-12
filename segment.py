from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np

from skimage.data import astronaut
from skimage.segmentation import felzenszwalb, slic, quickshift
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from PIL import Image

import time



def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="uint8" )
    return data

im = load_image("clouds.jpg")
count = 0;

def doSegment(im):
	timestr = time.strftime("%Y%m%d-%H%M%S")
	global count

	img = img_as_float(im)
	#img = img_as_float(imgO[::2, ::2])

	#segments_fz = felzenszwalb(img, scale=100, sigma=0.5, min_size=90)
	#segments_slic = slic(img, n_segments=250, compactness=10, sigma=1)
	segments_quick = quickshift(img, kernel_size=10, max_dist=30, ratio=1.0)

	#if(count % 2 == 0):
	bounds = mark_boundaries(img, segments_quick,color=(1.0, 1.0, 1.0), mode="subpixel")
	#else:
	#	bounds = mark_boundaries(img, segments_quick,color=(1, 1, 1), mode="inner")

	bb = Image.fromarray(np.uint8(bounds*255))
	bb.show()
	
	#bb.save("output/white"+timestr+".jpg",quality=100)
	bb = bb.resize((500, 500), Image.ANTIALIAS)
	count = count + 1
	#doSegment(bb)

doSegment(im)

"""
print("Felzenszwalb's number of segments: %d" % len(np.unique(segments_fz)))
print("Slic number of segments: %d" % len(np.unique(segments_slic)))
print("Quickshift number of segments: %d" % len(np.unique(segments_quick)))


fig, ax = plt.subplots(1, 3) 
fig.set_size_inches(8, 3, forward=True)
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95, 0.05, 0.05)

ax[0].imshow(mark_boundaries(img, segments_fz))
ax[0].set_title("Felzenszwalbs's method")
ax[1].imshow(mark_boundaries(img, segments_slic))
ax[1].set_title("SLIC")
ax[2].imshow(mark_boundaries(img, segments_quick))
ax[2].set_title("Quickshift")
for a in ax:
    a.set_xticks(())
    a.set_yticks(())
plt.show()
"""




