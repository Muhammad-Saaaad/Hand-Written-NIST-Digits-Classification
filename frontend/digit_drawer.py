import os
import sys

import django
from io import BytesIO
import logging
from PIL import Image, ImageDraw
import re
import requests
import tkinter as tk
from tkinter import Canvas, Button, Label, Frame

# Add the core directory to the path so we can import the Classification class
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'core'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from myapp.Classifier import Classification


logging.basicConfig(format='%(message)s', level=logging.INFO)

class DigitDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwritten Digit Recognition")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Set up the canvas for drawing
        self.canvas_frame = Frame(self.root, bd=2, relief=tk.RAISED)
        self.canvas_frame.pack(pady=10)
        
        self.canvas_width = 280
        self.canvas_height = 280
        self.canvas = Canvas(self.canvas_frame, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()
        
        # Create a blank image for drawing
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), color=0)
        self.draw = ImageDraw.Draw(self.image)
        
        # Bind mouse events for drawing
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        
        # Control buttons
        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=10)
        
        self.clear_button = Button(self.button_frame, text="Clear", command=self.clear_canvas, width=10, height=2)
        self.clear_button.grid(row=0, column=0, padx=10)
        
        self.predict_button = Button(self.button_frame, text="Predict", command=self.predict_digit, width=10, height=2)
        self.predict_button.grid(row=0, column=1, padx=10)
        
        # Result display
        self.result_frame = Frame(self.root)
        self.result_frame.pack(pady=10)
        
        self.result_label = Label(self.result_frame, text="Draw a digit and click Predict", font=("Arial", 16))
        self.result_label.pack()
        
        self.confidence_label = Label(self.result_frame, text="", font=("Arial", 12))
        self.confidence_label.pack()
        
        # Drawing variables
        self.last_x = None
        self.last_y = None
        self.line_width = 15
        
        # Initialize the classifier
        self.classification = Classification()
    
    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y
    
    def draw_line(self, event):
        if self.last_x and self.last_y:
            x, y = event.x, event.y
            # Draw on canvas
            self.canvas.create_line(self.last_x, self.last_y, x, y, 
                                   fill="white", width=self.line_width, 
                                   capstyle=tk.ROUND, smooth=tk.TRUE)
            # Draw on image
            self.draw.line([self.last_x, self.last_y, x, y], 
                          fill=255, width=self.line_width)
            self.last_x = x
            self.last_y = y
    
    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), color=0)
        self.draw = ImageDraw.Draw(self.image)
        self.result_label.config(text="Draw a digit and click Predict")
        self.confidence_label.config(text="")
    
    def predict_digit(self):
        # Save the drawn image to a BytesIO object for API request
        img_file = BytesIO()
        self.image.save(img_file, format='PNG')
        img_file.seek(0)
        
        # Prepare the data for the API request
        files = {'image': ('digit.png', img_file, 'image/png')}
        
        try:
            # Send the request to the API endpoint
            response = requests.post('http://localhost:8001/api/Predict_Image/', files=files)
            
            if response.status_code == 201:
                # Parse the response to get prediction results
                response_data = response.json()
                message = response_data.get('message', '')
                
                # Extract predicted number and accuracy from the message
                # Message format: "Digit predicted => {predicted_number} with accuracy {accuracy_score:.2f} and saved Sucessfully"
                predicted_number_match = re.search(r'Digit predicted => (\d+)', message)
                accuracy_match = re.search(r'with accuracy ([0-9.]+)', message)
                
                if predicted_number_match and accuracy_match:
                    predicted_number = predicted_number_match.group(1)
                    accuracy_score = accuracy_match.group(1)
                    
                    # Update result display
                    self.result_label.config(text=f"Predicted Digit: {predicted_number}")
                    self.confidence_label.config(text=f"Confidence: {accuracy_score}")
                    
                    logging.info(f"Successfully received prediction from API: {predicted_number} with accuracy {accuracy_score}")
                else:
                    self.result_label.config(text="Could not parse prediction")
                    self.confidence_label.config(text="")
                    console_logger.warning(f"Could not parse prediction from response: {message}")
            else:
                self.result_label.config(text="API Error")
                self.confidence_label.config(text=f"Status: {response.status_code}")
                console_logger.error(f"API error: {response.status_code} - {response.text}")
                
        except Exception as e:
            self.result_label.config(text="Connection Error")
            self.confidence_label.config(text="")
            console_logger.error(f"Error calling API: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitDrawer(root)
    root.mainloop()