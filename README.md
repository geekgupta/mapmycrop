
```markdown
# MapMyCrop Assignment

This project uses Django and is dockerized for Kubernetes deployment on the Google Cloud Platform (GCP).

## Setup

### Using GitHub
Clone this repository:
```bash
git clone https://github.com/geekgupta/mapmycrop.git
```

### Using Docker
Pull the Docker image:
```bash
docker pull  puru21/crop:0.0.1
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

