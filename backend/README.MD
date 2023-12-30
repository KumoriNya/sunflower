How to start the backend

(ONLY NEED TO DO THIS ONCE)

1. In the terminal have the "backend" folder be the root folder
2. Delete "backend.egg-info" and "venv" folders
3. In terminal type "pip install -e ."
4. Type "python -m venv venv"
5. type ". venv/bin/activate" (Linux) or "./venv/Scripts/activate" (Win) -
   Now should see "(venv) PS path\to\your\dir" in terminal
6. pip install -e .
7. Install requirements by "pip install -r requirements.txt"
   (You may need a modern version of python, I had 3.12 installed)

//////////
IMPORTANT
//////////
For any imports, the path should be as if the "root" folder is "backend".
E.g. If I want to import from user.py
path is "src.account_management.user"
In case 5 -> 6 doesn't work, do step 7 then step 6.
