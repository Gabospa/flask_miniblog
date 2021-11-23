from flask import abort, render_template

from app.models import Post
from . import public_pb


@public_pb.route('/')
def index():
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts) 


@public_pb.route("/p/<string:slug>/")
def show_post(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        abort(404)
    return render_template("public/post_view.html", post=post)