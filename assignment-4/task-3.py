import numpy as np
import cv2

# Load a local image
jerryImage = cv2.imread('jerry.png')

# Functions


def ScaleImage(image, scaleFactor):
    # Get the image dimensions
    """
    image.shape image is a NumPy array representing the image.
    .shape returns a tuple containing: (height, width, channels)
    Height (rows) = Number of pixels in the vertical direction.
    Width (cols) = Number of pixels in the horizontal direction.
    Channels (Optional) = Number of color channels (e.g., 3 for RGB, 1 for grayscale).

    image.shape[:2]
    [:2] extracts only the first two values: (height, width), ignoring the channels.
    This is useful when we only care about the image dimensions, not the color channels.
    rows, cols = image.shape[:2]: Assigns the height to rows and the width to cols.
    """
    height, width = image.shape[:2]

    # Create a scaling matrix for affine transformation (2x3)
    scalingMatrix = np.array([
        [scaleFactor, 0, 0],  # Scale x-axis
        [0, 1, 0]   # Scale y-axis
    ], dtype=np.float32)

    # Apply the scaling
    """
    When you apply any transformation matrix using cv2.warpAffine(), OpenCV performs two things:
        Maps pixels from the source image to new locations using the transformation matrix.
        Creates a new image with a defined output size (which you must specify).
    The key: Applying a transformation doesn’t automatically resize the output image. It only moves pixels inside the space you define.
    """
    scaledImage = cv2.warpAffine(
        image, scalingMatrix, (int(width * scaleFactor), height))

    return scaledImage


def RotateImage(image, angle):
    # Getting the image dimensions
    height, width = image.shape[:2]

    # Creating a rotation matrix
    """
    cv2.getRotationMatrix(centerOfImage, angleToRotate, scaleFactor)
    """
    rotationMatrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # Apply the rotation
    rotatedImage = cv2.warpAffine(image, rotationMatrix, (width, height))

    return rotatedImage


def TranslateImage(image, xOffset, yOffset):
    # Get the image dimensions
    height, width = image.shape[:2]


    # Create Translation Matrix
    translationMatrix = np.array([
        [1, 0, xOffset],
        [0, 1, yOffset]],
        dtype=np.float32)

    # Applying transformation
    translatedImage = cv2.warpAffine(image, translationMatrix, (int(width + xOffset), int(height + yOffset)))

    return translatedImage

# Main
cv2.imshow("Jerry Original", jerryImage)

scaledImage = ScaleImage(jerryImage, 2)
cv2.imshow("Jerry Wide", scaledImage)

rotatedImage = RotateImage(jerryImage, 90)
cv2.imshow("Jerry Rotated", rotatedImage)

translatedImage = TranslateImage(jerryImage, 100, 200)
cv2.imshow("Jerry Translated", translatedImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
