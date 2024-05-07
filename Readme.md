# Coffee & Wifi - Flask Web Application

The "Coffee & Wifi" application is a Flask-based web project that helps users find cafes with amenities like good coffee, strong WiFi, and ample power sockets. The application uses Flask, Bootstrap5 for styling, and WTForms for handling form data.

## Output


https://github.com/sarvesh-2109/coffee-and-wifi/assets/113255836/581ebabb-83f8-4e6d-b60c-edd6b39bc3ad


## Project Structure

The project is structured into several key components including Python scripts, HTML templates, a CSS stylesheet, and a CSV file for data storage. Below is an outline of the major components:

- `main.py`: Contains the Flask application setup, routes, and form definitions.
- `templates/`: Contains HTML files for rendering views.
- `static/css/`: Contains custom CSS files for styling.
- `cafe-data.csv`: Stores data about cafes added via the web form.

## Features

- **Home Page**: Displays a welcome message and a button to view all cafes.
- **Add Cafe**: Allows users to add new cafes by filling out a form.
- **View Cafes**: Displays a table of all cafes with details such as name, location, coffee rating, etc.

## Installation and Setup

To set up and run the project locally, follow these steps:

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Clone the Repository

```bash
git clone https://github.com/sarvesh-2109/coffee-and-wifi.git
cd coffee-and-wifi
```

### Install Required Packages

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

### Run the Application

Start the Flask application with the following command:

```bash
python main.py
```

Navigate to `http://127.0.0.1:5000/` in your web browser to view the application.

## Usage

Once the application is running, you can:

- **View the Home Page** by accessing the root URL `/`.
- **Add a Cafe** by clicking on the 'Add a new cafe' link and filling out the form.
- **View All Cafes** where each cafe's details are listed, and Google Maps links are provided for locations.

## Contributing

Contributions to improve the application are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

