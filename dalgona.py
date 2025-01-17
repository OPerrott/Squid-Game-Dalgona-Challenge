from PIL import Image

# Global lists to store pixel data
TRIANGLE = []
SQUARE = []
DIAMOND = []
CIRCLE = []
UNICORN = []
ELEPHANT = []
COOKIEOFGOD = []
MONALISA = []

def initialise_dalgona(dalgona_name):
    """
    Initializes the dalgona by analyzing the corresponding image file.
    
    :param dalgona_name: Name of the dalgona shape (Triangle, Square, Diamond, Circle)
    """
    image_path = ""

    # Determine the image path based on the dalgona name
    if dalgona_name == "Triangle":
        image_path = r"resources\dalgona_files\Triangle.Dalgoma.png"
    elif dalgona_name == "Square":
        image_path = r"resources\dalgona_files\Square.Dalgoma.png"
    elif dalgona_name == "Diamond":
        image_path = r"resources\dalgona_files\Diamond.Dalgoma.png"
    elif dalgona_name == "Circle":
        image_path = r"resources\dalgona_files\Circle.Dalgoma.png"
    elif dalgona_name == "Unicorn":
        image_path = r"resources\dalgona_files\Unicorn.Dalgoma.png"
    elif dalgona_name == "Elephant":
        image_path = r"resources\dalgona_files\Elephant.Dalgoma.png"
    elif dalgona_name == "CookieOfGod":
        image_path = r"resources\dalgona_files\CookieOfGod.Dalgoma.png"
    elif dalgona_name == "Monalisa":
        image_path = r"resources\dalgona_files\Monalisa.Dalgoma.png"
    else:
        print(f"Invalid dalgona name: {dalgona_name}")
        return

    analyse_dalgona_file(image_path, dalgona_name)

def analyse_dalgona_file(image_path, dalgona_name):
    """
    Analyzes the dalgona image file and stores pixel data.
    
    :param image_path: Path to the image file
    :param dalgona_name: Name of the dalgona shape
    """
    global TRIANGLE, SQUARE, DIAMOND, CIRCLE, UNICORN, ELEPHANT, COOKIEOFGOD, MONALISA

    try:
        # Open and process the image
        with Image.open(image_path) as img:
            img = img.convert("RGB")  # Ensure the image is in RGB mode
            width, height = img.size

            # Process each pixel row
            for y in range(height):
                width_loop = []  # Create a new list for each row
                for x in range(width):
                    r, g, b = img.getpixel((x, y))  # Get the RGB values

                    # Determine the pixel value
                    if r == 0 and g == 0 and b == 0:  # Black
                        width_loop.append(0)
                    elif r == 255 and g == 244 and b == 77:  # Specific yellow color
                        width_loop.append(1)
                    else:
                        width_loop.append(0)  # Unspecified color, optional for debugging

                # Append the row data to the corresponding list
                if dalgona_name == "Triangle":
                    TRIANGLE.append(width_loop)
                elif dalgona_name == "Square":
                    SQUARE.append(width_loop)
                elif dalgona_name == "Diamond":
                    DIAMOND.append(width_loop)
                elif dalgona_name == "Circle":
                    CIRCLE.append(width_loop)
                elif dalgona_name == "Unicorn":
                    UNICORN.append(width_loop)
                elif dalgona_name == "Elephant":
                    ELEPHANT.append(width_loop)
                elif dalgona_name == "CookieOfGod":
                    COOKIEOFGOD.append(width_loop)
                elif dalgona_name == "Monalisa":
                    MONALISA.append(width_loop)

        print(f"Analysis complete for: {dalgona_name}")

    except FileNotFoundError:
        print(f"File not found: {image_path}")
    except Exception as e:
        print(f"Error processing file {image_path}: {e}")

# Example usage:
if __name__ == "__main__":
    initialise_dalgona("Triangle")
    initialise_dalgona("Square")
    initialise_dalgona("Diamond")
    initialise_dalgona("Circle")
    initialise_dalgona("Unicorn")
    initialise_dalgona("Elephant")
    initialise_dalgona("CookieOfGod")
    initialise_dalgona("Monalisa")
    

    # Print the processed data (optional)
    print("Triangle data:", TRIANGLE)
    print("Square data:", SQUARE)
    print("Diamond data:", DIAMOND)
    print("Circle data:", CIRCLE)
    print("Unicorn data:", UNICORN)
    print("Elephant data:", ELEPHANT)
    print("CookieOfGod data:", COOKIEOFGOD)
    print("Monalisa data:", MONALISA)
