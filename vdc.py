import random
from PIL import Image, ImageDraw, ImageFont

def create_dhanteras_greeting():
    # List of Diwali-themed images
    images = ["diwali1.jpg", "diwali2.jpg", "diwali3.jpg"]  # Add paths to your images
    selected_image = random.choice(images)  # Randomly select an image

    # Open the selected image
    img = Image.open(selected_image)
    draw = ImageDraw.Draw(img)

    # Define the text and font
    text = "Happy Dhanteras!"
    font = ImageFont.truetype("arial.ttf", 50)  # You may need to adjust the font path

    # Calculate text position
    textwidth, textheight = draw.textsize(text, font)
    width, height = img.size
    x = (width - textwidth) / 2
    y = height - textheight - 20  # Position text at the bottom of the image

    # Add text to the image
    draw.text((x, y), text, font=font, fill="yellow")

    # Show or save the image with the greeting
    img.show()  # Opens the image
    img.save("dhanteras_greeting.jpg")  # Saves the image with the greeting

create_dhanteras_greeting()
