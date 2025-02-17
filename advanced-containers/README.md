Advanced Containers: Flask API with PostgreSQL and Docker
Project Overview
This project sets up a simple Flask API that allows for the creation and retrieval of users. The application connects to a PostgreSQL database running inside a Docker container. We use Docker Compose to orchestrate both the Flask application and the PostgreSQL database, making it easy to run and manage the project. Additionally, we include the option of a basic Nginx load balancer for scaling the application.

Installation Instructions
Prerequisites
To get started, you'll need the following installed on your machine:

Docker
Docker Compose
Git
Setting Up the Project
Clone the Repository

If you haven't already, clone this repository to your local machine:

bash
Copy
Edit
git clone <your-repository-url>
cd advanced-containers
Install Dependencies

The dependencies are listed in requirements.txt. These are installed when you build the Docker containers using Docker Compose.

Building and Running the Containers
Start the Containers

To bring up the project, use Docker Compose to build and start the containers:

bash
Copy
Edit
docker-compose up -d
This command will:

Build the Flask application image
Start the PostgreSQL container
Start the Flask application container
Check Logs (Optional)

You can check the logs of the containers using:

bash
Copy
Edit
docker-compose logs
Access the API

The Flask application will be running at http://localhost:5000. The database is connected, and the tables are created.

API Usage Examples
Create a New User
You can create a new user by sending a POST request to the /user endpoint:

bash
Copy
Edit
curl -X POST http://localhost:5000/user -H "Content-Type: application/json" -d "{\"first_name\": \"John\", \"last_name\": \"Doe\"}"
This will create a user with the first name "John" and last name "Doe". The response will contain the user's ID, first name, and last name.

Retrieve a User by ID
To retrieve a user by their ID, send a GET request to the /user/<id> endpoint:

bash
Copy
Edit
curl -X GET http://localhost:5000/user/1
Replace 1 with the actual user ID. The response will contain the user's details (ID, first name, last name) if the user is found.

Error Handling
If the user does not exist, the API will return a 404 Not Found status with the following response:

json
Copy
Edit
{
  "error": "User not found"
}
Nginx Load Balancer (Optional)
If you want to scale the application with Nginx, ensure that Nginx is running by modifying the docker-compose.yml file. Here's the configuration for the Nginx service:

yaml
Copy
Edit
nginx:
  image: nginx:alpine
  container_name: nginx_proxy
  ports:
    - "80:80"
  depends_on:
    - web
  volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
  networks:
    - app_network
The nginx.conf file includes a simple reverse proxy setup to forward requests to the Flask app.

Security Best Practices
Non-root users: The Dockerfile uses a non-root user (appuser) to run the application, following best security practices.
Secrets Management: Passwords and other sensitive data should be stored in environment variables rather than hardcoded in the codebase.
Minimal Base Image: The python:3.9-slim image is used to minimize the size of the application image.
Network Isolation: The application containers (Flask app and PostgreSQL database) are on an isolated network (app_network), ensuring communication between them but not with other containers on your system.
Scaling and Deployment
The project can be scaled by increasing the number of Flask application containers using Docker Compose. For production, you may want to configure a more robust load balancing and container orchestration solution like Kubernetes.