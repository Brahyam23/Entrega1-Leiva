from django.forms import Form


class User(Form):
    nombre = Form.CharField()
    nick = Form.CharField()
    password = Form.CharField()
    email = Form.EmailField()
    creation_date = Form.DateField()
