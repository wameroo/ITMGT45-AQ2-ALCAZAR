from flask import Flask,redirect
from flask import render_template
from flask import request
from flask import session
from bson.json_util import loads, dumps
from flask import make_response
import authentication
import database as db
import logging

app = Flask(__name__)

# Set the secret key to some random bytes.
# Keep this really secret!
app.secret_key = b"s@g@d@c0ff33!"

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)



@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", page="Index")

@app.route("/cart")
def cart():
    return render_template("cart.html", page="Cart")

@app.route('/addtocart')
def addtocart():
    code = request.args.get('code', '')
    product = db.get_product(int(code))
    item=dict()
    # A click to add a product translates to a
    # quantity of 1 for now

    item["qty"] = 1
    item["name"] = product["name"]
    item["subtotal"] = product["price"]*item["qty"]

    if(session.get("cart") is None):
        session["cart"]={}

    cart = session["cart"]
    cart[code]=item
    session["cart"]=cart
    return redirect('/cart')

@app.route('/addtocartmany')
def addtocartmany():
    code = request.args.get('code', '')
    code = int(code)
    while code <= 9000:
        product = db.get_product(int(code))
        item=dict()
        # A click to add a product translates to a
        # quantity of 1 for now

        item["qty"] = 1
        item["name"] = product["name"]
        item["subtotal"] = product["price"]*item["qty"]

        if(session.get("cart") is None):
            session["cart"]={}

        cart = session["cart"]
        cart[code]=item
        session["cart"]=cart
        code += 1000
    else:
        return redirect('/cart')

@app.route('/removeitem', methods=["POST"])
def removeitem():
    cart = session["cart"]
    code = request.form.get("code")
    list.remove(cart[code])
    session["cart"]=cart
    return render_template("cart.html")


@app.route("/pc_generate_finished")
def pc_generate_finished():
    return render_template("pc_generate_finished.html", page="PC DONE")

# @app.route("/productdetails")
# def productdetails():
#     return render_template("productdetails.html", page="Product Details")
#


##hard coded routes to products
@app.route("/gpu_example")
def gpu_example():
    return render_template("gpu_example.html", page="RTX 3080")

@app.route("/cpu_example")
def cpu_example():
    return render_template("cpu_example.html", page="RYZEN 9 5900X")

@app.route("/mobo_example")
def mobo_example():
    return render_template("mobo_example.html", page="X570")

@app.route("/memory_example")
def memory_example():
    return render_template("memory_example.html", page="Ram")

@app.route("/ssd_example")
def ssd_example():
    return render_template("ssd_example.html", page="NVMe")

@app.route("/hdd_example")
def hdd_example():
    return render_template("hdd_example.html", page="HDD")

@app.route("/psu_example")
def psu_example():
    return render_template("psu_example.html", page="1000W PSU")

@app.route("/chassis_example")
def chassis_example():
    return render_template("chassis_example.html", page="NZXT H510 Elite")

@app.route("/cpucooler_example")
def cpucooler_example():
    return render_template("cpucooler_example.html", page="NZXT Z53")

@app.route("/completed_builds")
def completed_builds():
    return render_template("completed_builds.html", page="Completed Builds")

@app.route("/completed_builds_streaming")
def completed_builds_streaming():
    return render_template("completed_builds_streaming.html", page="Completed Builds for Streaming")

@app.route("/completed_builds_gaming")
def completed_builds_gaming():
    return render_template("completed_builds_gaming.html", page="Completed Builds for Gaming")

@app.route("/completed_builds_multimedia")
def completed_builds_multimedia():
    return render_template("completed_builds_multimedia.html", page="Completed Builds for Multimedia")

@app.route("/streaming_tier_high")
def streaming_tier_high():
    return render_template("streaming_tier_high.html", page="High Tier Streaming PC")

@app.route("/streaming_tier_mid")
def streaming_tier_mid():
    return render_template("streaming_tier_mid.html", page="Mid Tier Streaming PC")

@app.route("/streaming_tier_low")
def streaming_tier_low():
    return render_template("streaming_tier_low.html", page="Low Tier Streaming PC")

@app.route("/multimedia_tier_high")
def multimedia_tier_high():
    return render_template("multimedia_tier_high.html", page="High Tier Multimedia PC")

@app.route("/multimedia_tier_mid")
def multimedia_tier_mid():
    return render_template("multimedia_tier_mid.html", page="Mid Tier Multimedia PC")

@app.route("/multimedia_tier_low")
def multimedia_tier_low():
    return render_template("multimedia_tier_low.html", page="Low Tier Multimedia PC")

@app.route("/gaming_tier_high")
def gaming_tier_high():
    return render_template("gaming_tier_high.html", page="High Tier Gaming PC")

@app.route("/gaming_tier_mid")
def gaming_tier_mid():
    return render_template("gaming_tier_mid.html", page="Mid Tier Gaming PC")

@app.route("/gaming_tier_low")
def gaming_tier_low():
    return render_template("gaming_tier_low.html", page="Low Tier Gaming PC")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/auth', methods = ['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    is_successful, user = authentication.login(username, password)
    app.logger.info('%s', is_successful)
    if(is_successful):
        session["user"] = user
        return redirect('/')
    else:
        error = "invalid username or password"
        return redirect('/login')

@app.route('/user_info')
def user_info():
    return render_template("user_info.html")


@app.route("/logout")
def logout():
    session.pop("user",None)
    session.pop("cart",None)
    return redirect("/")

@app.route("/signup")
def signup():
    return render_template("sign_up.html")

@app.route("/product_page")
def product_page():
    return render_template("product_page.html")

@app.route("/product_parts")
def product_parts():
    return render_template("products_parts.html")

@app.route("/pc_generate_questionnare")
def pc_generate_questionnare():
    return render_template("pc_generate_questionnare.html")

@app.route('/nouser')
def nouser():
    return render_template("nouser.html")
