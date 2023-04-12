# schema is an instance of db used to convert the db files to JSON files

from apiflask.schemas import Schema
from apiflask import fields


# creating the output schema
class TaskOutputSchema(Schema):
	id = fields.Integer()
	content = fields.String()
	date_added = fields.DateTime()
	is_completed = fields.Boolean()


class TaskCreateSchema(Schema):
	content = fields.String(required=True)


class TaskUpdateSchema(Schema):
	content = fields.String(required = True)
	is_completed = fields.Boolean(required = True)

class TaskOutputSchema(Schema):
	id = fields.Integer()
	content = fields.String()
	date_added = fields.DateTime()
	is_completed = fields.Boolean()
