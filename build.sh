#!/bin/bash

# Create an empty folder called models
mkdir models

# Run pickle_model.py script, to automatically add the pkl file to the models folder
python3 pickle_model.py

# Run the app locally
python3 app.py

# Visit the site
xdg-open http://localhost:5000
