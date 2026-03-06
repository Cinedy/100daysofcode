from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    date = datetime.datetime.now()
    return render_template("index.html", num=random_number, year=date.year)

@app.route("/guess/<name>")
def get_guess(name: str):
    url_age = f"https://api.agify.io?name={name}"
    url_gender = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(url_gender)
    age_response = requests.get(url_age)
    if gender_response.status_code == 200 and age_response.status_code == 200:
        gender_data = gender_response.json()
        age_data = age_response.json()
        return render_template("index.html", age=age_data["age"], gender=gender_data["gender"], name=name)
    else:
        print("error")
        return "Error"

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run()