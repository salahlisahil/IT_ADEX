from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import Statistic, db, Category, Project, Post, Comment

admin = Admin(name='ADEX', template_mode='bootstrap4')

admin.add_view(ModelView(Statistic, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))


class ProjectModelView(ModelView):
    form_ajax_refs = {
        'category': {
            'fields': ['id', 'title'],
            'page_size': 10
        }
    }


admin.add_view(ProjectModelView(Project, db.session))
