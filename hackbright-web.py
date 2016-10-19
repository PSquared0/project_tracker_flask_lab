from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    # github = request.args.get('github', 'jhacks')
    # first, last, github = hackbright.get_student_by_github(github)
    # first, last, github = hackbright.get_student_by_github(github)
    # html =  render_template('student_info.html',
    #     first=first,
    #     last=last,
    #     github=github)

    # return html

    # we are editing code below to show student grades and proejct title.

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    # student_github, project_title, grade = hackbright.get_grades_by_github(github)
    rows = hackbright.get_grades_by_github(github)
    print rows
    html =  render_template('student_info.html',
        first=first,
        last=last,
        github=github,
        rows=rows)

    return html



@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student"""
    student_first = request.form.get('first')
    student_last = request.form.get('last')
    github = request.form.get('github')
    hackbright.make_new_student(student_first, student_last, github)
    student_first, student_last, github = hackbright.get_student_by_github(github)
    return render_template('student_add.html', 
                            first=student_first, 
                            last=student_last, 
                            github=github)


@app.route('/student-form')
def student_form():
    """Displays Student information"""
    return render_template('student_form.html')


@app.route('/project')
def project():
    """Displays Student information"""
    github = request.args.get('github', 'jhacks')
    # student_github, project_title, grade = hackbright.get_grades_by_github(github)
    rows = hackbright.get_project_by_title(title)
    print rows
    html =  render_template('project.html',
        rows=rows)

    return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
