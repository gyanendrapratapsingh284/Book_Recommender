from flask import Flask,render_template,request
import pickle
# import pandas
# import requests
# import numpy as np

# bk = pickle.load(open("recommender_algo.pkl","rb"))
df1 = pickle.load(open("df1.pkl","rb"))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/recommend')
def recommend_ui():
    return render_template("gen.html")


@app.route('/recommend_books',methods = ['POST'])
def recommened():
    user_input = request.form.get('Genre')
    dff = df1.groupby(['Genre','Height']).sum()
    data = dff.Title[user_input].to_numpy()
    print(data)
    return render_template('gen.html',d = data,user = user_input)
    
if __name__ == '__main__':
    app.run(debug=True)
