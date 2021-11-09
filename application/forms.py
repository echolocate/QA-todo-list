from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField("Task description", validators=[DataRequired()])
    submit = SubmitField("Add Task")

# class UpdateForm(FlaskForm):
#     id = IntegerField("Task ID", validators=[DataRequired()])
#     description = StringField("Task description", validators=[DataRequired()])
#     submit = SubmitField("Update Task")
    
    