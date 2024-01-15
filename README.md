# MapMyCrop Assignment

This project uses Django, Django REST framework, and is dockerized for Kubernetes deployment on the Google Cloud Platform (GCP).

## Setup

### Using GitHub
Clone this repository:
```bash
git clone https://github.com/geekgupta/mapmycrop.git
cd mapmycrop
```

### Using Docker
Pull the Docker image:
```bash
docker pull puru21/crop:0.0.1
```

## Installation

### Manual Installation
1. Create a virtual environment.
2. Run:
   ```bash
   pip install -r requirements.txt
   ```

### Using Docker
Run:
```bash
docker-compose up
```

## Start the Project
Run:
```bash
python manage.py runserver
```

## Deployment
The project is deployed on [http://34.135.164.165/](http://34.135.164.165/) using Kubernetes on GCP.

---

## Features

1. **Framework Selection:**
   - Django was chosen as the web framework due to its robustness, built-in authentication features, and extensive ecosystem. It is well-suited for building secure web applications.

2. **User Registration:**
   - Implemented an endpoint for user registration, allowing users to register with a unique username and a securely hashed password.

3. **User Authentication:**
   - Created an authentication endpoint that validates user credentials (username and password) and returns a JWT token upon successful authentication. The token has a specified expiration duration for security.

4. **Token-based Authorization:**
   - Implemented a secure endpoint that requires a valid JWT token for access. Only authenticated users with a valid token can access this endpoint.

5. **API Integration:**
   - Utilized Open Meto (https://open-meteo.com/) to get historic weather data. The weather data API endpoint is accessible at `/weather/`.

6. **Input Validation and Error Handling:**
   - Proper input validation is implemented for user registration and authentication endpoints. Meaningful error messages are returned in case of validation failures or other errors, enhancing the user experience.

7. **Security Considerations:**
   - Implemented security measures to protect against common web vulnerabilities such as SQL injection, CSRF, and ensured secure password storage through password hashing. JSON Web Tokens (JWT) are used for secure authentication.

8. **Unit Testing:**
   - Wrote unit tests to validate the functionality of various endpoints, ensuring good test coverage and maintaining code reliability.

## Usage

### User Authentication

1. **Login:**
   - Use the following API endpoint for user login to obtain a JWT token:
     - POST http://127.0.0.1:8000/account/login/
     - Request Body:
       ```json
       {
           "username": "guptron1@gmail.com",
           "password": "12345678"
       }
       ```
2. **Registration:**
   - Use the following API endpoint for user registration:
     - POST http://127.0.0.1:8000/account/registration/
     - Request Body:
       ```json
       {
           "first_name": "purushottam",
           "last_name": "Gupta",
           "email": "guptron4@gmail.com",
           "password": "Puru21shiv"
       }
       ```

### Weather Data

1. **Get Weather Data:**
   - Use the following API endpoint to get historic weather data (after logging in and obtaining a token):
     - POST http://127.0.0.1:8000/weather/
     - Request Body:
       ```json
       {
           "latitude": 52.52,
           "longitude": 13.41,
           "start_date": "2023-12-30",
           "end_date": "2024-01-13",
           "hourly": "temperature_2m"
       }
       ```
   - Make sure to include the obtained JWT token in the Authorization header.

### Deployment

- Access the deployed application on [http://34.135.164.165/](http://34.135.164.165/).

Feel free to reach out if you have any questions or encounter issues during setup and usage.
