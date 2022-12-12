from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import ProductsModel
from schema import ProductSchema, PlainProductSchema

blp = Blueprint("Products", "products", description="Operations on products")

# query all products
@blp.route("/product/all")
class ProductList(MethodView):
    @blp.response(200, ProductSchema(many=True))
    def get(self):
        return ProductsModel.query.all()


@blp.route("/product/all/variants")
class ProductList(MethodView):
    @blp.response(200, ProductSchema(many=True))
    def get(self):
        return ProductsModel.query.all()


# query a single product
@blp.route("/product/<string:product_id>")
class Product(MethodView):
    @blp.response(200, ProductSchema)
    def get(self, product_id):
        product = ProductsModel.query.get_or_404(product_id)
        return product


# create or update a single product
@blp.route("/product/<string:product_id>")
class ProductUpdate(MethodView):
    @blp.arguments(ProductSchema)
    @blp.response(201, ProductSchema)
    def post(self, product_data, product_id):

        product = ProductsModel.query.get(product_id)
        if product:
            product.name = product_data["name"]
            product.description = product_data["description"]
            product.logo_id = product_data["logo_id"]
        else:
            product = ProductsModel(id=product_id, **product_data)
        try:
            db.session.add(product)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return product
