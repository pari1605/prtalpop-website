from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3
import os
import uuid
app = Flask(__name__)
app.secret_key = "petalpop_secret"

admin_email = "prathod1605@gmail.com"

def get_product(product_id):

    # try database first
    try:
        pid = int(product_id)

        conn = sqlite3.connect("petalpop.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products WHERE id=?", (pid,))
        row = cursor.fetchone()

        conn.close()

        if row:
            return {
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "image": row[3]
            }

    except:
        pass

    # fallback to dictionary
    if product_id in products:
        product = products[product_id].copy()
        product["id"] = product_id
        return product

    return None

products = {

"rose":{
"name":"Red Rose Bouquet",
"price":300,
"image":"images/red rose bouquet home page.png",
"short_desc":"Elegant red roses wrapped beautifully.",
"description":"A classic bouquet of fresh red roses that radiates love and elegance.",

"specifications":{
"Flower Type":"Red Roses",
"Number of Stems":"12 Roses",
"Bouquet Size":"Medium",
"Wrapping":"Premium paper with ribbon"
},

"related":["pinkrose","whiterose","yellowrose"],
"occasion":["birthday","anniversary","sorry","congratulations"]
},


"tulip":{
"name":"Tulip Bouquet",
"price":800,
"image":"images/tulip bouquet home page.png",
"short_desc":"Fresh and vibrant tulips.",
"description":"Tulips are known for their vibrant colors and delicate petals.",

"specifications":{
"Flower Type":"Tulips",
"Number of Stems":"10–12 Tulips",
"Bouquet Size":"Medium",
"Color":"Mixed",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["sunflower","daisy","lily"],
"occasion":["birthday","anniversary","sorry","congratulations"]
},


"sunflower":{
"name":"Sunflower Bouquet",
"price":900,
"image":"images/sunflower bouquet home page.png",
"short_desc":"Bright and cheerful sunflowers arranged beautifully.",
"description":"This vibrant bouquet features fresh sunflowers known for their bright yellow petals and uplifting charm.",

"specifications":{
"Flower Type":"Sunflowers",
"Number of Stems":"6–8 Sunflowers",
"Bouquet Size":"Medium",
"Color":"Bright Yellow",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["tulip","daisy","allinone"],
"occasion":["getwellsoon","sorry","congratulations"]
},


"orchids":{
"name":"Orchids Bouquet",
"price":900,
"image":"images/orchids bouquet home page.png",
"short_desc":"Elegant orchids arranged beautifully.",
"description":"This stunning bouquet features fresh orchids known for their delicate petals and graceful beauty.",

"specifications":{
"Flower Type":"Orchids",
"Number of Stems":"8–10 Orchid Stems",
"Bouquet Size":"Medium",
"Color":"Classic Orchids",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["purpleorchids","blueorchids","allinone"],
"occasion":["getwellsoon","sorry","anniversary"]
},


"lily":{
"name":"Lily Bouquet",
"price":1000,
"image":"images/lily bouquet home page.png",
"short_desc":"Elegant lilies arranged to create a graceful bouquet.",
"description":"Fresh lilies known for their enchanting fragrance and delicate petals.",

"specifications":{
"Flower Type":"Lilies",
"Number of Stems":"6–8 Lily Stems",
"Bouquet Size":"Medium",
"Color":"White / Pink Lilies",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["mixlily","whitelily","allinone"]
},


"daisy":{
"name":"Daisy Bouquet",
"price":700,
"image":"images/daisy bouquet.png",
"short_desc":"Fresh daisies arranged to create a cheerful bouquet.",
"description":"This delightful bouquet features fresh daisies known for their bright and charming appearance.",

"specifications":{
"Flower Type":"Daisies",
"Number of Stems":"10–12 Daisy Stems",
"Bouquet Size":"Medium",
"Color":"White petals with yellow center",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["sunflower","whitelily","allinone"],
"occasion":["getwellsoon","congratulations"]
},


"pinkrose":{
"name":"Pink Rose Bouquet",
"price":500,
"image":"images/pink rose bouquet.png",
"short_desc":"Delicate pink roses arranged beautifully.",
"description":"Soft pink roses symbolizing admiration and gratitude.",

"specifications":{
"Flower Type":"Pink Roses",
"Number of Stems":"12 Rose Stems",
"Bouquet Size":"Medium",
"Color":"Soft Pink Roses",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["rose","whiterose","yellowrose"],
"occasion":["birthday","sorry","congratulations"]
},


"yellowrose":{
"name":"Yellow Rose Bouquet",
"price":500,
"image":"images/yellow rose bouquet.png",
"short_desc":"Bright yellow roses symbolizing friendship.",
"description":"A cheerful bouquet of yellow roses that brings warmth and happiness.",

"specifications":{
"Flower Type":"Yellow Roses",
"Number of Stems":"12 Rose Stems",
"Bouquet Size":"Medium",
"Color":"Bright Yellow Roses",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["rose","whiterose","pinkrose"],
"occasion":["birthday","congratulations","sorry","getwellsoon"]
},


"purpleorchids":{
"name":"Purple Orchids Bouquet",
"price":1000,
"image":"images/purple orchids bouquet.png",
"short_desc":"Elegant purple orchids arranged beautifully.",
"description":"Purple orchids symbolize admiration, grace, and luxury.",

"specifications":{
"Flower Type":"Purple Orchids",
"Number of Stems":"8–10 Orchid Stems",
"Bouquet Size":"Medium",
"Color":"Rich Purple Orchids",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["orchids","blueorchids","allinone"],
"occasion":["anniversary","congratulations"]
},


"mixrose":{
"name":"Mix Rose Bouquet",
"price":800,
"image":"images/mix rose bouquet.png",
"short_desc":"A vibrant bouquet of mixed roses.",
"description":"A colorful arrangement of roses symbolizing love, friendship, and joy.",

"specifications":{
"Flower Type":"Mixed Roses",
"Number of Stems":"12 Rose Stems",
"Bouquet Size":"Medium",
"Color":"Mixed Colors",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["rose","pinkrose","whiterose"],
"occasion":["congratulations","sorry","anniversary","wedding"]
},


"carnations":{
"name":"Carnations Bouquet",
"price":900,
"image":"images/carnations bouquet.png",
"short_desc":"Fresh carnations arranged beautifully.",
"description":"Carnations are known for their delicate petals and long-lasting freshness.",

"specifications":{
"Flower Type":"Carnations",
"Number of Stems":"10–12 Carnation Stems",
"Bouquet Size":"Medium",
"Color":"Pink / Red / Mixed",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["rose","pinkrose","whiterose"],
"occasion":["getwellsoon","sorry","congratulations","wedding","anniversary"]
},


"mixlily":{
"name":"Mix Lily Bouquet",
"price":1100,
"image":"images/mix lily bouquet.png",
"short_desc":"Mixed lilies arranged into a vibrant bouquet.",
"description":"A beautiful combination of lilies in multiple colors.",

"specifications":{
"Flower Type":"Mixed Lilies",
"Number of Stems":"8–10 Lily Stems",
"Bouquet Size":"Medium",
"Color":"Mixed Lily Colors",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["whitelily","lily","whiterose"],
"occasion":["getwellsoon","sorry","wedding","anniversary"]
},


"whitelily":{
"name":"White Lily Bouquet",
"price":1200,
"image":"images/white lily bouquet.png",
"short_desc":"Graceful white lilies arranged beautifully.",
"description":"White lilies symbolize purity, elegance, and peace.",

"specifications":{
"Flower Type":"White Lilies",
"Number of Stems":"6–8 Lily Stems",
"Bouquet Size":"Medium",
"Color":"White",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["sunflower","lily","daisy"],
"occasion":["getwellsoon","sorry","wedding"]
},


"whiterose":{
"name":"White Rose Bouquet",
"price":700,
"image":"images/white rose bouquet.png",
"short_desc":"Elegant white roses symbolizing purity.",
"description":"White roses represent peace, elegance, and sincerity.",

"specifications":{
"Flower Type":"White Roses",
"Number of Stems":"12 Rose Stems",
"Bouquet Size":"Medium",
"Color":"White",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["pinkrose","yellowrose","rose"],
"occasion":["getwellsoon","wedding","sorry","anniversary"]
},


"allinone":{
"name":"All in One Bouquet",
"price":1500,
"image":"images/DIY Bouquet.png",
"short_desc":"A vibrant bouquet featuring multiple flower types.",
"description":"A luxurious bouquet containing roses, tulips, sunflowers, lilies, orchids and daisies.",

"specifications":{
"Flower Type":"Mixed Flowers",
"Number of Stems":"18–24 Stems",
"Bouquet Size":"Large",
"Color":"Multi Color",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["daisy","sunflower","orchids"]
},


"blueorchids":{
"name":"Blue Orchids Bouquet",
"price":1500,
"image":"images/blue orchids bouquet.png",
"short_desc":"Exotic blue orchids arranged beautifully.",
"description":"Blue orchids symbolize uniqueness and elegance.",

"specifications":{
"Flower Type":"Blue Orchids",
"Number of Stems":"8–10 Orchid Stems",
"Bouquet Size":"Medium",
"Color":"Blue",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["orchids","purpleorchids","allinone"],
"occasion":["birthday","getwellsoon","sorry"]
},


"pinkroseandpinklilybouquet":{
"name":"Pink Rose and Pink Lily Bouquet",
"price":1100,
"image":"images/pink rose and pink lily bouquet.png",
"short_desc":"This charming bouquet features a lovely combination of fresh pink roses and delicate pink lilies, creating a soft and elegant floral arrangement.",
"description":"This charming bouquet features a lovely combination of fresh pink roses and delicate pink lilies, creating a soft and elegant floral arrangement."
"Carefully arranged by skilled florists, it blends the beauty and fragrance of both flowers into a graceful gift."
"Perfect for birthdays, celebrations, or expressing appreciation and warm wishes to someone special.",

"specifications":{
"Flower Type":"Pink Roses and Pink Lilies",
"Number of Stems":"12 Rose Stems + 6 Lily Stems",
"Bouquet Size":"Large",
"Color":"Large",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["pinkrose","lily","yellowrose"],
"occasion":["wedding","getwellsoon","sorry"]
},


"whiteroseandwhitelilybouquet":{
"name":"White Rose and White Lily Bouquet",
"price":1100,
"image":"images/all white bouquet.png",
"short_desc":"A graceful bouquet of white roses and white lilies beautifully arranged to symbolize purity, elegance, and timeless beauty.",
"description":"This elegant bouquet features a stunning combination of fresh white roses and delicate white lilies."
"Carefully arranged by skilled florists, it creates a sophisticated and serene floral gift with a soft natural fragrance."
"Perfect for birthdays, celebrations, or expressing heartfelt emotions with classic floral beauty.",

"specifications":{
"Flower Type":"White Roses and White Lilies",
"Number of Stems":"12 Rose Stems + 6 Lily Stems",
"Bouquet Size":"Large",
"Color":"Pure White Floral Combination",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["whiterose","whitelily","lily"],
"occasion":["birthday","getwellsoon","sorry","anniversary"]
},


"pinkroseandorchidsbouquet":{
"name":"Pink Rose and Orchids Bouquet",
"price":1500,
"image":"images/pink rose and orchids bouquet.png",
"short_desc":"A stunning bouquet of pink roses and orchids beautifully arranged to express elegance, admiration, and heartfelt affection.",
"description":"This beautiful bouquet features a graceful combination of fresh pink roses and exotic orchids."
"Carefully arranged by skilled florists, it blends soft romantic charm with a touch of luxurious beauty."
"Perfect for birthdays, celebrations, or surprising someone special with an elegant floral gift.",

"specifications":{
"Flower Type":"Pink Roses and Orchids",
"Number of Stems":"12 Rose Stems + 6 Orchid Stems",
"Bouquet Size":"Large",
"Color":"Soft Pink with Purple / Mixed Orchid Shades",
"Wrapping":"Premium floral paper with ribbon"
},

"related":["pinkrose","purpleorchids","orchids"],
"occasion":["birthday","getwellsoon","congratulations"]
},


"vanillacake":{
"name":"Vanilla Bento Cake",
"price":500,
"image":"images/vanilla cake.jpeg",
"short_desc":"A cute vanilla bento cake perfect for celebrations.",
"description":"This delightful vanilla bento cake is soft, creamy, and perfect for birthdays or small celebrations.",

"specifications":{
"Flavor":"Vanilla",
"Serving Size":"2-3 people",
"Shape":"Round",
"Packaging":"Bento cake box"
},

"related":["chocolatecake","strawberrycake"],
"occasion":["birthday"]
},



"chocolatecake":{
"name":"Chocolate Bento Cake",
"price":500,
"image":"images/chocolate cake.jpeg",
"short_desc":"Rich chocolate cake with smooth frosting.",
"description":"A delicious chocolate bento cake made for chocolate lovers.",

"specifications":{
"Flavor":"Chocolate",
"Serving":"2-3 People",
"Shape":"Round",
"Packaging":"Bento Cake Box"
},

"related":["vanillacake","strawberrycake"],
"occasion":["birthday"]
},


"strawberrycake":{
"name":"Strawberry Bento Cake",
"price":500,
"image":"images/strawberry cake.jpeg",
"short_desc":"Fresh strawberry cake topped with strawberries.",
"description":"A sweet strawberry bento cake topped with fresh strawberries.",

"specifications":{
"Flavor":"Strawberry",
"Serving":"2-3 People",
"Shape":"Round",
"Packaging":"Bento Cake Box"
},

"related":["vanillacake","chocolatecake"],
"occasion":["birthday"]
},



"pinkcakecombo":{
"name":"Pink Rose & Strawberry Cake Combo",
"price":900,
"image":"images/cake and pink rose combo.png",
"short_desc":"Pink rose bouquet with strawberry cake.",
"description":"A perfect combo gift including pink roses and strawberry cake.",

"specifications":{
"Items":"Pink Rose Bouquet + Strawberry Cake",
"Occasion":"Birthday / Celebration",
"Packaging":"Gift Wrapped"
},

"related":["rose","pinkrose","strawberrycake"],
"occasion":["birthday"]
},



"orchidcakecombo":{
"name":"Blue Orchids & Vanilla Cake Combo",
"price":900,
"image":"images/cake and orchids combo.png",
"short_desc":"Blue orchids bouquet with vanilla cake.",
"description":"A beautiful combo including blue orchids bouquet and vanilla cake.",

"specifications":{
"Items":"Blue Orchids Bouquet + Vanilla Cake",
"Occasion":"Birthday / Surprise",
"Packaging":"Gift Wrapped"
},

"related":["blueorchids","vanillacake"],
"occasion":["birthday"]
},


"rosecakecombo":{
"name":"Red Rose & Chocolate Cake Combo",
"price":900,
"image":"images/cake & rose bouquet conbo.png",
"short_desc":"Romantic combo of red roses and chocolate cake.",
"description":"A romantic gift combo including red roses and chocolate cake.",

"specifications":{
"Items":"Red Rose Bouquet + Chocolate Cake",
"Occasion":"Anniversary / Love",
"Packaging":"Gift Wrapped"
},

"related":["rose","chocolatecake"],
"occasion":["birthday"]
}


}



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shop")
def shop():

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    # Fetch all products
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    conn.close()

    bouquets = []
    cakes = []
    combos = []

    for row in rows:
        product = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "image": row[3],
            "category": row[7] if len(row) > 7 else "bouquet"  # fallback
        }

        if product["category"] == "cake":
            cakes.append(product)
        elif product["category"] == "combo":
            combos.append(product)
        else:
            bouquets.append(product)

    return render_template(
        "shop.html",
        bouquets=bouquets,
        cakes=cakes,
        combos=combos
    )

@app.route("/recommend")
def recommend():
    return render_template("recommend.html")


@app.route("/diy")
def diy():
    return render_template("diy.html")


@app.route("/admin")
def admin():

    # 🔒 LOGIN CHECK
    if "user" not in session:
        return redirect("/login")

    if session.get("user", "").lower().strip() != admin_email.lower():
        return redirect("/")

    import sqlite3
    import json

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    # ✅ FETCH PRODUCTS
    cursor.execute("SELECT id, name, price, image FROM products")
    rows = cursor.fetchall()

    product_list = []

    for row in rows:
        product_list.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "image": row[3]
        })

    # ✅ FETCH ORDERS (SAFE)
    try:
        cursor.execute("SELECT * FROM orders")
        orders_data = cursor.fetchall()
    except:
        orders_data = []

    conn.close()

    # ✅ FORMAT ORDERS
    formatted_orders = []

    for order in orders_data:

        try:
            items = json.loads(order[6])  # products column
        except:
            items = []

        product_text = ""

        for item in items:

            # 🌸 DIY PRODUCT
            if isinstance(item, dict) and item.get("type") == "diy":

                flowers = item.get("flowers", {})

                flower_text = ", ".join(
                    [f"{k} x {v}" for k, v in flowers.items() if v > 0]
                )

                product_text += f"DIY Bouquet ({flower_text}) | "

            # 🛍 NORMAL PRODUCT
            else:
                name = item.get("name", "Product")
                qty = item.get("qty", 1)

                product_text += f"{name} (x{qty}) | "

        formatted_orders.append({
            "name": order[1],
            "phone": order[2],
            "address": order[3],
            "pincode": order[4],
            "payment": order[5],
            "products": product_text if product_text else "No items"
        })

    return render_template(
        "admin.html",
        products=product_list,
        orders=formatted_orders
    )


@app.route('/add_product', methods=['GET','POST'])
def add_product():

    if request.method == 'POST':

        name = request.form['name']
        price = request.form['price']
        short_desc = request.form['short_desc']
        description = request.form['description']
        specifications = request.form['specifications']
        category = request.form['category']
        occasion_list = request.form.getlist("occasion")
        occasion = ",".join(occasion_list)
        import json
        raw_specs = request.form['specifications']
        spec_dict = {}

        for line in raw_specs.split('\n'):
            if ':' in line:
               key, value = line.split(':',1)
               spec_dict[key.strip()] = value.strip()
        specifications = json.dumps(spec_dict)
                                    
        image = request.files['image']
        image_filename = "images/" + image.filename
        image.save(os.path.join('static', image_filename))
        conn = sqlite3.connect("petalpop.db")
        cursor = conn.cursor()

        cursor.execute(
        """
INSERT INTO products (name, price, image, short_desc, description, specifications, category, occasion)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""",
    (name, price, image_filename, short_desc, description, specifications, category, occasion)
)

        conn.commit()
        conn.close()

        return redirect('/admin')

    return render_template('add_product.html')

@app.route("/product/<product_id>")
def product(product_id):

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    # handle id or name
    if str(product_id).isdigit():
        cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    else:
        cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + product_id + '%',))

    row = cursor.fetchone()

    if not row:
        return "Product not found"

    import json

    product = {
        "id": row[0],
        "name": row[1],
        "price": row[2],
        "image": row[3],
        "short_desc": row[4] or "",
        "description": row[5] or "",
        "specifications": {}
    }

    # fix JSON specs
    if row[6]:
        try:
            product["specifications"] = json.loads(row[6])
        except:
            product["specifications"] = {}

    conn.close()

    # ✅ related products from DB (NO DICTIONARY)
    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE id != ? ORDER BY RANDOM() LIMIT 4",
        (product["id"],)
    )

    related_rows = cursor.fetchall()
    conn.close()

    related_products = []

    for r in related_rows:
        related_products.append({
            "id": r[0],
            "name": r[1],
            "price": r[2],
            "image": r[3]
        })

    return render_template(
        "product.html",
        product=product,
        related_products=related_products
    )
@app.route("/edit_price/<int:product_id>", methods=["POST"])
def edit_price(product_id):

    if "user" not in session:
        return redirect("/login")

    if session.get("user") != admin_email:
        return redirect("/")

    price = request.form.get("price")

    # 🚨 validation
    if not price:
        return "Price cannot be empty"

    try:
        new_price = int(price)
    except:
        return "Invalid price"

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET price=? WHERE id=?",
        (new_price, product_id)
    )

    conn.commit()
    conn.close()

    return redirect("/admin")
@app.route("/cart")
def cart():

    cart_items = session.get("cart", {})

    if isinstance(cart_items, list):
        cart_items = {}
        session["cart"] = cart_items

    items = []
    total = 0

    for product_id, item in cart_items.items():

        # ✅ DIY PRODUCT
        if isinstance(item, dict) and item.get("type") == "diy":

            flowers = item["flowers"]
            wrap = item["wrap"]
            price = item["price"]
            qty = item["qty"]

            # readable flower text
            flower_text = ", ".join(
                [f"{k} x {v}" for k, v in flowers.items() if v > 0]
            )

            product = {
                "id": product_id,
                "name": "DIY Bouquet (" + flower_text + ")",
                "price": price,
                "image": "images/DIY Bouquet.png",
                "qty": qty,
                "subtotal": price * qty
            }

        # ✅ NORMAL PRODUCT
        else:

            qty = item

            conn = sqlite3.connect("petalpop.db")
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id, name, price, image FROM products WHERE id=?",
                (product_id,)
            )

            row = cursor.fetchone()
            conn.close()

            if not row:
                continue

            product = {
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "image": row[3],
                "qty": qty,
                "subtotal": row[2] * qty
            }

        # ✅ VERY IMPORTANT (INSIDE LOOP)
        items.append(product)
        total += product["subtotal"]

    return render_template("cart.html", items=items, total=total)

@app.route("/occasion/<name>")
def occasion(name):

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    # 🔥 match comma-separated values
    cursor.execute("""
        SELECT * FROM products
        WHERE occasion LIKE ?
    """, ('%' + name + '%',))

    rows = cursor.fetchall()
    conn.close()

    products = []

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "image": row[3]
        })

    return render_template(
        "occasion.html",
        products=products,
        occasion=name
    )
@app.route("/add_to_cart/<product_id>")
def add_to_cart(product_id):

    qty = int(request.args.get("qty",1))

    cart = session.get("cart", {})

    if product_id in cart:
        cart[product_id] += qty
    else:
        cart[product_id] = qty

    session["cart"] = cart

    return redirect(request.referrer)

@app.route("/increase/<product_id>")
def increase(product_id):

    cart = session.get("cart", {})

    if product_id in cart:
        cart[product_id] += 1

    session["cart"] = cart

    return redirect("/cart")


@app.route("/decrease/<product_id>")
def decrease(product_id):

    cart = session.get("cart", {})

    if product_id in cart:

        cart[product_id] -= 1

        if cart[product_id] <= 0:
            del cart[product_id]

    session["cart"] = cart

    return redirect("/cart")

@app.route("/remove/<product_id>")
def remove(product_id):

    cart = session.get("cart", {})

    if product_id in cart:
        del cart[product_id]

    session["cart"] = cart

    return redirect("/cart")


import sqlite3

@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("petalpop.db")
        cursor = conn.cursor()

        cursor.execute(
        "INSERT INTO users(name,email,password) VALUES(?,?,?)",
        (name,email,password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip().lower()
        password = request.form["password"]

        conn = sqlite3.connect("petalpop.db")
        cursor = conn.cursor()

        cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email,password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            session["user"] = email

            return redirect("/profile")

    return render_template("login.html")

@app.route("/profile")
def profile():

    if "user" not in session:
        return redirect("/login")

    return render_template("profile.html", user=session["user"])


@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/orders")
def orders():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, phone, address, payment, items, wallet_used, total
    FROM orders
    WHERE user=?
    ORDER BY id DESC
    """, (session["user"],))
       
    rows = cursor.fetchall()
    conn.close()

    orders = []

    for row in rows:
        orders.append({
    "name": row[0],
    "phone": row[1],
    "address": row[2],
    "payment": row[3],
    "items": json.loads(row[4]),
    "wallet_used": row[5],
    "total": row[6]
})

        cashback = session.get("cashback", 0)
        session.pop("cashback", None)

    return render_template("orders.html", orders=orders)



@app.route("/checkout")
def checkout():

    cart_items = session.get("cart", {})

    items = []
    total = 0

    for product_id, item in cart_items.items():

        # ✅ DIY PRODUCT
        if isinstance(item, dict) and item.get("type") == "diy":

            flowers = item["flowers"]
            wrap = item["wrap"]
            price = item["price"]
            qty = item["qty"]

            flower_text = ", ".join([
                f"{k} x {v}" for k, v in flowers.items() if v > 0
            ])

            product = {
                "id": product_id,
                "name": f"DIY Bouquet ({flower_text})",
                "price": price,
                "qty": qty,
                "subtotal": price * qty
            }

        # ✅ NORMAL PRODUCT
        else:

            qty = item

            conn = sqlite3.connect("petalpop.db")
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id, name, price FROM products WHERE id=?",
                (product_id,)
            )

            row = cursor.fetchone()
            conn.close()

            if not row:
                continue

            product = {
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "qty": qty,
                "subtotal": row[2] * qty
            }

        items.append(product)
        total += product["subtotal"]

    return render_template("checkout.html", items=items, total=total)



@app.route("/confirm_order", methods=["POST"])
def confirm_order():

    import json

    cart = session.get("cart", {})

    if not cart:
        return redirect("/cart")

    name = request.form["name"]
    phone = request.form["phone"]
    address = request.form["address"]
    pincode = request.form["pincode"]
    payment = request.form["payment"]

    serviceable = ["400001","400002","400003","400004","400005","400006","400007","400008","400009","400010","400011"]

    if pincode not in serviceable:
        return "Sorry, delivery not available in your area."

    order_items = []
    total = 0

    # 🔁 LOOP THROUGH CART
    for product_id, item in cart.items():

        # ✅ DIY PRODUCT
        if isinstance(item, dict) and item.get("type") == "diy":

            subtotal = item["price"] * item["qty"]
            total += subtotal

            order_items.append({
                "type": "DIY Bouquet",
                "flowers": item["flowers"],
                "wrap": item["wrap"],
                "qty": item["qty"],
                "price": item["price"],
                "image": "images/DIY Bouquet.png"
            })

        # ✅ NORMAL PRODUCT
        elif isinstance(item, int):

            qty = item

            conn = sqlite3.connect("petalpop.db")
            cursor = conn.cursor()

            cursor.execute(
                "SELECT name, price, image FROM products WHERE id=?",
                (product_id,)
            )

            row = cursor.fetchone()
            conn.close()

            if row:
                subtotal = row[1] * qty
                total += subtotal

                order_items.append({
                    "type": "Product",
                    "name": row[0],
                    "qty": qty,
                    "price": row[1],
                    "image": row[2]
                })

    # 🔍 GET WALLET BALANCE
    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT wallet FROM users WHERE email=?", (session["user"],))
    wallet_balance = cursor.fetchone()[0]

    conn.close()

    # 💡 CALCULATE WALLET USAGE
    wallet_used = min(wallet_balance, total)
    remaining = total - wallet_used

    # 💾 STORE FOR PAYMENT PAGE
    session["wallet_used"] = wallet_used
    session["remaining"] = remaining
    session["total"] = total

    # 💸 DEDUCT WALLET
    if wallet_used > 0:
        conn = sqlite3.connect("petalpop.db")
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET wallet = wallet - ? WHERE email=?",
            (wallet_used, session["user"])
        )

        conn.commit()
        conn.close()

    # 👉 CONVERT ITEMS TO STRING
    items_str = json.dumps(order_items)

    # ✅ SAVE ORDER
    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute("""
INSERT INTO orders (user, name, phone, address, pincode, payment, items, wallet_used, total)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    session["user"],
    name,
    phone,
    address,
    pincode,
    payment,
    items_str,
    wallet_used,
    total
))

    conn.commit()
    conn.close()

    # 🛒 CLEAR CART
    session["cart"] = {}

    # 🎁 CASHBACK (10%)
    cashback = int(total * 0.1)

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET wallet = wallet + ? WHERE email=?",
        (cashback, session["user"])
    )

    conn.commit()
    conn.close()

    session ["callback"] = cashback

    # 🚀 REDIRECT
    if payment == "online":
        return redirect("/payment")
    else:
        return redirect("/orders")

@app.route("/recommend_result", methods=["POST"])
def recommend_result():

    occasion = request.form["occasion"]
    budget = int(request.form["budget"])

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    conn.close()

    scored_products = []

    for row in rows:

        product = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "image": row[3],
            "occasion": row[8] if len(row) > 8 else "",
            "category": row[7] if len(row) > 7 else "bouquet"
        }

        # ✅ STEP 1: STRICT FILTER
        occasions = product["occasion"].split(",") if product["occasion"] else []

        if occasion not in occasions:
            continue   # ❌ skip completely

        # ✅ STEP 2: SCORING (only for matching ones)
        score = 0

        # budget logic
        if product["price"] <= budget:
            score += 30
        else:
            score -= 10

        # bonus logic
        if occasion == "birthday" and product["category"] == "cake":
            score += 20

        if occasion == "anniversary" and product["category"] == "combo":
            score += 15

        if occasion == "sorry" and product["category"] == "bouquet":
            score += 10

        scored_products.append((score, product))

    # sort
    scored_products.sort(reverse=True, key=lambda x: x[0])

    recommended = [p[1] for p in scored_products[:8]]

    return render_template(
        "recommend_result.html",
        recommended=recommended
    )
import uuid
import json

import uuid

@app.route("/add_diy_to_cart", methods=["POST"])
def add_diy_to_cart():

    data = request.json

    flowers = data.get("flowers", {})
    wrap = data.get("wrap", "")

    # ✅ calculate flower price properly
    flower_prices = {
        "rose": 20,
        "tulip": 30,
        "sunflower": 25,
        "orchids": 40,
        "lily": 35,
        "daisy": 15,
        "lavender": 20,
        "jasmine": 15,
        "carnation": 18,
        "pinkrose": 22,
        "yellowrose": 22
    }

    flower_total = 0
    for f, qty in flowers.items():
        flower_total += flower_prices.get(f, 0) * qty

    total_price = flower_total + 200 + 50   # wrap + delivery

    cart = session.get("cart", {})

    # ✅ ALWAYS NEW UNIQUE ITEM
    product_id = "diy_" + str(uuid.uuid4())

    cart[product_id] = {
        "type": "diy",
        "flowers": flowers,
        "wrap": wrap,
        "price": total_price,
        "qty": 1
    }

    session["cart"] = cart

    return jsonify({"status": "success"})

@app.route("/clear_cart")
def clear_cart():
    session["cart"] = {}
    return "Cart cleared ✅"

@app.route("/search")
def search():

    query = request.args.get("q","").lower()

    results = []

    for key, product in products.items():

        if query in product["name"].lower():

            item = product.copy()
            item["id"] = key

            results.append(item)

    return render_template(
        "search_result.html",
        results=results,
        query=query
    )

@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):

    if "user" not in session:
        return redirect("/login")

    if session.get("user") != admin_email:
        return redirect("/")

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))

    conn.commit()
    conn.close()

    return redirect("/admin")


@app.route("/buy_now/<int:product_id>")
def buy_now(product_id):

    qty = int(request.args.get("qty", 1))

    # 👉 Put item into session cart
    session["cart"] = {str(product_id): qty}

    return redirect("/checkout")
@app.route("/same_day")
def same_day():
    return render_template("same_day.html")

import requests

@app.route("/set_location", methods=["POST"])
def set_location():

    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")

    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"

    headers = {
        "User-Agent": "PetalPopApp"
    }

    response = requests.get(url, headers=headers)
    location_data = response.json()

    address = location_data.get("address", {})

    # 🧠 Extract area + city separately
    area = (
        address.get("suburb") or
        address.get("neighbourhood") or
        address.get("city_district") or
        ""
    )

    city = (
        address.get("city") or
        address.get("town") or
        address.get("village") or
        "Mumbai"
    )

    # ✨ Combine nicely
    if area and city:
        final_location = f"{area}, {city}"
    else:
        final_location = city

    session["city"] = final_location

    return jsonify({"city": final_location})


import qrcode

import uuid
import qrcode

@app.route("/payment")
def payment():

    # ✅ generate random order id
    order_id = str(uuid.uuid4())[:8]

    # ✅ your real UPI (CHANGE THIS)
    upi_id = "prathod1605@okicici"

    # ✅ amount (temporary or from session)
    amount = session.get("remaining", session.get("total"))

    # ✅ UPI link
    upi_link = f"upi://pay?pa={upi_id}&pn=PetalPop&am={amount}&cu=INR&tn=Order-{order_id}"

    # ✅ generate QR
    img = qrcode.make(upi_link)
    img.save("static/qr.png")

    # ✅ IMPORTANT (YOU MISSED THIS)
    return render_template(
    "payment.html",
    total=session.get("total"),
    wallet_used=session.get("wallet_used"),
    remaining=amount,
    amount=amount,
    order_id=order_id
)



@app.route("/payment_success")
def payment_success():

    order = session.get("pending_order")

    if not order:
        return redirect("/")

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO orders (user, name, phone, address, pincode, payment, items)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        session["user"],
        order["name"],
        order["phone"],
        order["address"],
        order["pincode"],
        "online",
        json.dumps(order["items"])
    ))

    conn.commit()
    conn.close()

    session.pop("pending_order", None)

    return redirect("/orders")



@app.route("/set_manual_location", methods=["POST"])
def set_manual_location():

    city = request.json.get("city")

    session["city"] = city

    return jsonify({"city": city})



@app.route("/wallet")
def wallet():

    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT wallet FROM users WHERE email=?", (session["user"],))
    balance = cursor.fetchone()[0]

    conn.close()

    return render_template("wallet.html", balance=balance)

@app.route("/add_money", methods=["GET", "POST"])
def add_money():

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        amount = int(request.form["amount"])

        # store amount temporarily
        session["add_money_amount"] = amount

        return redirect("/add_money_payment")

    return render_template("add_money.html")

@app.route("/add_money_payment")
def add_money_payment():

    amount = session.get("add_money_amount")

    if not amount:
        return redirect("/wallet")

    order_id = str(uuid.uuid4())[:8]

    upi_id = "prathod1605@okicici"

    upi_link = f"upi://pay?pa={upi_id}&pn=PetalPop Wallet&am={amount}&cu=INR&tn=Wallet-{order_id}"

    img = qrcode.make(upi_link)
    img.save("static/qr_wallet.png")

    return render_template(
        "add_money_payment.html",
        amount=amount,
        order_id=order_id
    )

@app.route("/add_money_success")
def add_money_success():

    amount = session.get("add_money_amount")

    if not amount:
        return redirect("/wallet")

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET wallet = wallet + ? WHERE email=?",
        (amount, session["user"])
    )

    conn.commit()
    conn.close()

    # clear session
    session.pop("add_money_amount", None)

    return redirect("/wallet")

def migrate_products():
    import json
    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    for key, p in products.items():

        cursor.execute("SELECT id FROM products WHERE name=?", (p["name"],))
        exists = cursor.fetchone()

        specs_json = json.dumps(p.get("specifications", {}))

        if exists:
            cursor.execute("""
                UPDATE products
                SET short_desc=?, description=?, specifications=?
                WHERE name=?
            """, (
                p.get("short_desc", ""),
                p.get("description", ""),
                specs_json,
                p["name"]
            ))

    conn.commit()
    conn.close()


@app.route("/migrate_occasions")
def migrate_occasions():

    conn = sqlite3.connect("petalpop.db")
    cursor = conn.cursor()

    for key, p in products.items():

        occasion_list = p.get("occasion", [])

        if occasion_list:
            occasion_text = ",".join(occasion_list)

            cursor.execute(
                "UPDATE products SET occasion=? WHERE name=?",
                (occasion_text, p["name"])
            )

    conn.commit()
    conn.close()

    return "Occasion migration done ✅"




if __name__ == "__main__":
    app.run(debug=True)