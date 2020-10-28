# url-shortener
This app provides user interface and api for shortening urls

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
![](/screenshots/main_page.png)

## API
By clicking "API" link in the top right corner we can see api documentation:
![](/screenshots/api_root.png)
