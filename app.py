
from flask import Flask, render_template, request, jsonify
import openai
import os
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

# Set OpenAI API Key
openai.api_key = 'your_openai_api_key'

# Directory to save generated images
IMAGE_DIR = 'generated_images'
os.makedirs(IMAGE_DIR, exist_ok=True)

@app.route('/')
def index():
    """
    Renders the homepage where users can input prompts.
    """
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    """
    Handles the generation of an image based on a text prompt.
    """
    prompt = request.form['prompt']
    try:
        # Call the DALL-E API
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        
        # Decode the image and save it
        image_data = response['data'][0]['image']
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        image_path = os.path.join(IMAGE_DIR, f"{prompt.replace(' ', '_')}.png")
        image.save(image_path)
        
        return jsonify({'message': 'Image generated successfully', 'image_path': image_path})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
