# from flask import Flask, render_template,request, jsonify

# from chat import get_response
# app=Flask(__name__)

# @app.get("/")
# def index_get():
#     return render_template("base.html")

# @app.post("/predict")
# def predict():
#     text=request.get_json().get("message")
#     response=get_response(text) 
#     message={"answer":response}
#     return jsonify(message)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.route("/")
def index_get():
    return render_template("your_chat_interface.html")

@app.route("/get", methods=["POST"])
def get():
    user_message = request.form.get("msg")
    bot_response = get_response(user_message)  # Use your chatbot function here
    return jsonify(bot_response)

if __name__ == "__main__":
    app.run(debug=True)



 
