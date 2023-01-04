## Requirements

- Python 3
- Git
- MongoDB Server

The `python` and `git` executables must be in the path, and the MongoDB
server must be started.

## Instructions

Create a new Python virtual environment:

    $ python -m venv venv

Then activate it:

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | `$ source <venv>/bin/activate`          |
|          | fish       | `$ source <venv>/bin/activate.fish`     |
|          | csh/tcsh   | `$ source <venv>/bin/activate.csh`      |
|          | PowerShell | `$ <venv>/bin/Activate.ps1`             |
| Windows  | cmd.exe    | `C:\> <venv>\Scripts\activate.bat`      |
|          | PowerShell | `PS C:\> <venv>\Scripts\Activate.ps1`   |

Then:

    $ py -m pip install -r requirements.txt 
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py shell -c "import setup_db" -- If you face some errors while doing this step, please ensure that the indexes 		created for the posted by and applicants in the database are not unique. If they are delete them. This can be done from the 	MongoDBCompass easily.
    $ python manage.py runserver

Sample users details:

| name       | password   | 
|------------|------------|
| admin      | admin      |
| Ali        | 123        |
| Hassan     | abc        | 
| Mohammed   | Mohammed   | 
| Nasser     | asdASD123  |
| Restaurant | 123        |
| DesignCo   | asdASD123  |
| aCompany   | 321        |