## Description

This Django project is developed using Test-Driven Development (TDD) methodology.

## Technologies Used

- Django
- Python


## Packages / Libraries Used

- django-extensions - To run python scripts, ex: for creating objects in database
- django-crispy-forms - To style the django form
- Faker - To get access to the fake data
- libgravatar - To create an avatar, based on picture linked to the email.
- model-bakery - To create model data.
- coverage - To get the consolidated test reports.


## Setup Instructions

To run this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Run database migrations: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`

## Running Tests

To run tests for this project, execute the following command:

```bash
python manage.py test
