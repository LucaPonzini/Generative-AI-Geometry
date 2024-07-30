Generative AI Procedural Geometry
=================================

This project is a simple Flask web application that generates and displays random geometric shapes using Python and Matplotlib. The generated shapes include circles, squares, triangles, and polygons with random parameters.

Features
--------

- Generate random geometric shapes (circles, squares, triangles, polygons).
- Display the generated shape directly on the web page.

Requirements
------------

- Python 3.6+
- Flask
- Matplotlib
- Numpy

Installation
------------

1. Clone the repository or download the source code.

    git clone https://github.com/yourusername/Generative-AI-Geometry.git
    cd Generative-AI-Geometry

2. Create a virtual environment (optional but recommended).

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages.

    pip install flask matplotlib numpy

Usage
-----

1. Run the Flask application.

    python app.py

2. Open a web browser and navigate to `http://127.0.0.1:5000`.

3. Click the "Generate Image" button to generate and display a random geometric shape.

Project Structure
-----------------

Generative-AI-Geometry/
├── app.py                 # Main Flask application
├── model.py               # Generative model (not used in the current version)
├── templates/
│   └── index.html         # HTML template for the web page
└── README.txt             # Project README file

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
---------------

- Flask (https://flask.palletsprojects.com/) - Micro web framework used for the web application.
- Matplotlib (https://matplotlib.org/) - Library used for generating and plotting shapes.
- Numpy (https://numpy.org/) - Library used for numerical operations.
