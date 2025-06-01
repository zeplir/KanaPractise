# KanaPractise

## Project Info

### Purpose
The purpose of this project are essentially two things.
1. Dive into some fullstack development.
2. Learn Japanese.
Essentially two things I'm really interested in.

### Backend
The backend in written in python using flask and is a server that
accepts requests, currently to /kanji and /kana, which are both POST.
In the future some type of db might be implemented to track stats etc.

### Frontend
The frontend is done in js and tailwind. Im not super familar with tailwind
so the actual code might not be the greatest.

## Running the program
Currently the server and frontend only works locally and is run using
the following steps.

### Python venv
1. *Initiate venv*
    python3 -m venv venv
2. *Activate venv*
    source myenv/bin/activate
3. *Install the dependencies*
    pip3 install -r docs/requirements.txt

## Backend
You can now start the server using:
    python backend/src/server.py

## Frontend
Now the website can be used aswell, which is done by opening the html-file
on your browser of choice.
