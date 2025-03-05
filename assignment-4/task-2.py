import numpy as np


def GreyscaleImage():
    # Creating an image of random black (0), white(255) and greyish(0-255) color values
    """
    This creates a 5x5 matrix with random values in between 0 and 255
    dtype: Stands for "data type".
    Specifies the type of numbers stored in the NumPy array.
    np.uint8 (Unsigned 8-bit Integer)
    uint = Unsigned Integer (no negative values).
    8 = 8 bits per number.
    Stores values from 0 to 255 (common in image processing).
    """
    image = np.random.randint(0, 255, (5, 5), dtype=np.uint8)
    
    # Printing the created image
    print(f"Original Generated Image:\n{image}\n")
    
    # Slicing the image, cropping only the middle 3x3 region of the image
    # image[1:4, 1:4] = image[startRow:endRow, StartCol:endCol] excluding the endRow and endCol
    croppedImage = image[1:4, 1:4]
    print(f"Cropped Image:\n{croppedImage}\n")
    
    # Inverting the colors of the image
    """
    0 becomes 255
    255 becomes 0
    120 becomes 135 (since 255 - 120 = 135)
    """
    invertedImage = 255 - croppedImage
    
    # Displaying the results
    print(f"Inverted Image:\n{invertedImage}\n")
    
# Main
GreyscaleImage()