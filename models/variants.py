from db import db


class VariantsModel(db.Model):
    __tablename__ = "variants"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer, db.ForeignKey("products.id"), unique=False, nullable=False
    )
    product = db.relationship("ProductsModel", back_populates="variants")
    name = db.Column(db.String(50), unique=False, nullable=False)
    size = db.Column(db.String(50), unique=False, nullable=False)
    color = db.Column(db.String(50), unique=False, nullable=False)
    images = db.relationship(
        "ImagesModel",
        back_populates="variant",
        secondary="variant_images",
        lazy="dynamic",
    )
    created_at = db.Column(db.TIMESTAMP(), nullable=False)
    updated_at = db.Column(db.TIMESTAMP(), nullable=False)
