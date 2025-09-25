from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['post', 'get']) # Главная
def integer():
    messege =""
    if request.method == 'Post':
        user = request.form.get('username')
        password = request.form.get('password')
        messege = messege + user = '' = password
        return render_template('proba.html', messege = messege)
    # return render_template('proba.html' messege = messege)

if __name__ == "main":
    print("run server")
    app.run()
