import os
from dataclasses import dataclass, field

from flask import Flask, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import func, Integer
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy.orm import selectinload, joinedload, contains_eager

from config import Config

basedir = os.path.abspath(os.path.dirname(__file__))
sync_engine = "sqlite:///" + os.path.join(basedir, 'instance', 'my.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sync_engine
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)


# region Таблицы
class Order(db.Model):
    id_order = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, server_default=func.current_date())

    id_client_order = db.Column(db.Integer, db.ForeignKey('client.id_client'))

    client_order = db.relationship('Client', back_populates='order')

    client_order_list = db.relationship('OrderList', back_populates='order_order_list')

    client_order_employees = db.relationship('Employees', back_populates='order_employees')


class Client(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.Text)
    client_address = db.Column(db.Text)
    client_phone = db.Column(db.Text)

    order = db.relationship('Order', back_populates='client_order')


class OrderList(db.Model):
    id_order_list = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Text)
    price = db.Column(db.Integer)

    id_order_order_list = db.Column(db.Integer, db.ForeignKey('order.id_order'))
    order_order_list = db.relationship('Order', back_populates='client_order_list')


class Employees(db.Model):
    id_employees = db.Column(db.Integer, primary_key=True)
    employees_fullname = db.Column(db.Text)
    employees_profession = db.Column(db.Text)
    salary = db.Column(db.Integer)

    id_order_employees = db.Column(Integer, db.ForeignKey('order.id_order'))
    order_employees = db.relationship('Order', back_populates='client_order_employees')


class Basket(db.Model):
    id_basket = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Text)
    price = db.Column(db.Integer)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class SyncORM:

    @staticmethod
    def create_tables():  # создаем все таблицы наcледуемые от db
        """Функция удаления и создания всех таблиц"""
        with app.app_context():
            # db.drop_all()
            db.create_all()

    @staticmethod
    def insert_tables_client(temp_name, temp_address, temp_phone):
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with app.app_context():  # замена сессиям в связки Фласк+Алхимия
            client = Client(client_name=temp_name, client_address=temp_address, client_phone=temp_phone)
            db.session.add(client)
            db.session.commit()

    #
    @staticmethod
    def insert_tables_order(temp_id):
        """Функция добавления данных в табл заказ - temp_id - id клиента, дата заказа ставится автоматом"""
        with app.app_context():
            order = Order(id_client_order=temp_id)
            db.session.add(order)
            db.session.commit()

    @staticmethod
    def insert_tables_order_list(temp_id, temp_order):
        """Функция добавления данных в заказ - temp_id - id заказа, temp_order - заказ, temp_price - цена"""
        with app.app_context():
            query = db.select(Recipes)
            result = db.session.execute(query)
            recipes = result.scalars().all()
            for i in recipes:
                if i.name_recipe == temp_order:
                    temp_price = i.price
                    break

            order_list = OrderList(id_order_order_list=temp_id, order=temp_order, price=temp_price)
            db.session.add(order_list)
            db.session.commit()

    @staticmethod
    def insert_tables_recipes(temp_name_recipe, temp_size, temp_cheese, temp_pepperoni, temp_mushrooms, temp_onions,
                              temp_bacon, temp_price, temp_decription,
                              temp_eng_name):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with app.app_context():
            recipes = Recipes(name_recipe=temp_name_recipe, size=temp_size, cheese=temp_cheese,
                              pepperoni=temp_pepperoni, mushrooms=temp_mushrooms, onions=temp_onions,
                              bacon=temp_bacon, price=temp_price, description=temp_decription, eng_name=temp_eng_name)
            db.session.add(recipes)
            db.session.commit()

    @staticmethod
    def insert_tables_employees(temp_id_order_employees, temp_employees_fullname, temp_employees_profession,
                                temp_salary):  # функция доабвления данных в таблицу
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with app.app_context():
            employees = Employees(id_order_employees=temp_id_order_employees,
                                  employees_fullname=temp_employees_fullname,
                                  employees_profession=temp_employees_profession, salary=temp_salary)
            db.session.add(employees)
            db.session.commit()

    @staticmethod
    def get_client(client_id):
        with app.app_context():
            result = db.session.get(Client, client_id)  # для вывода ожного достаточно использовать get
            client = result
            return client

    @staticmethod
    def get_clients():
        with app.app_context():
            query = db.select(Client)  # для выбора всех выбирае всю таблицу целиком
            result = db.session.execute(query)  # экзекьютим/выполняем ее
            clients = result.scalars().all()  # отображаем выбранных клиентво (скаляр для отсеива ненужных скобок)
            return clients

    @staticmethod
    def get_pizza(name):
        with app.app_context():
            query = db.select(Recipes)
            result = db.session.execute(query)
            recipes = result.scalars().all()
            for i in recipes:
                if i.name_recipe == name:
                    return i

    @staticmethod
    def get_order(name):
        with app.app_context():
            query = db.select(Recipes)
            result = db.session.execute(query)
            recipes = result.scalars().all()
            for i in recipes:
                if i.name_recipe == name:
                    # это функция для потенциального списывания продуктов со склада
                    director.make_pizza_self(size=i.size, cheese=i.cheese, pepperoni=i.pepperoni, mushrooms=i.mushrooms,
                                             onions=i.onions, bacon=i.bacon)
                    # кладем заказ в корзину
                    basket = Basket(order=i.name_recipe, price=i.price)
                    db.session.add(basket)
                    db.session.commit()
                    basket, all_price = SyncORM.basket_order()
                    return basket, all_price

    @staticmethod
    def basket_order():
        with app.app_context():
            all_price = 0
            query = db.select(Basket)
            result = db.session.execute(query)
            basket = result.scalars().all()  # отображаем выбранных заказов
            all_price = sum([i.price for i in basket])
            return basket, all_price

    @staticmethod
    def drop_basket_order():
        with app.app_context():
            db.session.query(Basket).delete()
            db.session.commit()

    @staticmethod
    def search_client_id(name):
        with app.app_context():
            query = db.select(Client)
            result = db.session.execute(query)
            client = result.scalars().all()
            for i in client:
                if i.client_name == name:
                    return i.id_client

    @staticmethod
    def search_table_order(temp_id):
        with app.app_context():
            query = db.select(Order)
            result = db.session.execute(query)
            order = result.scalars().all()
            for i in order:
                if i.id_client_order == temp_id:
                    return i.id_order

    @staticmethod
    def create_new_order(usernameorder, addressorder, phoneorder):
        SyncORM.insert_tables_client(usernameorder, addressorder, phoneorder)
        temp_id = SyncORM.search_client_id(usernameorder)
        SyncORM.insert_tables_order(temp_id)
        temp_id_order = SyncORM.search_table_order(temp_id)
        with app.app_context():
            query = db.select(Basket)
            result = db.session.execute(query)
            basket = result.scalars().all()
            for i in basket:
                SyncORM.insert_tables_order_list(temp_id_order, i.order)
                db.session.commit()
            SyncORM.drop_basket_order()

    @staticmethod
    def chek_value(username, password):
        with app.app_context():
            query = db.select(User)
            result = db.session.execute(query)
            user = result.scalars().all()
            for i in user:
                if i.username == username:
                    return User.check_password(i, password)

    @staticmethod
    def insert_tables_user(temp_name, temp_pass):
        """Функция выбора вставки таблицы клиента. temp_name - имя клиента, temp_address - адрес, temp_phone -тел """
        with app.app_context():
            check = False
            query = db.select(User)
            result = db.session.execute(query)
            user = result.scalars().all()
            for i in user:
                if i.username == temp_name:
                    check = True
                    break
            if check is False:
                u = User(username=temp_name)
                u.set_password(temp_pass)
                db.session.add(u)
                db.session.commit()

    @staticmethod
    def search_user(username):
        with app.app_context():
            query = db.select(User)
            result = db.session.execute(query)
            user = result.scalars().all()
            for i in user:
                if i.username == username:
                    return i

    @staticmethod
    def select_tables_client_order_order_list(temp_id):
        """Функция выбора и вывода  клиента, заказа и списка заказа id -это id клиента"""
        with app.app_context():
            query = (
                db.select(Client)
                .options(joinedload(Client.order).joinedload(Order.client_order_list))
                .filter(Client.id_client == temp_id)
            )
            result = db.session.execute(query)
            res = result.unique().scalars().all()

            return res


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class OrderForm(FlaskForm):
    # validators=[DataRequired() проверяет не пустой ли поле
    usernameOrder = StringField('Имя', validators=[DataRequired()])
    addressOrder = StringField('Адрес', validators=[DataRequired()])
    phoneOrder = StringField('телефон', validators=[DataRequired()])
    put_order = SubmitField('Заказать')


@dataclass
class Products:
    size: int = field(default=15)
    cheese: int = field(default=0)
    pepperoni: int = field(default=0)
    mushrooms: int = field(default=0)
    onions: int = field(default=0)
    bacon: int = field(default=0)


class Recipes(db.Model):
    id_recipe = db.Column(db.Integer, primary_key=True)
    name_recipe = db.Column(db.String(50), unique=True)
    size = db.Column(db.Integer)
    cheese = db.Column(db.Integer)
    pepperoni = db.Column(db.Integer)
    mushrooms = db.Column(db.Integer)
    onions = db.Column(db.Integer)
    bacon = db.Column(db.Integer)
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    eng_name = db.Column(db.Text)


@dataclass
class PizzaBuilder:  # создаем класс сборки пиццы
    parts = []

    @property
    def product(self):
        self._product = Products()  # присваиваем полю класса элементы другого класса.
        product = self._product  # присваиваем поле в переменную
        return product

    def add_size(self, part):  # метод изменения размера пиццы
        self.product.size = part
        self.parts.append(f'размер {part}')

    def add_cheese(self, part):  # метод добавки сыра
        self.product.cheese = part
        self.parts.append(f'сыр {part}')

    def add_pepperoni(self, part):  # метод добавки пеперони
        self.product.pepperoni = part
        self.parts.append(f'Пеперони {part}')

    def add_mushrooms(self, part):  # метод добавки грибов
        self.product.mushrooms = part
        self.parts.append(f'Грибы {part}')

    def add_onions(self, part):  # метод добавки лука
        self.product.onions = part
        self.parts.append(f'лук {part}')

    def add_bacon(self, part):  # метод добавки бекона
        self.product.bacon = part
        self.parts.append(f'Бекон {part}')

    def list_parts(self):  # метод описания состава пиццы
        return self.parts


@dataclass
class PizzaDirector:  # создание класса директора пиццы

    _builder = None  # создание класса директора пиццы

    @property  # передаем в директора класс создания пиццы(геттер)
    def builder(self):
        return self._builder

    @builder.setter  # передаем в директора класс создания пиццы(сеттер)
    def builder(self, builder: PizzaBuilder):
        self._builder = builder

    def make_pizza_self(self, size, cheese, pepperoni, mushrooms, onions, bacon):  # метод создания пиццы
        self.builder.add_size(size)
        self.builder.add_cheese(cheese)
        self.builder.add_pepperoni(pepperoni)
        self.builder.add_mushrooms(mushrooms)
        self.builder.add_onions(onions)
        self.builder.add_bacon(bacon)
        self.builder.list_parts()


# end region

SyncORM.create_tables()

director = PizzaDirector()  # создаем объекта класса директор
builder = PizzaBuilder()  # создаем объекта класса создания пиццы
director.builder = builder  # вызываем метод билдер из класса директор


@login.user_loader  # Функция загрузки пользователя
def load_user(temp_id):
    return User.query.get(int(temp_id))


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
    app.run()
