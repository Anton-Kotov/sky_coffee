from sqlalchemy import sql, Column, DateTime, Sequence, Integer

from utils.db_api.database import db


class User(db.Model):
    __tablename__ = "users_data"
    query: sql.Select

    telegram_id = Column(db.BigInteger, primary_key=True)
    name = Column(db.String(50))
    phone = Column(db.String(15))
    basket = Column(db.String(600))
    current_price = Column(db.Float(10))
    total_spent = Column(db.Float(10))

class Reviews(db.Model):
    __tablename__ = "reviews"
    query: sql.Select

    id = db.Column(db.Integer, primary_key=True)
    telegram_id = Column(db.BigInteger)
    name = Column(db.String(50))
    date = Column(DateTime(True), server_default=db.func.now())
    reviews = Column(db.String(100))

class Item(db.Model):
    __tablename__ = "items"
    query: sql.Select

    id = Column(db.Integer, Sequence("user_id_seq"), primary_key=True)

    main_code = Column(db.String(20))
    main_name = Column(db.String(50))

    category_code = Column(db.String(20))
    category_name = Column(db.String(50))

    subcategory_code = Column(db.String(20))
    subcategory_name = Column(db.String(50))

    volume = Column(db.String(20))
    adds = Column(db.String(50))
    photo = Column(db.String(250))
    price = Column(Integer)


#     def __repr__(self):
#         return f"""
# {self.subcategory_name} - объемом {self.name}
# Цена: {self.price}₽
# """

class Additives(db.Model):
    __tablename__ = "additives"
    query: sql.Select

    id = Column(db.Integer, Sequence("user_id_seq"), primary_key=True)

    category_code = Column(db.String(20))
    category_name = Column(db.String(50))

    name = Column(db.String(50))
    photo = Column(db.String(250))
    price = Column(Integer)

#     def __repr__(self):
#         return f"""
# {self.category_name} - {self.name}
# Цена: {self.price}₽
#     """
