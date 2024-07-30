from flask import Flask, render_template, Response
import io
import base64
import matplotlib.pyplot as plt
import numpy as np
import logging
import random

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def generate_random_shape():
    fig, ax = plt.subplots()

    # Randomly select a shape type
    shape_type = random.choice(['circle', 'square', 'triangle', 'polygon'])

    if shape_type == 'circle':
        circle = plt.Circle((0.5, 0.5), 0.4, color='blue', fill=True)
        ax.add_artist(circle)
    elif shape_type == 'square':
        square = plt.Rectangle((0.1, 0.1), 0.8, 0.8, color='green', fill=True)
        ax.add_artist(square)
    elif shape_type == 'triangle':
        triangle = plt.Polygon([[0.5, 0.9], [0.1, 0.1], [0.9, 0.1]], color='red', fill=True)
        ax.add_artist(triangle)
    elif shape_type == 'polygon':
        num_sides = random.randint(5, 8)
        angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False).tolist()
        points = [(0.5 + 0.4 * np.cos(angle), 0.5 + 0.4 * np.sin(angle)) for angle in angles]
        polygon = plt.Polygon(points, color='purple', fill=True)
        ax.add_artist(polygon)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    plt.axis('off')

    # Save the generated image to the buffer
    file_obj = io.BytesIO()
    plt.savefig(file_obj, format='png')
    plt.close(fig)
    file_obj.seek(0)
    logging.debug(f'{shape_type.capitalize()} image generated and saved to buffer')

    return file_obj

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    try:
        file_obj = generate_random_shape()

        # Encode the image to base64 string
        encoded_img = base64.b64encode(file_obj.getvalue()).decode('utf-8')
        img_str = f'data:image/png;base64,{encoded_img}'
        
        return render_template('index.html', image=img_str)
    except Exception as e:
        logging.error(f'Error during image generation: {e}')
        return Response(f'Error: {e}', status=500)

if __name__ == '__main__':
    app.run(debug=True)
