# url-shortener
This app provides user interface and api for shortening urls.
It is currently deploed at https://short-url-test.herokuapp.com/

## Installation
```bash
git clone https://github.com/An0therM0nkey/url-shortener.git && cd url-shortener
```

## Setting up
Install requirements:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Set environmental variables:
```bash
export $(cat .env | xargs) && export $(cat .flaskenv | xargs)
```
Run app:
```bash
flask run
```
<kbd>![](/screenshots/main_page.png)</kbd>

## API
By clicking "API" link in the top right corner we can see api documentation:
<kbd>![](/screenshots/api_root.png)<kbd>
