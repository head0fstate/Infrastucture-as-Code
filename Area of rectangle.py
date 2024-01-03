def calculate_rectangle_area(length, width):
    area = length * width
    return area

if __name__ == "__main__":
    try:
        # Get user input for length and width
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        
        # Calculate the area
        area = calculate_rectangle_area(length, width)
        
        # Display the result
        print(f"The area of the rectangle with length {length} and width {width} is: {area}")
    except ValueError:
        print("Please enter valid numerical values for length and width.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
