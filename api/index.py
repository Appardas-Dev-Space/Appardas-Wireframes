"""
appardas wireframe gallery & website hub — Vercel Serverless & Local Application
Static HTML + Tailwind wireframes served with clean absolute routing.
Zero JavaScript required.
"""

import os
import glob
from flask import Flask, render_template, send_from_directory, redirect, url_for, abort

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

possible_template_dirs = [
    os.path.join(BASE_DIR, "templates"),
    os.path.join(BASE_DIR, "..", "templates"),
    "/var/task/api/templates",
    "/var/task/templates",
]
template_folder = next((d for d in possible_template_dirs if os.path.isdir(d)), os.path.join(BASE_DIR, "templates"))

possible_static_dirs = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "..", "static"),
    "/var/task/api/static",
    "/var/task/static",
]
static_folder = next((d for d in possible_static_dirs if os.path.isdir(d)), os.path.join(BASE_DIR, "static"))

app = Flask(
    __name__,
    template_folder=template_folder,
    static_folder=static_folder,
    static_url_path="/static"
)

# --------------------------------------------------------------------------
# Root / Landing Page -> Wireframe Gallery
# --------------------------------------------------------------------------
@app.route("/")
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


# --------------------------------------------------------------------------
# Public Face Wireframes
# --------------------------------------------------------------------------
@app.route("/public")
@app.route("/sme")
def public_home():
    return render_template("public/index.html")

@app.route("/services")
def services():
    return render_template("public/services.html")

@app.route("/work")
def work():
    return render_template("public/work.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/team")
def team():
    return render_template("public/team.html")

@app.route("/contact")
def contact():
    return render_template("public/contact.html")

@app.route("/privacy")
def privacy():
    return render_template("public/privacy.html")

@app.route("/staff-profile")
@app.route("/team/<slug>")
def staff_profile(slug=None):
    return render_template("public/staff-profile.html")


# --------------------------------------------------------------------------
# Internal Face Wireframes
# --------------------------------------------------------------------------
@app.route("/internal")
@app.route("/internal/dashboard")
@app.route("/dashboard")
def dashboard():
    return render_template("internal/dashboard.html")

@app.route("/internal/content")
@app.route("/content")
def content():
    return render_template("internal/content.html")

@app.route("/internal/directory")
@app.route("/directory")
def directory():
    return render_template("internal/directory.html")

@app.route("/internal/id-manager")
@app.route("/internal/ids")
@app.route("/ids")
def id_manager():
    return render_template("internal/id-manager.html")

@app.route("/internal/inquiries")
@app.route("/inquiries")
def inquiries():
    return render_template("internal/inquiries.html")

@app.route("/internal/login")
@app.route("/login")
def login():
    return render_template("internal/login.html")

@app.route("/internal/settings")
@app.route("/settings")
def settings():
    return render_template("internal/settings.html")


# --------------------------------------------------------------------------
# Backward Compatibility & Asset Fallbacks
# --------------------------------------------------------------------------
@app.route("/appardas-logo.png")
@app.route("/public/appardas-logo.png")
@app.route("/internal/appardas-logo.png")
@app.route("/wireframes/appardas-logo.png")
def serve_logo():
    return send_from_directory(app.static_folder, "appardas-logo.png")

@app.route("/00-RESEARCH-AND-PLAN.md")
def serve_spec():
    parent_dir = os.path.dirname(BASE_DIR)
    for d in [parent_dir, BASE_DIR]:
        if os.path.exists(os.path.join(d, "00-RESEARCH-AND-PLAN.md")):
            return send_from_directory(d, "00-RESEARCH-AND-PLAN.md")
    abort(404)

@app.route("/debug")
def debug():
    return {
        "status": "online",
        "cwd": os.getcwd(),
        "base_dir": BASE_DIR,
        "template_folder": app.template_folder,
        "template_folder_exists": os.path.exists(app.template_folder),
        "templates_found": [os.path.relpath(p, app.template_folder) for p in glob.glob(os.path.join(app.template_folder, "**/*"), recursive=True) if os.path.isfile(p)] if os.path.exists(app.template_folder) else []
    }

@app.route("/<page>.html")
def html_redirect(page):
    route_map = {
        "index": "/",
        "services": "/services",
        "work": "/work",
        "about": "/about",
        "team": "/team",
        "contact": "/contact",
        "privacy": "/privacy",
        "staff-profile": "/staff-profile",
        "dashboard": "/internal/dashboard",
        "login": "/internal/login",
        "directory": "/internal/directory",
        "id-manager": "/internal/id-manager",
        "inquiries": "/internal/inquiries",
        "settings": "/internal/settings",
        "content": "/internal/content",
    }
    target = route_map.get(page)
    if target:
        return redirect(target)
    abort(404)

@app.route("/public/<page>")
def public_subpath(page):
    name = page[:-5] if page.endswith(".html") else page
    if name in ["index", ""]:
        return redirect("/public")
    return redirect(f"/{name}")

@app.route("/wireframes/<path:subpath>")
def wireframes_fallback(subpath):
    if subpath in ["index.html", "", "index"]:
        return redirect("/")
    if subpath.startswith("public/"):
        page = subpath[len("public/"):].replace(".html", "")
        return redirect("/public" if page == "index" else f"/{page}")
    if subpath.startswith("internal/"):
        page = subpath[len("internal/"):].replace(".html", "")
        return redirect(f"/internal/{page}")
    return redirect("/")
