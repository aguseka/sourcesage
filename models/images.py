from db import db


class ImagesModel(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50), unique=False, nullable=False)
    product_id = db.Column(
        db.Integer, db.ForeignKey("products.id"), unique=False, nullable=False
    )
    product = db.relationship(
        "ProductsModel", back_populates="images", secondary="product_images"
    )
    variant = db.relationship(
        "VariantsModel", back_populates="images", secondary="variant_images"
    )
