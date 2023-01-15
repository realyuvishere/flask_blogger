# BlogLite

A simple blogging web application.

## How to run the application
1. Open the terminal at the root folder
2. If there is no folder in the root directory by the name `.env`, create a virtual environment for the project to run in and install the dependencies from `requirements.txt`. The following methods can be used to execute this step:
    - **For *nix system users**, a Bash shell script named `setup.sh` exists in the root folder which does the setup by running it. To do it **manually**, execute the following commands in the given order:
    ```bash
    python3 -m venv .env
    source .env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
    - **For Windows users**, the setup can be done manually by using the following commands in the given order:
    ```bash
    python3 -m venv .env
    .env\scripts\activate.bat
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
3. Source the virtual environment in the terminal using either of the following methods:
    - **For *nix system users**, to complete this and the next step, the `run.sh` shell script, which is written in Bash, can be executed in the terminal. Optionally, this step can be completed **manually** by running either of the following commands:
        - `source .env/bin/activate`
        - `. .env/bin/activate`
    - **For Windows users**, running the following command in the terminal should suffice: `.env\scripts\activate.bat`

4. Run the `main.py` file using the following command: `python main.py`

## Technologies used
- Python v3.7.3
    - External dependencies are listed out in `requirements.txt`.
- HTML5, CSS3, JavaScript
- Bootstrap v5.0.2

## Folder structure and important files
- `main.py` is the main entry point of the app.
- `run.sh` is a `bash` script which contains instructions to run the server.
- `setup.sh` is a `bash` script which contains the instructions to do the initial setup for *nix based systems, or terminals which support `bash`.
- `requirements.txt` contains all the direct / indirect dependencies needed for the application to work.
- `README.md` is literally is the file you are reading right now.
- `/templates/` contains the HTML templates used for rendering views on the server.
- `/static/` contains the static resources like CSS and JS files necessary for functionality of the app. It also contains some media related to the app.
- `/docs/` contains the documentation of the API for the application.
- `/db/` contains the database used in the project.
- `/app/` contains the main components of the application.
- `/.env/` contains the virtual environment for running the application.
- `/app/api/` contains all the `flask-restful` API object declarations which can be imported anywhere in the project / application.
- `/app/config/` contains all the configurations / constants required to run the application. Any parameters can be directly changed in one of the files within the folder.
- `/app/controller/` contains the function declarations of various operations performed by the APIs, these can be used in the APIs or the rendered views.
- `/app/models/` contains the object models of the various schemas declared in the database.
- `/app/views/` contains all the routes at which the views will be rendered by `flask` and `jinja2`.
