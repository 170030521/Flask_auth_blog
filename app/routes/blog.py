from flask import render_template,redirect,url_for,request
from app import app
from app.models import db,Blog
# from app.routes.auth import view_get,view_post

@app.route("/view_all_blogs",methods=["GET","POST"])
def view_all_blogs():
    blogs = db.session.query(Blog).all()
    return render_template("post_list.html", blogs=blogs)
    # return db.session.query(Blog).all()


@app.route("/delete_blog/<int:blog_id>", methods=["GET", "POST"])
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if blog:
        db.session.delete(blog)
        db.session.commit()
    return redirect(url_for('view_all_blogs'))

@app.route("/update_blog/<int:blog_id>", methods=["GET", "POST"])
def update_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if request.method == "POST":
        blog.title = request.form['title']
        blog.content = request.form['content']
        db.session.commit()
        return redirect(url_for('view_all_blogs'))
    
    return render_template("post_detail.html", blog=blog)  
  
# @app.route("/any_one_blog/<blog_id>")
# def any_one_blog(blog_id):
def filter_blogs(title_filter, name_filter):
    # Base query to fetch blogs
    query = db.session.query(Blog)
    
    # Apply filtering by title if a title filter is provided
    if title_filter:
        query = query.filter(Blog.title.ilike(f"%{title_filter}%"))
    
    # Apply filtering by author if an author filter is provided
    if name_filter:
        query = query.filter(Blog.name.ilike(f"%{name_filter}%"))
    
    # Execute the query and return the results
    return query.all()

@app.route("/filtered_blogs", methods=["GET"])
def filtered_blogs():
    # Get filter parameters from the GET request
    title_filter = request.args.get('title_filter', '')
    name_filter = request.args.get('name_filter', '')
    
    # Retrieve filtered blogs
    blogs = filter_blogs(title_filter, name_filter)
    
    # Render the template with filtered blogs
    return render_template("post_list.html", blogs=blogs, title_filter=title_filter, name_filter=name_filter)

@app.route("/create_new",methods=["GET"])
def Create_new():
    return redirect(url_for("view_get"))



