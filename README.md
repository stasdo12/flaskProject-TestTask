# Product Review Management API

This project provides a RESTful API for managing product information and reviews using Flask, Flask-RESTful, SQLAlchemy, and caching. The API allows users to retrieve detailed product information, view associated reviews, add new reviews, and paginate through the available reviews.

## Project Structure

- **app.py**: Main Flask application setup using Flask-RESTful. Defines API endpoints and initializes the database with sample data.

- **config.py**: Configuration for the Flask application, including the database URL.

- **database.py**: Initialization of the SQLAlchemy database and caching.

- **Dockerfile**: Specification for the Docker image used to run the Flask application.

- **docker-compose.yml**: Configuration of Docker services for the Flask application and PostgreSQL database.

- **models.py**: Definition of SQLAlchemy models for the `Product` and `Review` tables.

- **requirements.txt**: List of Python dependencies required for the project.

- **resources.py**: Implementation of the `ProductResource` class, a Flask-RESTful resource handling product and review-related endpoints.

## How to Run

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd yourproject
    ```

3. **Build and Run Docker Containers:**

    ```bash
    docker-compose up --build
    ```

    This command sets up the Flask application and the PostgreSQL database.

4. **Access the API:**

    Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the API.

## API Endpoints

- **GET /product/<int:product_id>**: Retrieve information about a specific product.

- **PUT /product/<int:product_id>**: Add a new review for a specific product.

## Database Initialization

To initialize the database with sample data, use the following command:

```bash
docker-compose exec app flask init-db
```

This command initializes the database and populates it with data from the provided CSV files.

## Environment Variables

Ensure that the necessary environment variables are set in the `.env` file or in your Docker Compose file. Check the `config.py` file for the required variables.

## Notes

- The application runs in debug mode, and the API can be accessed at [http://localhost:5000](http://localhost:5000).

- The PostgreSQL database is running in a Docker container.

Feel free to explore the code and customize it according to your needs. If you encounter any issues, refer to the troubleshooting section or the project documentation.

Happy coding!
