from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import ImagesModel, ProductsModel
from schema import PlainImageSchema, ProductImageSchema, ProductSchema

blp = Blueprint("Images", "images", description="Operations on images")


@blp.route("/images/all")
class AllImages(MethodView):
    @blp.response(200, PlainImageSchema(many=True))
    def get(self):
        return ImagesModel.query.all()


@blp.route("/product/<string:product_id>/images")
class ImagesOfProduct(MethodView):
    @blp.response(200, ProductSchema(many=True))
    def get(self, product_id):
        product = ProductsModel.query.get_or_404(product_id)

        return product.images.all()

    @blp.arguments(ProductImageSchema)
    @blp.response(201, ProductImageSchema)
    def post(self, images_data, product_id):
        if ImagesModel.query.filter(ImagesModel.product_id == product_id).first():
            abort(
                400, message="A images with that name already exists in that product."
            )

        images = ImagesModel(**images_data, product_id=product_id)

        try:
            db.session.add(images)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e),
            )

        return images
