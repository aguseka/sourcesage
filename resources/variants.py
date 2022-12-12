from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import VariantsModel, ProductsModel
from schema import VariantSchema


blp = Blueprint("Variants", "variants", description="Operations on variants")

# query all product with variants
@blp.route("/variant/all")
class VariantList(MethodView):
    @blp.response(200, VariantSchema(many=True))
    def get(self):
        return VariantsModel.query.all()


# see a list of variants for a single variant_data
@blp.route("/product/<string:product_id>/variant")
class VariantsInProduct(MethodView):
    @blp.response(200, VariantSchema(many=True))
    def get(self, product_id):
        product = ProductsModel.query.get_or_404(product_id)

        return product.variants.all()  # lazy="dynamic" means 'variants' is a query

    @blp.arguments(VariantSchema)
    @blp.response(201, VariantSchema)
    def post(self, variant_data, product_id):
        variant = VariantsModel(**variant_data, product_id=product_id)

        if variant:
            variant.name = variant_data["name"]
            variant.size = variant_data["size"]
            variant.color = variant_data["color"]
        else:
            variant = VariantsModel(id=product_id, **variant_data)

        db.session.add(variant)
        db.session.commit()

        return variant


@blp.route("/product/<string:product_id>/variant/<string:variant_id>")
class SingleVariantUpdate(MethodView):
    @blp.arguments(VariantSchema)
    @blp.response(201, VariantSchema)
    def post(self, variant_data, product_id, variant_id):
        variant = VariantsModel.query.get(variant_id)
        if variant:
            variant.product_id = product_id
            variant.name = variant_data["name"]
            variant.size = variant_data["size"]
            variant.color = variant_data["color"]
        else:
            variant = VariantsModel(id=variant_id, **variant_data)
        try:
            db.session.add(variant)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return variant
