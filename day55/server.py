import random
from flask import Flask
app = Flask(__name__)

random_number = random.randint(0,9)
print(random_number)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:guess>")
def check(guess: int):
    
    if guess < random_number:
        return "too low, try again!"
    elif guess > random_number:
        return "too high, try again"
    else:
        return f"Your guess, {guess}, is correct!"


if __name__ == "__main__":
    app.run(port=5001)