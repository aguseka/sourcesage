from marshmallow import Schema, fields


class PlainProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    logo_id = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class PlainVariantSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    size = fields.Str(required=True)
    color = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class PlainImageSchema(Schema):
    id = fields.Int(dump_only=True)
    url = fields.Str()


class ProductImageSchema(PlainImageSchema):
    product_id = fields.Int(dump_only=True)
    product = fields.Nested(PlainProductSchema(), dump_only=True)


class VariantImageSchema(PlainImageSchema):
    variant = fields.List(fields.Nested(PlainVariantSchema()), dump_only=True)
    variant_id = fields.Int(dump_only=True)


class ProductSchema(PlainProductSchema):
    variants = fields.List(fields.Nested(PlainVariantSchema()), dump_only=True)
    images = fields.List(fields.Nested(PlainImageSchema()), dump_only=True)


class VariantSchema(PlainVariantSchema):
    product = fields.Nested(PlainProductSchema(), dump_only=True)
    images = fields.List(fields.Nested(PlainImageSchema()), dump_only=True)
