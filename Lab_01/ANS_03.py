def calculate_distance_squared(point):
    """Calculate the square of the Euclidean distance of a point from the origin."""
    x, y = point
    return x**2 + y**2

def furthest_points(points):
    """Find the furthest and second furthest points from the origin."""
    if len(points) < 2:
        raise ValueError("At least two points are required.")

    # Initialize variables to store the furthest and second furthest points
    furthest = points[0]
    second_furthest = points[1]

    # Calculate initial distances
    max_distance = calculate_distance_squared(furthest)
    second_max_distance = calculate_distance_squared(second_furthest)

    # Ensure `furthest` has the larger distance initially
    if second_max_distance > max_distance:
        furthest, second_furthest = second_furthest, furthest
        max_distance, second_max_distance = second_max_distance, max_distance

    # Iterate through the remaining points
    for point in points[2:]:
        distance = calculate_distance_squared(point)

        if distance > max_distance:
            # Update both furthest and second furthest
            second_furthest = furthest
            second_max_distance = max_distance

            furthest = point
            max_distance = distance
        elif distance > second_max_distance:
            # Update only the second furthest
            second_furthest = point
            second_max_distance = distance

    return furthest, second_furthest

# Example Inputs and Outputs
points1 = [[0, 0], [0, 1], [-2, 0]]
points2 = [[3, 3], [5, -1], [-2, 4]]
points3 = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1]]

# Test Cases
print(furthest_points(points1))  # Output: ([-2, 0], [0, 1])
print(furthest_points(points2))  # Output: ([5, -1], [-2, 4])
print(furthest_points(points3))  # Output: ([-1, -1], [1, 0] or similar depending on distances)
