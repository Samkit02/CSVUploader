
# CSV Uploader with Django and React

This project is a CSV uploader built using Django for the backend and React for the frontend. It allows users to upload a CSV file, which is then processed and stored in a database. The project also includes error handling and feedback for successful or failed file uploads.

## Features

- Upload CSV files from the frontend using React.
- Django backend processes and stores the CSV data in a database.
- CSRF protection enabled for secure requests.
- Simple user feedback for upload success or failure.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python (3.8+)
- Node.js (v14+)
- Django (5.0+)
- Docker (for running the project with Docker)

## Getting Started

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/csv_uploader.git
cd csv_uploader
```

### 2. Backend (Django) Setup

#### Install Django and Other Dependencies

```bash
pip install -r requirements.txt
```

#### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Create a Superuser (Optional for Admin Access)

```bash
python manage.py createsuperuser
```

#### Run the Django Server

```bash
python manage.py runserver
```

The Django server should now be running on `http://localhost:8000`.

### 3. Frontend (React) Setup

#### Navigate to the `frontend` Directory

```bash
cd frontend
```

#### Install Node.js Dependencies

```bash
npm install
```

#### Start the React Development Server

```bash
npm start
```

The React development server will be running on `http://localhost:3000`.

### 4. Access the Application

- Go to `http://localhost:3000` to view the frontend.
- You can upload a CSV file from the frontend form.
- After successful upload, visit `http://localhost:8000/admin` to view the uploaded data (if admin access is set up).

### Django Admin Credentials

To access the Django admin panel and check the uploaded data, use the following superuser credentials:

- **Username**: `samkitshah`
- **Password**: `S@mkit123`

## Example CSV File Format

I have added the sample_data.csv in the Repo.

## Running the Project with Docker

You can also run the project using Docker, which will containerize both the Django and React apps.

### Running with Docker Compose

To run the whole project using Docker Compose:

```bash
docker-compose up --build
```

This will build and run both the Django backend and React frontend, exposing them on `http://localhost:8000` and `http://localhost:3000` respectively.
