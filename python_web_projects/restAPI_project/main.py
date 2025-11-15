import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

BIG_API_KEY = "TopSecretAPIKey"

app = Flask(__name__)
app.json.ensure_ascii = False

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)



class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def random_coffee():
    result = db.session.execute(db.select(Cafe))
    caffe_shops = result.scalars().all()
    random_cafe = random.choice(caffe_shops)
    return jsonify(id=random_cafe.id,
                   name=random_cafe.name,
                   map_url=random_cafe.map_url,
                   img_url=random_cafe.img_url,
                   location=random_cafe.location,
                   seats=random_cafe.seats,
                   has_toilet=random_cafe.has_toilet,
                   has_wifi=random_cafe.has_wifi,
                   has_sockets=random_cafe.has_sockets,
                   can_take_calls=random_cafe.can_take_calls,
                   coffee_price=random_cafe.coffee_price
                   )


@app.route("/all")
def all_coffee_shops():
    result = db.session.execute(db.select(Cafe))
    caffe_shops = result.scalars().all()
    all_shops = []
    for shop in caffe_shops:
        all_shops.append(shop.to_dict())
    return jsonify(coffe_shops = all_shops)

@app.route('/search')
def search_coffee_shops():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    caffe_shops = result.scalars().all()
    if caffe_shops:
        return jsonify(cafes=[cafe.to_dict() for cafe in caffe_shops])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    result = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id))
    caffe_shop = result.scalars().first()

    if caffe_shop:
        caffe_shop.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the coffee price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_coffee_shop(cafe_id):
    api_key = request.args.get("api-key")
    result = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id))
    caffe_shop = result.scalars().first()

    if not caffe_shop:
        return jsonify(error={"Not Found": "Sorry, the cafe shop with that id was not found in the database"})

    if api_key != BIG_API_KEY:
        return jsonify(error={"API_KEY Missing": "Sorry, that`s not allowed. Make sure you have the correct api_key"})

    db.session.delete(caffe_shop)
    db.session.commit()
    return jsonify(response={"success": "Successfully deleted the cafe from the database."})




if __name__ == '__main__':
    app.run(debug=True)
