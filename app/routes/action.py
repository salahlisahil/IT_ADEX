from flask.views import MethodView
from flask import render_template, request, redirect, url_for, flash, Blueprint

from app.forms import CommentForm, ContactForm
from app.helpers import send_email, get_formatted_errors
from app.models import Comment

action_bp = Blueprint('action', __name__)


class ContactView(MethodView):
    methods = ['GET', 'POST']

    def __init__(self):
        self.form = ContactForm()

    def get(self):
        return render_template('base/contact.html', form=self.form)

    def post(self):
        if self.form.validate_on_submit():
            answer = send_email(
                email=self.form.email.data,
                template='contact',
                name=self.form.name.data,
                surname=self.form.surname.data,
                message=self.form.message.data
            )
            if 'message' in answer:
                flash(answer.get('message'), category='error')
                return render_template('base/contact.html', form=self.form)
            else:
                flash('Your message has been sent. Thank you!', category='success')
                return redirect(url_for('action.contact'))
        if self.form.errors:
            formatted_errors = get_formatted_errors(self.form)
            flash(formatted_errors, category='error')
            return render_template('base/contact.html', form=self.form)
        return render_template('base/contact.html', form=self.form)


action_bp.add_url_rule('/contact', view_func=ContactView.as_view('contact'))


class CommentView(MethodView):
    methods = ['GET', 'POST']

    def __init__(self):
        self.form = CommentForm()

    def get(self):
        comments = Comment.query.order_by(Comment.created_at.desc()).all()
        return render_template('base/comment.html', form=self.form, comments=comments)

    def post(self):
        if self.form.validate_on_submit():
            new_model_instance = Comment()
            self.form.populate_obj(new_model_instance)
            new_model_instance.save()

            return redirect(url_for('action.comment'))
        return render_template('base/comment.html', form=self.form)


action_bp.add_url_rule('/comment', view_func=CommentView.as_view('comment'))


@action_bp.route('/newsletter', methods=['POST'])
def newsletter():
    if request.method == 'POST':
        email = request.form.get('email')
        answer = send_email(email, template='newsletter')
        if 'message' in answer:
            flash(answer.get('message'), category='error')
        else:
            flash('You have been subscribed!', category='success')
        return redirect(url_for('base.index'))
