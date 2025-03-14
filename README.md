# Country_Info_API_Redis

A Django REST API for managing country-related information. This API provides endpoints for retrieving, creating, updating, and deleting countries along with essential data such as population, capital, area, climate, GDP, and more.

## Features

- **Django Framework**: Built using Django 5.1.7.
- **RESTful API**: Uses Django REST Framework for creating API endpoints.
- **Caching**: Redis caching is implemented to optimize data retrieval.
- **Database**: PostgreSQL database for storing country data.
- **Environment Variables**: Uses `.env` files to manage secret keys and database configurations.

## API Endpoints

1. **List and Create Countries**
   - **GET** `/api/` - List all countries.
   - **POST** `/api/` - Create a new country.

2. **Retrieve, Update, or Delete Country**
   - **GET** `/api/{id}/` - Retrieve details of a country by ID.
   - **PUT** `/api/{id}/` - Update details of a country by ID.
   - **DELETE** `/api/{id}/` - Delete a country by ID.

3. **Retrieve Country by Name**
   - **GET** `/api/{name}/` - Retrieve details of a country by name.

## Installation

1. Clone the repository:
   git clone https://github.com/anageguchadze/Country_Info_API_Redis.git
   cd Country_Indo_API_Redis

Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Set up environment variables:
Create a .env file in the root directory and add the following:
plaintext
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port

Run migrations:
python manage.py migrate

Start the development server:
python manage.py runserver
Caching with Redis

This project uses Redis for caching. To set up Redis:
Install Redis on your system.
Update the .env file with your Redis URL:
plaintext
REDIS_URL=redis://localhost:6379/1

Usage
Use curl, Postman, or any HTTP client to interact with the API endpoints.
Example: Get all countries
curl -X GET http://127.0.0.1:8000/api/
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
