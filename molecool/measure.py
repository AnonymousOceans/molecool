"""Measuring angles and distances for the rest of the package."""

import numpy as np

"""Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    """

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
    
def calculate_distance(pointA, pointB):
    # This function calculates the distance between two points given as numpy arrays.

    """Calculate the distance between two points.

    Parameters
    ----------
    pointA, pointB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> point1 = np.array([0, 0, 0])
    >>> point2 = np.array([0, 0.1, 0])
    >>> calculate_distance(point1, point2)
    0.1
    """

    distance = pointA - pointB
    finaldistance = np.linalg.norm(distance)

    return finaldistance
