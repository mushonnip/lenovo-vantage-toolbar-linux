# Lenovo Vantage Toolbar Linux

## The Goal
The goal for this project is to make Lenovo Vantage Toolbar like in windows app

![alt text](https://i.ibb.co/6sYvRQv/toolbar.png)

## About
This is my personal project and for personal use, if this app is useful for you, just fork it or contribute

![alt text](https://i.ibb.co/kcGcJFk/ss.png)

## Build The App
### Create and using venv

```console
python -m venv env
source env/bin/activate
```
### Install the requirement
```console
pip install -r requirements.txt
```
### Build it
this will generate `dist` folder and `lenovo_vantage_toolbar_linux` executeable file inside
```console
pyinstaller --name="lenovo_vantage_toolbar_linux" --windowed --onefile main.py
```

### Make it run
Try it with terminal
```console
sudo ./dist/lenovo_vantage_toolbar_linux
```
or make it run on start up