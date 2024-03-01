# LearningDjango

## Description

LearningDjango is a web application that offers a score table feature. Users can perform CRUD operations (Create, Read, Update, Delete) on student records, including student names and scores. This project was created by following the excellent 'FREE Django Tutorial for Beginners' video series made by Tony from the YouTube channel 'Tony Teaches Tech'. This README provides detailed instructions on setting up the project locally and utilizing its features.

## Features

- View a table of student names and scores.
- Add new students to the table.
- Edit existing student records.
- Delete student records.

## Prerequisites

Before getting started, ensure the following prerequisites are met:

- Python 3.x is installed.
- Git is installed.

### Getting Started
```bash
# Clone the repository
git clone https://github.com/maheshram-hs/LearningDjango.git
cd yourproject

# Create a virtual environment
python -m venv venv  # You can use "python3" instead of "python" on some systems

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Application
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your web browser.

## Usage

1. Open the website and view the student score table.
2. Use the "Add" button to add a new student, providing a name and score.
3. Use the "Edit" and "Delete" buttons to modify or remove existing student records.
4. Save the changes by clicking the "Save" button.

## Contributing

If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgments

This project was created by following the excellent tutorials made by Tony from the YouTube channel 'Tony Teaches Tech' for his "FREE Django Tutorial for Beginners" video series.
