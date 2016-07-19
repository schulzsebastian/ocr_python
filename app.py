#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from ocr_script import image_to_text

app = Flask(__name__, template_folder='./')


@app.route('/', methods=['GET', 'POST'])
def getplayers():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
