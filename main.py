import requests
from flask import Flask, request
import json
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

app = Flask(__name__)

@app.route('/')
def serialize():
        r = requests.get(request.args.get('url'), headers=headers)
        with open('image.png', 'wb') as file:
                file.write(r.content)

        im = Image.open('image.png')
        im.load()
        im = im.convert('RGB')

        if (im.width or im.height) > 500:
                im.thumbnail((200,200), Image.ANTIALIAS)

        table = []

        for y in range(0, im.height):
                row = []
                for x in range(0, im.width):
                                pixel = im.getpixel((x,y))
                                data = []
                                data.append(pixel[0])
                                data.append(pixel[1])
                                data.append(pixel[2])
                                row.append(data)
                table.append(row)


        return json.dumps(table)

if __name__ == '__main__':
        app.run(host='0.0.0.0')
