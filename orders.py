import sqlite3


def find_order(customer):
    conn = sqlite3.connect("shop.db")
    query = "SELECT * FROM orders WHERE customer = '" + customer + "'"
    return conn.execute(query).fetchall()


def add_item(item, cart=[]):
    cart.append(item)
    return cart


def shout(name):
    name.upper()
    return name
