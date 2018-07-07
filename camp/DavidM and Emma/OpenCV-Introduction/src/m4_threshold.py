"""
Demonstrates an image manipulation that is particularly useful:
  -- threshold
  -- adaptiveThreshold
  
Authors:  David Mutchler (based on examples from others), September 2012.
"""

import cv2

def main():
    """ Example that shows the   cv2.threshold  function in action. """
    # Students:  Read the documentation of the   cv2.threshold   function
    #    at http://docs.opencv.org/modules/refman.html
    #    (search for cv2.threshold) while reading/running this example.
    filename = 'big_lego_robot.jpg'
    image = cv2.imread(filename)
    grayscale = cv2.imread(filename, 0)
    if image is None:
        print('Error - the file does not exist or is in the wrong place.')
    
    cv2.imshow('Original image', image)
    cv2.imshow('Grayscale image', grayscale)
    cv2.waitKey()
    
    demo_threshold(image, grayscale)
    
def demo_threshold(image, grayscale):
    threshold = 170
    maxval = 255
    
    # The threshold function returns an error code and the new image.
    # The error code (r) is not useful here, so I ignore it in the code below.
    
    # The documentation says that threshold is only to be applied to grayscale,
    # but it seems to do something on BGR (3-channel) images, so I include them.
    
    # Threshold #1: Pixels above the threshold (170) are set to 255, others to 0.
    r, new_image = cv2.threshold(image, threshold, maxval, cv2.THRESH_BINARY) #@UnusedVariable
    r, new_grayscale = cv2.threshold(grayscale, threshold, maxval, cv2.THRESH_BINARY) #@UnusedVariable
    
    cv2.imshow('Threshold 1 image', new_image)
    cv2.imshow('Threshold 1 grayscale', new_grayscale)
    cv2.waitKey()
    
    # Threshold #2: Pixels above the threshold (200) are left alone, others set to 0.
    threshold = 200
    r, new_image = cv2.threshold(image, threshold, maxval, cv2.THRESH_TOZERO) #@UnusedVariable
    r, new_grayscale = cv2.threshold(grayscale, threshold, maxval, cv2.THRESH_TOZERO) #@UnusedVariable
    
    cv2.imshow('Threshold 2 image', new_image)
    cv2.imshow('Threshold 2 grayscale', new_grayscale)
    cv2.waitKey()
    
    # Threshold #3 (adaptive thresholding):  Similar to #1, but each pixel is thresholded
    #    based on a BLOCK of pixels surrounding the pixel.
    maxval = 255
    blocksize = 7
    c = 10 # Pixels more than 10 less than the average of the pixels nearby are set to 0.
    new_grayscale = cv2.adaptiveThreshold(grayscale, maxval,
                                          cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                          blocksize, c)
    # only grayscale, does not work for BGR (3-channel)
    
    cv2.imshow('Threshold 3 grayscale', new_grayscale)
    cv2.waitKey()
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
