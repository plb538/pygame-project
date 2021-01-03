# Initial Setup Instructions

1. Got to `https://www.python.org/downloads/` and download Python3. 
    
    NOTE: Ensure you select *Add Python to PATH*

    ![Python Download Wizard](./resources/readme/python_instructions.png "Add Python to Path")


2. Run the following in the Windows cmdline to update your Python package manager and install the required dependencies:

```
python -m pip install -U pip
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
```

# Running the Game

1. Run the following in the Windows cmdline to source the appropriate Python virtual environment (to gain access to the installed dependencies):

```
.\venv\Scripts\activate
```

2. Run the following in the Windows cmdline to start the game:

```
python main.py
```