import logging

from flask import abort, render_template, current_app
from werkzeug.exceptions import NotFound

from app.models import Post
from . import public_pb


logger = logging.getLogger(__name__)

@public_pb.route('/')
def index():
    current_app.logger.info('Mostrando los posts del blog')
    logger.info('Mostrando los post del blog con nuevo logger')
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts) 


@public_pb.route("/p/<string:slug>/")
def show_post(slug):
    logger.info('Mostrando un post')
    logger.debug(f'Slug: {slug}')
    post = Post.get_by_slug(slug)
    if post is None:
        logger.info(f'El post {slug} no existe')
        abort(404)
    return render_template("public/post_view.html", post=post)


@public_pb.route("/error")
def show_error():
    res = 1/0
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)