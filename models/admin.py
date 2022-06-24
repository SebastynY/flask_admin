from flask_admin.contrib.sqla import ModelView

from flask_admin import expose


class UserView(ModelView):
    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
        return self.render('create_user.html')
