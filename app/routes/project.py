from flask import Blueprint, render_template, request, abort, redirect, url_for, flash
from app.models import Category, Project

project_bp = Blueprint('projects', __name__)


@project_bp.route('/category/<int:category_id>')
def category(category_id):
    projects_category = Category.query.get(category_id)
    if not projects_category:
        abort(404)

    projects = Project.query.filter_by(category=projects_category).all()

    return render_template('base/category.html', category=projects_category, projects=projects)


@project_bp.route('/project/<int:project_id>')
def project(project_id):
    get_project = Project.query.get(project_id)
    if not get_project:
        abort(404)

    get_category = Category.query.get(get_project.category_id)
    if not get_category:
        abort(404)

    return render_template('base/project.html', project=get_project, category=get_category)
