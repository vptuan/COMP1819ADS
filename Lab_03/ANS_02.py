import math

def closest_point_to_line(a, b, c, points):
    """
    Finds the point closest to the line represented by the equation ax + by + c = 0.

    Parameters:
        a (float): Coefficient of x in the line equation.
        b (float): Coefficient of y in the line equation.
        c (float): Constant term in the line equation.
        points (list): List of points, where each point is represented as [x, y].

    Returns:
        list: The closest point to the line.
    """
    def distance_to_line(x, y):
        """
        Calculates the distance between a point (x, y) and the line ax + by + c = 0.
        """
        return abs(a * x + b * y + c) / math.sqrt(a**2 + b**2)

    # Initialize variables to store the closest point and its distance
    closest_point = None
    min_distance = float('inf')

    # Iterate through all points to find the closest one
    for point in points:
        x, y = point
        distance = distance_to_line(x, y)
        if distance < min_distance:
            min_distance = distance
            closest_point = point

    return closest_point

# Example usage
a, b, c = 2, 3, -4
points = [[0, -1], [3, 1], [-2, 0]]

closest_point = closest_point_to_line(a, b, c, points)
print("Closest point to the line:", closest_point)