from . import portfolio
from flask import jsonify, make_response, send_file, Response, request, stream_with_context
import json
from flask import render_template, url_for, redirect
import os
import io

static_folder_pro = "../static/projects/projects.json"


@portfolio.route('/')
def home():

    return render_template("home.html", title='home', username="carlos")


@portfolio.route('/projects')
def projects():
    data = get_static_json(static_folder_pro)['projects']
    data.sort(key=order_projects_by_weight, reverse=True)

    tag = request.args.get('tags')
    if tag is not None:
        data = [project for project in data if tag.lower() in [project_tag.lower() for project_tag in project['tags']]]

    return render_template('projects.html', projects=data, tag=tag)


def get_static_json(path):
    return json.load(open(get_static_file(path)))


def order_projects_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0


def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)


@portfolio.route('/projects/<title>')
def project(title):
    projects = get_static_json(static_folder_pro)['projects']

    in_project = [p for p in projects if p['link'] == title]

    if in_project is not None:
        selected = in_project
        #selected['description'] = io.open(get_static_file('static/projects/%s/%s.html' % (selected, selected)),
         #                                 encoding='utf-8').read()
        #print(selected)
    return render_template('project.html', project=selected)