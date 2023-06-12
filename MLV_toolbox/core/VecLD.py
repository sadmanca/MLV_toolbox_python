import numpy as np
from tabulate import tabulate

class VecLD:
    """
    A class to represent a vectorized linedrawing. 

    Attributes:
        originalImage (str): the original image as a string
        imsize (np.ndarray): the size of the image as a NumPy array
        lineMethod (str): the method used to detect lines in the image
        numContours (int): the number of contours in the image
        contours (np.ndarray): the contours of the image as a NumPy array
    """
    def __init__(
        self,
        originalImage: str = None,
        imsize: np.ndarray = None,
        lineMethod: str = None,
        numContours: int = None,
        contours: np.ndarray = None,
    ):
        """
        Initializes the VecLD class.

        Args:
            originalImage: the original image as a string
            imsize: the size of the image as a NumPy array
            lineMethod: the method used to detect lines in the image
            numContours: the number of contours in the image
            contours: the contours of the image as a NumPy array
        """
        self.originalImage = originalImage
        self.imsize = imsize
        self.lineMethod = lineMethod
        self.numContours = numContours
        self.contours = contours

    def __str__(self):
        """
        Returns a string representation of the VecLD class in a table.
        """
        headers = ["Variable", "Type", "Value"]
        data = [
            ["originalImage", type(self.originalImage).__name__, self.originalImage],
            ["imsize", type(self.imsize).__name__, self.imsize],
            ["lineMethod", type(self.lineMethod).__name__, self.lineMethod],
            ["numContours", type(self.numContours).__name__, self.numContours],
            ["contours", type(self.contours).__name__, self.contours.shape],
        ]
        return tabulate(data, headers=headers)

    def __eq__(self, other):
        """
        Compares two VecLD objects for equality.

        Args:
            other: the other VecLD object

        Returns:
            True if the objects are equal, False otherwise
        """
        return (
            self.originalImage == other.originalImage
            and np.array_equal(self.imsize, other.imsize)
            and self.lineMethod == other.lineMethod
            and self.numContours == other.numContours
            and np.array_equal(self.contours, other.contours)
        )
        return False
        