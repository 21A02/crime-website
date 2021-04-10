# Crime Data Analysis Website
### Necessary packages to install:
1. Flask 
- pip install Flask
2. Google Spreadsheets
- pip install gspread oauth2client 
### Steps to run code:
1. Download repository.
2. Open app.py in VS code.
3. Use ctrl+shift+P to select python interpreter.
4. Run app.py
5. When server is initialized, copy link and paste in your web browser


### Points to remember for developers:
- All .html files are to be kept in **templates** folder
- All associated static files like .css, .js and images are to be kept in **static** folder.
- Paths are to be mentioned like this:
```html
<link rel="stylesheet" href="{{url_for('static',filename='index.css')}}"> 
```
