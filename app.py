# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 16:09:31 2023

@author: samym
"""


from flask import Flask, request, render_template,url_for
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("FormationR.html")

# @app.route('/', methods=['POST'])
# def text_box():
#     text = request.form['text']
#     processed_text = text.upper()
#     return render_template("bienvenue.html" , message = processed_text)


@app.route('/excel')
def Projets():
    return render_template("Calculator.html")



if __name__ == "__main__":
    app.run()




    