from django.forms import Form


class New(Form):
    title = Form.CharField()
    description = Form.CharField()
    url = Form.URLField()


class Post(Form.Model):
    title = Form.CharField()
    description = Form.CharField()
    url = Form.URLField()
