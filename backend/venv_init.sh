rm -r ./backend-egg-info
rm -r ./venv
pip install -e .
python -m venv venv
pip install -e .
pip install -r requirements.txt