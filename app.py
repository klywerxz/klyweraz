from flask import Flask, request, redirect
from flask import render_template
import sqlite3

# инквидизация перемен
app = Flask(__name__)

 # создаем подключение к базе данныз (файл называется  "my_database.db")
connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()


# функции для работы с бд
def productDB(): # возвращать данные про товары
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall() # возвращаем данных в виде list

# controller
@app.route('/') # Главная
def index():
    shop = productDB()
    return render_template("index.html", shop = shop)

@app.route('/personal_account') # Личный кабинет
def personal_account():
    return render_template("personal_account.html")

@app.route('/basket') # Корзина
def basket():
    return render_template("basket.html")

@app.route('/services') # Услуги
def services():
    return render_template("services.html")

@app.route('/contact') #Контакты
def contact():
    return render_template("contact.html")

@app.route('/about_the_company') # О компании
def about_the_company():
    return render_template("about_the_company.html")

@app.route('/news_and_promotions') # Новости и акции
def news_and_promotions():
    return render_template("news_and_promotions.html")

@app.route('/shop') # форма обратной связи
def shop():
    return render_template("shop.html")

@app.route('/user/<username>')
def user(username):
    return render_template("hello.html", name = username)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registr.html')


if __name__ == "__main__": # точка входа новой программы
    print("Сервер запущен") # Проверка точка входа
    app.run(debug=True)