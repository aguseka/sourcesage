from db import db


class Variant_ImagesModel(db.Model):

    __tablename__ = "variant_images"
    id = db.Column(db.Integer, primary_key=True)
    variant_id = db.Column(db.Integer, db.ForeignKey("variants.id"))
    images_id = db.Column(db.Integer, db.ForeignKey("images.id"))
