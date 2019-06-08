#!/usr/bin/python
from flask import Flask, request, url_for
from shutil import copyfile
import codecs
import os

app = Flask(__name__,static_folder=os.getcwd(),static_url_path="")

@app.route('/save', methods=['POST'])
def save():
    filename = request.form.get('filename')
    backup = request.form.get('backup')
    data = request.form.get('tiddlers')
    print filename
    print backup
    copyfile(filename, backup)
    with codecs.open(filename,'wb',encoding='utf-8') as f:
        f.write(data)
    return "done!"

if __name__ == '__main__':
    app.run()
