
from marshmallow import Schema, fields

class categorySchemaAddcategory(Schema):
      name = fields.String(required=True)
      link = fields.String(required=True)
      image = fields.String(required=True)

class categorySchemaUpdatecategory(Schema):
      name = fields.String(required=False)
      image = fields.String(required=False)
      is_active = fields.Boolean(required=False)


class categorySchemaDeletecategory(Schema):
      category_id = fields.Number(required=True,error_messages={"required": "category id is required"})
      
class categoryModel():
      def __init__(self,name,link,image):
         self.name=name
         self.link=link
         self.image=image

categorySchemaAddcategory=categorySchemaAddcategory()
categorySchemaUpdatecategory=categorySchemaUpdatecategory()
categorySchemaDeletecategory=categorySchemaDeletecategory()