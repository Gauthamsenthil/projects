import math

def find_circumference(radius):
    """
    Calculate the circumference of a circle given its radius.
    
    Formula: C = 2 * π * r
    """
    return 2 * math.pi * radius

# Example usage:
r = 5
print(f"The circumference of a circle with radius {r} is {find_circumference(r):.2f}")
