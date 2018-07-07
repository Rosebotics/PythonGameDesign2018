"""
Reads a jpg image and writes it as a png.
Displays images.

Important functions in the cv2 library.
  -- imread
  -- imwrite
  -- imshow
  -- waitKey
  
Authors:  David Mutchler (based on examples from others), September 2012.
"""

import cv2 # Use cv2, not cv, wherever possible - cv2 is newer.
import numpy # Usually not needed, just for numpy.zeros(..) below.

def main():
    """ Example that shows reading, writing and displaying images. """
    filename_to_read = 'Honda-Asimo-delivers-drinks.jpg'
    filename_to_write = filename_to_read.replace('jpg', 'png')
    
    # Reads an image file.  It is stored internally as a numpy array (matrix).
    image = cv2.imread(filename_to_read)
    if image is None:
        print('Error - the image file does not exist or is in the wrong place.')
    
    # Writes an image file from the image.
    cv2.imwrite(filename_to_write, image)
    
    # Displays the image in a window.
    # Waits for any keypress before continuing.
    cv2.imshow('Asimo. Press any KEY to continue.', image)
    
    
    # Reads another image file, then displays its image.
    image_mars = cv2.imread('mars_curiosity.jpg')
    cv2.imshow('Mars Curiosity. Press any KEY to continue.', image_mars)
    cv2.waitKey()
    
    # Closes the window with Asimo.  Note that you reference a window
    #    by its name, that is, by its caption (title).
    cv2.destroyWindow('Asimo. Press any KEY to continue.')
    cv2.waitKey()
    
    # Prints the internally-stored image (numpy array) on the console.
    # Makes, prints and displays a new zero-filled numpy array.
    print(image)
    
    new = numpy.zeros((5, 10))
    print('New 5 x 10 image, all zeros (black)')
    print(new)
    cv2.imshow('All zeros (black)', new)
    cv2.waitKey()
    
    # Ending the program closes all open windows.
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
