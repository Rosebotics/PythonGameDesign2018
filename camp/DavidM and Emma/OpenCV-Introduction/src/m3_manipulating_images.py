"""
Demonstrates:
  -- the internal format of an image (an M x N x 3 matrix) and
  -- how to manipulate an image:
       -- by calling a function that modifies the image, or
       -- by directly manipulating the numbers in the image.

Important methods and fields in the cv2 library,
where img is an image (as stored internally) by OpenCV:
  -- img.copy()
  -- img.shape
Important functions in the cv2 library:
  -- imread  imwrite   imshow  waitKey
  -- circle (and similar functions for drawing other shapes)
  
Authors:  David Mutchler (based on examples from others), September 2012.
"""

import cv2
import numpy # Only need this when directly manipulating the numpy array, see below.

def main():
    """ Example that shows reading, MANIPULATING and displaying images. """
    filename = 'stripes.bmp'
    
    # Reads an image file.  It is stored internally as a matrix.
    image_stripes = cv2.imread(filename)
    if image_stripes is None:
        print('Error - the file does not exist or is in the wrong place.')
    
    # Prints the internally-stored image (matrix) on the console.
    #   Study what gets printed, noting that:
    #     -- It is an M x N x 3 matrix, where
    #     -- The image has M rows and N columns, and
    #     -- image[i][j] is a 3-element list that represents a single pixel.
    print(image_stripes)
    
    # The default form of imread (as used above) represents each pixel
    # by a list of three numbers: the amount of Blue, Green and Red,
    # respectively, in the pixel.  Note that this is BGR order, not RGB.
    # Each number is 8 bits (hence between 0 and 255).
    # The pixel at image[i][j] is at row i and column j of the image,
    # so i is along the y-axis and j along the x-axis.
    
    height = len(image_stripes)
    width = len(image_stripes[0])
        
    print('The dimensions of this image are', image_stripes.shape)
    print('The height, width of the image are:', height, width)
    print('Pixel[0][0] (upper-left corner) is:', image_stripes[0][0])
    print('Pixel[0][width-1] (upper-right corner) is:', image_stripes[0][width - 1])
    print('Pixel[height-1][0] (lower-left corner) is:', image_stripes[height - 1][0])
    print('Pixel[height-1][width-1] (lower-right corner is:', image_stripes[height - 1][width - 1])
    
    # You can manipulate an image EITHER:
    #   -- by calling some cv2 function with the image as an argument, or
    #   -- by directly modifying the numbers in the image.
    # For example:
    
    # Makes three copies of the image:
    copy1 = image_stripes.copy()
    copy2 = image_stripes.copy()
    copy3 = image_stripes.copy()

    # Modifies the first copy by putting a filled circle onto it:
    center = (75, 50) # Points and colors are TUPLEs, not lists
    radius = 25
    color = (255, 255, 0) # Blue-green (aqua)
    thickness = -1 # Negative thickness means that the circle is filled.
    cv2.circle(copy1, center, radius, color, thickness)
    
    # Modifies the second copy by changing the numbers in the
    # middle 24 rows to:
    #  -- blue (top 8 of 24 rows),
    #  -- green (middle 8 of 24 rows), or
    #  -- red (bottom 8 of 24 rows)
    # thus make horizontal stripes.
    middle_row = height // 2
    for x in range(0, width - 1):
        for y in range(middle_row - 12, middle_row - 4):
            copy2[y][x] = (255, 0, 0)
        for y in range(middle_row - 4, middle_row + 3):
            copy2[y][x] = (0, 255, 0)
        for y in range(middle_row + 3, middle_row + 11):
            copy2[y][x] = (0, 0, 255)
            
    # Reads the original image file in grayscale.
    #   Note that the pixels here are a single number,
    #   not a 3-element list.
    image_grayscale = cv2.imread(filename, 0) # Optional argument 0 -> grayscale
    print('Dimensions of the grayscale image are: ', image_grayscale.shape)
    print('Example pixel of the grayscale image is: ', image_grayscale[100][50])
    
    # A typical direct manipulation of the image: transpose it.
    transposed1 = numpy.transpose(image_grayscale)
    transposed2 = numpy.transpose(image_stripes, [1, 0, 2])
    
    # Displays all the images (some may be on top of others):
    cv2.imshow('The original image', image_stripes)
    cv2.imshow('With a circle put onto it', copy1)
    cv2.imshow('With horizontal stripes put onto it', copy2)
    cv2.imshow('Grayscale version of original', image_grayscale)
    cv2.imshow('Transposed grayscale image', transposed1)
    cv2.imshow('Transposed original image', transposed2)
    cv2.waitKey()
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
