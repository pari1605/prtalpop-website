import sqlite3

def create_tables():
    conn = sqlite3.connect('petalpop.db')
    c = conn.cursor()

    # USERS TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT,
            wallet INTEGER DEFAULT 0
        )
    ''')

    # PRODUCTS TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            image TEXT,
            short_desc TEXT,
            description TEXT,
            specifications TEXT,
            category TEXT,
            occasion TEXT
        )
    ''')

    # ORDERS TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            address TEXT,
            pincode TEXT,
            payment TEXT,
            items TEXT,
            total INTEGER,
            user TEXT,
            wallet_used INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()


# Run this once when app starts
create_tables()