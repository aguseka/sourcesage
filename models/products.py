from db import db


class ProductsModel(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    images = db.relationship(
        "ImagesModel",
        back_populates="product",
        secondary="product_images",
        lazy="dynamic",
    )
    logo_id = db.Column(db.String(50), unique=False, nullable=False)
    created_at = db.Column(db.TIMESTAMP(), nullable=False)
    updated_at = db.Column(db.TIMESTAMP(), nullable=False)
    variants = db.relationship(
        "VariantsModel", back_populates="product", lazy="dynamic"
    )
