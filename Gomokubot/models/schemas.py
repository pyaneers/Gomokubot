from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import DBBoard

class DBBoardSchema(ModelSchema):
    """
        Serealizes DBBoard using mashmallow
    """
    class Meta:
        model = DBBoard
