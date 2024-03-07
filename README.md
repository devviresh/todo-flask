# Flask Todo App with PostgreSQL

This is a simple Todo application built with Flask and PostgreSQL. It allows users to manage their tasks by performing CRUD operations (Create, Read, Update, Delete).

## Features

- Add new tasks
- View existing tasks
- Delete tasks
- Update tasks

## Setup

1. **Clone the repository**:

   ```bash
   git clone [<repository_url>](https://github.com/devviresh/todo-flask.git)
   cd todo-flask
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the PostgreSQL database**:

   - Install PostgreSQL if you haven't already.
   - Create a new database for the application.
   - Set the `DATABASE_URL` environment variable to point to your PostgreSQL database.

4. **Run the application**:

   ```bash
   python wsgi.py
   ```

   The application should now be running locally. You can access it at `http://localhost:5000`.

## Configuration

- `DATABASE_URL`: Set this environment variable to the PostgreSQL connection URI of your database.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
