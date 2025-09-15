def sort(width, height, length, mass):
    # Calculate the volume of the package
    volume = width * height * length
    # Check if the package is bulky
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    # Check if the package is heavy
    heavy = mass >= 20
    # Use ternary operator to determine the result
    return "REJECTED" if bulky and heavy else ("SPECIAL" if bulky or heavy else "STANDARD")
    # Return "REJECTED" if both bulky and heavy, else "SPECIAL" if either, else "STANDARD"
