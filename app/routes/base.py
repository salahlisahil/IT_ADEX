from flask import Blueprint, render_template, request, redirect, url_for

from app.helpers import send_email
from app.models import Statistic, Category, Post

base_bp = Blueprint('base', '__name__')


@base_bp.route('/')
def index():
    statistics = Statistic.query.all()
    categories = Category.query.all()
    return render_template('base/index.html', statistics=statistics, categories=categories)


@base_bp.route('/secure-payments')
def secure_payments():
    return render_template('base/securePayments.html')


@base_bp.route('/market-research')
def market_research():
    return render_template('base/research.html')


@base_bp.route('/terms')
def terms():
    return render_template('base/terms.html')


@base_bp.route('/blog')
def blog():
    posts = Post.query.order_by(Post.created_at.desc()).limit(3).all()
    resent_posts = Post.query.order_by(Post.created_at.desc()).offset(3).all()
    return render_template('base/dailyUpdates.html', posts=posts, resent_posts=resent_posts)


@base_bp.route('/payment')
def payment():
    return render_template('payment/paymentcard.html')
