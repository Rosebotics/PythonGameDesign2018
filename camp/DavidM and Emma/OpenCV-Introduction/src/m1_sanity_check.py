"""
Reads an image and prints the matrix form of that image.
Use this as a sanity check that your OpenCV is working.
    
Authors:  David Mutchler (based on examples from others), September 2012.
"""
#------------------------------------------------------------------------
# Run this program as a sanity check that your OpenCV is working.
# It should print (on the console) a matrix (list of lists of lists)
# that ENDs with:
#   [154 147 150]
#   [153 146 149]
#   [157 150 153]]]
# If you don't see that, something is wrong.
#------------------------------------------------------------------------

import cv2

def main():
    """ Converts a specific jpg (which must be xx """
    filename = 'Honda-Asimo-delivers-drinks.jpg'
    image = cv2.imread(filename)
    if image is None:
        print('Error - the file does not exist or is in the wrong place.')
    print(image)

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
