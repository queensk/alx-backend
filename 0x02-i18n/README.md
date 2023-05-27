# 0x02-i18n
This project is a web application that demonstrates internationalization (i18n) and localization (l10n) using Flask and Babel. It allows users to switch between different languages and formats based on their preferences and location.

## Features
- Supports English, French and Arabic languages
- Detects the user’s locale from the browser settings, URL parameters or user profile
- Formats dates, times and numbers according to the user’s locale
- Provides a login and logout functionality
- Stores the user’s data in a MongoDB database

## Installation
To run this project, you need to have `Python 3.7+`, `Flask 2.0+`, `Babel 2.9+` and `PyMongo 3.12+` installed on your system. You can use pip to install the required packages:
```
pip install -r requirements.txt
```
You also need to have MongoDB running on your system. You can follow the official documentation to install and start MongoDB: `https://docs.mongodb.com/manual/installation/`

## Usage
To start the web application, run the following command:
```
FLASK_APP=main.py flask run
```
Then, open your browser and go to `http://localhost:5000/` to see the homepage. You can switch between different languages using the buttons on the top right corner. You can also log in or sign up using the links on the top left corner. Once logged in, you can edit your profile and change your language preference.

## License
This project is licensed under the `MIT License`. See the LICENSE file for more details.
