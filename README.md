
# AI Image Generator

This application generates images based on user-provided text prompts using OpenAI's DALL-E API. It provides a simple web interface where users can input their prompts and view the generated images.

## Features
- Generate AI images from text prompts.
- Save generated images locally.
- Simple web interface for user interaction.

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Web framework for building the application.
- **OpenAI API**: For generating images using the DALL-E model.
- **Pillow**: For image processing and saving.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required dependencies:
   ```bash
   pip install flask openai pillow
   ```
3. Set your OpenAI API key:
   Replace `'your_openai_api_key'` in `app.py` with your actual OpenAI API key.
4. Run the application:
   ```bash
   python app.py
   ```
5. Access the application:
   Open `http://127.0.0.1:5000` in your web browser.

## How It Works
1. Users enter a text prompt into the web form.
2. The prompt is sent to the server, which uses OpenAI's DALL-E API to generate an image.
3. The generated image is saved locally and displayed to the user.

## Example
- Prompt: "A futuristic cityscape at sunset"
- Output: ![Example Image](generated_images/example.png)

## License
This project is licensed under the MIT License.
