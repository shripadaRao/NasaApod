import json
import typer
import requests, time
from datetime import datetime, timedelta
from PIL import Image
from time import sleep
from apis import api_url
from datetime import date
from io import BytesIO

app = typer.Typer()

#@app.command()
#def hello(name : str):
#    typer.echo(f"Hello {name}")

default_date = typer.Argument(
    datetime.now().strftime('%Y-%m-%d'),
    formats = ['%Y-%m-%d'])
#today date
today_date = date.today()

#yesterday date
yesterday_date = today_date - timedelta(days=1)
yesterday_date = str(yesterday_date)

@app.command()
def fetch(date : datetime = yesterday_date):
    print("Sending api request...")
    #requests.status_codes
    
    dt = str(date.date())
    url_for_date = f"{api_url}&date={dt}"
    print(url_for_date)
    response = requests.get(url_for_date)
    #typer.echo(response.content)

    
    dict = json.loads(response.content)
    print(dict['explanation'])
    #print(exp_response)

#getting url from that json data
    url = response.json()['url']
    print("Fetching image...")
    img_response = requests.get(url)
    image = Image.open(BytesIO(img_response.content))

    image.show()

   

if __name__ == "__main__":
    app()
