import os

from flask import Flask, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy

from Flask.form import OrderForm, LoginForm
from database import app, db
from ORM import SyncORM

SyncORM.create_tables()


# SyncORM.insert_tables_client('Антон', 'г.Минск, Черняховского 4-3', '32546545774')
# SyncORM.insert_tables_client('Денис Евсеев', 'г.Минск, Рокоссовского 15-354', '6756757567')
# SyncORM.insert_tables_client('Михаил Булгаков', 'г.Гродно, Ленина 21-12', '2354879565')
# SyncORM.insert_tables_client('Петюня', 'г.Брест, Лынькова 166', '235896793456')
# SyncORM.insert_tables_client('Оля Вуду', 'г.Брест, Гагарина 3-5', '56756860342')
# SyncORM.insert_tables_client('Алина Рин', 'г.Минск, Машерова 124', '4578967947')
# SyncORM.insert_tables_client('Дмитрий Бейл', 'г.Могилев, Б. Шевченко 111-6', '789213475885')
# SyncORM.insert_tables_client('Игорь ГХК', 'г.Пинск, Черняховского 5-2', '4579625547655')
#
# SyncORM.insert_tables_order(1)
# SyncORM.insert_tables_order(2)
# SyncORM.insert_tables_order(3)
# SyncORM.insert_tables_order(4)
# SyncORM.insert_tables_order(5)
# SyncORM.insert_tables_order(6)
# SyncORM.insert_tables_order(7)
# SyncORM.insert_tables_order(8)
# SyncORM.insert_tables_order(1)
# SyncORM.insert_tables_order(2)
# SyncORM.insert_tables_order(2)
# SyncORM.insert_tables_order(3)
# SyncORM.insert_tables_order(4)
#
# SyncORM.insert_tables_recipes('4 сезона', 18, 4, 3, 6, 7, 3, 35, 'Самая вкусная пицца!!!!', '4_sezona')
# SyncORM.insert_tables_recipes('5 Сыров', 14, 5, 7, 3, 4, 1, 43, 'Самая вкусная пицца!!!!', '5_syrov')
# SyncORM.insert_tables_recipes('Ветчина и Грибы', 14, 3, 5, 6, 1, 6, 45, 'Самая вкусная пицца!!!!', 'vetchina_i_griby')
# SyncORM.insert_tables_recipes('Гавайская', 13, 8, 2, 6, 5, 3, 36, 'Самая вкусная пицца!!!!', 'gavayskaya')
# SyncORM.insert_tables_recipes('Грибная с голубым сыром', 18, 6, 3, 5, 7, 1, 51, 'Самая вкусная пицца!!!!', 'gribnaya')
# SyncORM.insert_tables_recipes('Карбонара', 15, 12, 7, 1, 4, 5, 23, 'Самая вкусная пицца!!!!', 'carbonara')
# SyncORM.insert_tables_recipes('Маргарита', 15, 2, 10, 6, 8, 9, 34, 'Самая вкусная пицца!!!!', 'margarita')
# SyncORM.insert_tables_recipes('Пепперони', 18, 4, 4, 2, 6, 6, 25, 'Самая вкусная пицца!!!!', 'Pepperony')
# SyncORM.insert_tables_recipes('Фермерская', 18, 1, 9, 9, 9, 9, 42, 'Самая вкусная пицца!!!!', 'fermerskaya')
#
# SyncORM.insert_tables_employees(1, 'Сергей Петров', "Пиццерист", 5)
# SyncORM.insert_tables_employees(2, 'Сергей Петров', "Пиццерист", 7)
# SyncORM.insert_tables_employees(3, 'Сергей Петров', "Пиццерист", 9)
# SyncORM.insert_tables_employees(4, 'Сергей Петров', "Пиццерист", 10)
# SyncORM.insert_tables_employees(5, 'Сергей Петров', "Пиццерист", 4)
# SyncORM.insert_tables_employees(6, 'Сергей Петров', "Пиццерист", 9)
# SyncORM.insert_tables_employees(7, 'Сергей Петров', "Пиццерист", 6)
# SyncORM.insert_tables_employees(8, 'Сергей Петров', "Пиццерист", 7)
# SyncORM.insert_tables_employees(9, 'Сергей Петров', "Пиццерист", 4)
# SyncORM.insert_tables_employees(10, 'Сергей Петров', "Пиццерист", 8)
# SyncORM.insert_tables_employees(11, 'Сергей Петров', "Пиццерист", 5)
# SyncORM.insert_tables_employees(12, 'Сергей Петров', "Пиццерист", 4)
# SyncORM.insert_tables_employees(13, 'Сергей Петров', "Пиццерист", 9)
# SyncORM.insert_tables_employees(13, 'Анна Васильева', "Пиццерист", 11)
#
# SyncORM.insert_tables_order_list(1, '4 сезона')
# SyncORM.insert_tables_order_list(1, '5 Сыров')
# SyncORM.insert_tables_order_list(2, 'Ветчина и Грибы')
# SyncORM.insert_tables_order_list(3, 'Гавайская')
# SyncORM.insert_tables_order_list(4, 'Грибная с голубым сыром')
# SyncORM.insert_tables_order_list(5, 'Карбонара')
# SyncORM.insert_tables_order_list(6, 'Фермерская')
# SyncORM.insert_tables_order_list(7, 'Маргарита')
# SyncORM.insert_tables_order_list(8, 'Маргарита')
# SyncORM.insert_tables_order_list(9, 'Маргарита')
# SyncORM.insert_tables_order_list(10, 'Карбонара')
# SyncORM.insert_tables_order_list(11, 'Пепперони')
# SyncORM.insert_tables_order_list(12, 'Пепперони')
# SyncORM.insert_tables_order_list(13, 'Фермерская')
# SyncORM.insert_tables_order_list(1, 'Карбонара')
# SyncORM.insert_tables_order_list(5, 'Гавайская')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pizza/<string:pizza>')
def get_pizza_interface(pizza):
    if pizza != 'favicon.ico':
        pizza = SyncORM.get_pizza(pizza)
        temp = pizza.eng_name
        path = '/media/examples/' + temp + '.png'
        return render_template('pizza.html', pizza=pizza, temp_path=path)


@app.route('/order/<string:order>')
def get_order_interface(order):
    if order != 'favicon.ico':
        temp = []
        temp, all_price = SyncORM.get_order(order)

        return render_template('basket.html', basket=temp, all_price=all_price)


@app.route('/basket')
def get_basket_interface():
    temp = []
    temp, all_price = SyncORM.basket_order()
    return render_template('basket.html', basket=temp, all_price=all_price)


@app.route('/basket/drop', methods=['GET'])
def drop_basket_order_interface():
    SyncORM.drop_basket_order()
    return render_template('index.html')


@app.route('/basket/confirm', methods=['GET', 'POST'])
def confirm_order_interface():
    form = OrderForm()
    if form.validate_on_submit():
        flash("Ваш заказ успешно принят! Ожидайте", "success")
        SyncORM.create_new_order(form.usernameOrder.data, form.addressOrder.data, form.phoneOrder.data)
        return redirect(url_for('index'))

    return render_template('confirm_order.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if SyncORM.chek_value(form.username.data, form.password.data) is True:
            flash(f"Добрый день {form.username.data}", "success")
            # Перенаправление на страницу входа или другую страницу
            temp_user = SyncORM.search_user(form.username.data)
            login_user(temp_user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', title='Войти', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/<int:client_id>')
@login_required
def get_client_interface(client_id):
    client = SyncORM.select_tables_client_order_order_list(client_id)
    return render_template('client.html', client=client)


@app.route('/clients')
@login_required
def get_clients_interface():
    clients = SyncORM.get_clients()
    return render_template('clients.html', clients=clients)


if __name__ == '__main__':
    app.run(debug=True)
