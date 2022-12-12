from db import db


class Product_ImagesModel(db.Model):
    __tablename__ = "product_images"
    id = db.Column(db.Integer, primary_key=True)
    products_id = db.Column(
        db.Integer, db.ForeignKey("products.id"), unique=False, nullable=False
    )
    images_id = db.Column(
        db.Integer, db.ForeignKey("images.id"), unique=False, nullable=False
    )
