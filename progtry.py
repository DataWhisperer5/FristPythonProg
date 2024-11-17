from PIL import Image
from guizero import App, Picture, PushButton, Box

# Resize the image dynamically
img_path = r"C:\Users\gonza\Downloads\manja-vitolic-gKXKBY-C-Dk-unsplash.jpg"
img = Image.open(img_path)
img = img.resize((300, 200))  # Adjust width and height
resized_img_path = "resized_image.jpg"
img.save(resized_img_path)

# Function for each button
def button1_action():
    print("Button 1 clicked!")

def button2_action():
    print("Button 2 clicked!")

def button3_action():
    print("Button 3 clicked!")

# Create the main app window
app = App(title="Picture and Buttons", width=400, height=500)

# Add a Picture widget with the resized image
picture = Picture(app, image=resized_img_path, align="top")

# Create a Box to hold the buttons at the bottom
button_box = Box(app, align="bottom", layout="grid")

# Add buttons to the box
button1 = PushButton(button_box, text="Button 1", command=button1_action, grid=[0, 0])
button2 = PushButton(button_box, text="Button 2", command=button2_action, grid=[1, 0])
button3 = PushButton(button_box, text="Button 3", command=button3_action, grid=[2, 0])

# Run the app
app.display()


