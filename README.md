# Game1

This is my first look into the phaser javascript game engine. The static files are from the phaser tutorial. The web-server is Flask. 

## Install

Create and activate a virtual environment (optional).

```bash
virtualenv -p python3 venv
. venv/bin/activate
```

Install Flask

```bash
pip install -r requirements.txt
```

## Run

Run the dev server

```bash
FLASK_ENV=development FLASK_APP=server flask run
```

## Play the game

The default port if `5000`. If the server is running, the game should be accessible at: [http://127.0.0.1:5000/part1.html](http://127.0.0.1:5000/part1.html)
