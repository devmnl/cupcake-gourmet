import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'cupcake.db')


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL,
            image TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL,
            number TEXT NOT NULL,
            complement TEXT,
            neighborhood TEXT NOT NULL,
            payment_method TEXT NOT NULL,
            total REAL NOT NULL,
            status INTEGER NOT NULL DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')

    conn.commit()
    conn.close()


def seed_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM products')
    count = cursor.fetchone()[0]

    if count > 0:
        conn.close()
        return

    products = [
        (
            'Cupcake de Chocolate',
            'Cupcake de chocolate belga com recheio de brigadeiro e cobertura de ganache.',
            8.50,
            'Chocolate',
            'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=delicious%20chocolate%20cupcake%20with%20chocolate%20frosting%20on%20white%20plate%20top%20view&image_size=square_hd'
        ),
        (
            'Cupcake de Morango',
            'Cupcake de baunilha com recheio de morango fresco e cobertura de chantilly.',
            9.00,
            'Frutas',
            'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=delicious%20strawberry%20cupcake%20with%20cream%20frosting%20fresh%20strawberry%20on%20top&image_size=square_hd'
        ),
        (
            'Cupcake Red Velvet',
            'Cupcake Red Velvet com recheio de cream cheese e cobertura cremosa.',
            10.00,
            'Especiais',
            'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=red%20velvet%20cupcake%20with%20cream%20cheese%20frosting%20elegant%20presentation&image_size=square_hd'
        ),
        (
            'Cupcake de Baunilha',
            'Cupcake clássico de baunilha com recheio de creme e cobertura de manteiga.',
            7.50,
            'Clássicos',
            'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=vanilla%20cupcake%20with%20white%20buttercream%20frosting%20sprinkles&image_size=square_hd'
        ),
        (
            'Cupcake de Nutella',
            'Cupcake de chocolate com recheio generoso de Nutella e cobertura cremosa.',
            11.00,
            'Especiais',
            'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=nutella%20cupcake%20with%20hazelnut%20chocolate%20frosting%20topped%20with%20nuts&image_size=square_hd'
        ),
        (
            'Cupcake de Limão',
            'Cupcake de limão siciliano com recheio de curd e cobertura de glacê.',
            8.00,
            'Frutas',
            'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=lemon%20cupcake%20with%20yellow%20frosting%20lemon%20zest%20on%20top%20fresh&image_size=square_hd'
        )
    ]

    cursor.executemany(
        'INSERT INTO products (name, description, price, category, image) VALUES (?, ?, ?, ?, ?)',
        products
    )

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_tables()
    seed_products()
    print('Banco de dados criado com sucesso!')
