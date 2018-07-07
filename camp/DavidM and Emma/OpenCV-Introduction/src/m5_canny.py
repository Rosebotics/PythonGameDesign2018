"""
Demonstrates an image manipulation that is particularly useful:
  -- Canny (for edge detection)
  
Authors:  David Mutchler (based on examples from others), September 2012.
"""

import cv2

def main():
    """ Example that shows the   cv2.Canny  function in action. """
    # Students:  Read the documentation of the   cv2.Canny   function
    #    at http://docs.opencv.org/modules/refman.html
    #    (search for cv2.Canny) while reading/running this example.
    filename = 'big_lego_robot.jpg'
    # filename = 'stripes.bmp' # Try this one too
    image = cv2.imread(filename)
    grayscale = cv2.imread(filename, 0)
    if image is None:
        print('Error - the file does not exist or is in the wrong place.')
    
    cv2.imshow('Original image', image)
    cv2.imshow('Grayscale image', grayscale)
    cv2.waitKey()
    
    demo_canny(grayscale) # Canny operates on grayscale
    
def demo_canny(grayscale):
    """ Uses Canny to try to find edges in an image """
    
    # Thresholds at 10 and 100, respectively.
    lower_threshold = 10
    upper_threshold = 100
    new_grayscale = cv2.Canny(grayscale, lower_threshold, upper_threshold)
     
    cv2.imshow('Canny 1 grayscale', new_grayscale)
    cv2.waitKey()
    
    # Thresholds at 1 and 2, respectively
    lower_threshold = 1
    upper_threshold = 2
    new_grayscale = cv2.Canny(grayscale, lower_threshold, upper_threshold)
    
    cv2.imshow('Canny 2 grayscale', new_grayscale)
    cv2.waitKey()
    
    # Thresholds at 200 and 300, respectively
    lower_threshold = 200
    upper_threshold = 300
    new_grayscale = cv2.Canny(grayscale, lower_threshold, upper_threshold)
    
    cv2.imshow('Canny 3 grayscale', new_grayscale)
    cv2.waitKey()
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
