# main.py
def sort(width, height, length, mass):
    # Calculate the volume of the package
    volume = width * height * length
    
    # Check if the package is bulky
    is_bulky = (volume >= 1000000) or (width >= 150) or (height >= 150) or (length >= 150)
    
    # Check if the package is heavy
    is_heavy = mass >= 20
    
    # Determine the stack based on the conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
print(sort(10, 10, 10, 5))        # Output: "STANDARD"
print(sort(100, 100, 100, 10))    # Output: "SPECIAL"
print(sort(10, 10, 10, 25))       # Output: "SPECIAL"
print(sort(200, 200, 200, 25))    # Output: "REJECTED"