from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SubmitField, SelectField, FloatField
from wtforms.validators import InputRequired, Email, Length, NumberRange
from .models import *

class signup(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    firstname = StringField('First name', validators=[InputRequired()])
    lastname = StringField('Last name', validators=[InputRequired()])
    email = StringField('E-mail', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    conpassword = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=8, max=80), ])
    address = StringField('Address', validators=[InputRequired()])

class accountsetting(FlaskForm):
    addmoney = FloatField('Add balence', validators=[NumberRange (min=0)])

class changeaddress(FlaskForm):
    changeCurAdd = StringField('Address', validators=[InputRequired()])

class changepass(FlaskForm):
    oldpassword = PasswordField('Old Password', validators=[InputRequired(), Length(min=8, max=80)])
    changeuserpass = PasswordField('New Password', validators=[InputRequired(), Length(min=8, max=80)])
    confirm = PasswordField('Confirm New Password', validators=[InputRequired(), Length(min=8, max=80), ])

class login1(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class loginEmployee(FlaskForm):
    employee = StringField('Employee Username', validators=[InputRequired(), Length(max=50)])
    password = PasswordField('Employee Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class menu1(FlaskForm):
    qty = IntegerField('qty', validators=[InputRequired()], default=0)

class complaint(FlaskForm):
    comp = StringField('Complaint or Compliment', validators=[InputRequired()])
    isGood = BooleanField('Is Good?')
    employee = SelectField("Choose Employee",choices=[])
    submit = SubmitField("Submit Order Complaint")

class PlaceButton(FlaskForm):
    submit = SubmitField("Place Order")

class ShopButton(FlaskForm):
    submit = SubmitField("Add to Cart")

class addToMenu(FlaskForm):
    dropchoices = []
    fooditem = get_all_food_items()
    for item in fooditem:
        dropchoices.append((item.itemID, item.itemName))
    droplist = SelectField(label="Add Food Item", choices=dropchoices)
    submit = SubmitField("Add to Menu")

class deleteFromMenu(FlaskForm):
    dropchoices = []
    fooditem = get_all_food_items()
    for item in fooditem:
        dropchoices.append((item.itemID, item.itemName))
    droplist = SelectField(label="Remove Food Item", choices=dropchoices)
    submit = SubmitField("Remove from Menu")

class dropDownFood(FlaskForm):
    dropchoices = []
    fooditem = get_all_food_items()
    for item in fooditem:
        dropchoices.append((item.itemID,item.itemName))
    droplist = SelectField(label="Food Items", choices=dropchoices)


class managerButtons(FlaskForm):
    hire = SubmitField("Hire Employee")
    fire = SubmitField("Fire Employee")
    close = SubmitField("Close Customer Account")
    promoteE = SubmitField("Promote Employee")
    demoteE = SubmitField("Demote Employee")
    promoteC = SubmitField("Grant VIP")
    demoteC = SubmitField("Drop VIP")
    warning = SubmitField("Issue Warnings")
    employeeDropList = SelectField(label="Employees", choices=[])
    customerDropList = SelectField(label="Customers", choices=[])

    
class hireEmployee(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    firstname = StringField('First name', validators=[InputRequired()])
    lastname = StringField('Last name', validators=[InputRequired()])

    emplyTypeList = []
    employeeTypes = get_employee_types()

    for type in employeeTypes:
        emplyTypeList.append((type.typeID,type.description))

    typeDropList = SelectField(label="Types of Employees", choices=emplyTypeList)

    salaryList = []
    salaries = get_salaries()

    for salary in salaries:
        salaryList.append((salary.salaryID,salary.hourBase))

    salaryDropList = SelectField(label="Initial Salary Per Hour", choices=salaryList)

    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    conpassword = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=8, max=80), ])
    submit = SubmitField("Add New Employee To Database")



