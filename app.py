# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Data extracted from the images
# jobs_data = {
#     "Management": {"exposure": 25, "friction": 10},
#     "Business and financial operations": {"exposure": 20, "friction": 20},
#     "Computer and mathematical": {"exposure": 35, "friction": 60},
#     "Architecture and engineering": {"exposure": 10, "friction": 30},
#     "Life, physical, and social science": {"exposure": 50, "friction": 40},
#     "Community and social service": {"exposure": 15, "friction": 35},
#     "Legal": {"exposure": 7, "friction": 15},
#     "Educational instruction and library": {"exposure": 40, "friction": 60},
#     "Arts, design, entertainment, sports, and media": {"exposure": 60, "friction": 90},
#     "Healthcare practitioners and technical": {"exposure": 30, "friction": 50},
#     "Healthcare support": {"exposure": 35, "friction": 65},
#     "Protective service": {"exposure": 12, "friction": 45},
#     "Food preparation and serving related": {"exposure": 20, "friction": 80},
#     "Building and grounds cleaning and maintenance": {"exposure": 8, "friction": 55},
#     "Personal care and service": {"exposure": 70, "friction": 75},
#     "Sales and related": {"exposure": 55, "friction": 85},
#     "Office and administrative support": {"exposure": 45, "friction": 70},
#     "Farming, fishing, and forestry": {"exposure": 10, "friction": 60},
#     "Construction and extraction": {"exposure": 15, "friction": 20},
#     "Installation, maintenance, and repair": {"exposure": 5, "friction": 25},
#     "Production": {"exposure": 22, "friction": 65},
#     "Transportation and material moving": {"exposure": 18, "friction": 75},
# }

# @app.route('/')
# def index():
#     return render_template('index.html', jobs=jobs_data.keys())

# @app.route('/job-risk', methods=['POST'])
# def job_risk():
#     selected_job = request.form.get('job')
#     data = jobs_data[selected_job]
#     return render_template('result.html', job=selected_job, exposure=data["exposure"], friction=data["friction"])

# if __name__ == '__main__':
#     app.run(debug=True)


























# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Data extracted from the images
# jobs_data = {
#     "Management": {"exposure": 25, "friction": 10},
#     "Business and financial operations": {"exposure": 20, "friction": 20},
#     "Computer and mathematical": {"exposure": 35, "friction": 60},
#     "Architecture and engineering": {"exposure": 10, "friction": 30},
#     "Life, physical, and social science": {"exposure": 50, "friction": 40},
#     "Community and social service": {"exposure": 15, "friction": 35},
#     "Legal": {"exposure": 7, "friction": 15},
#     "Educational instruction and library": {"exposure": 40, "friction": 60},
#     "Arts, design, entertainment, sports, and media": {"exposure": 60, "friction": 90},
#     "Healthcare practitioners and technical": {"exposure": 30, "friction": 50},
#     "Healthcare support": {"exposure": 35, "friction": 65},
#     "Protective service": {"exposure": 12, "friction": 45},
#     "Food preparation and serving related": {"exposure": 20, "friction": 80},
#     "Building and grounds cleaning and maintenance": {"exposure": 8, "friction": 55},
#     "Personal care and service": {"exposure": 70, "friction": 75},
#     "Sales and related": {"exposure": 55, "friction": 85},
#     "Office and administrative support": {"exposure": 45, "friction": 70},
#     "Farming, fishing, and forestry": {"exposure": 10, "friction": 60},
#     "Construction and extraction": {"exposure": 15, "friction": 20},
#     "Installation, maintenance, and repair": {"exposure": 5, "friction": 25},
#     "Production": {"exposure": 22, "friction": 65},
#     "Transportation and material moving": {"exposure": 18, "friction": 75},
# }

# @app.route('/')
# def index():
#     return render_template('index.html', jobs=jobs_data.keys())

# @app.route('/job-risk', methods=['POST'])
# def job_risk():
#     selected_job = request.form.get('job')
#     data = jobs_data[selected_job]
#     return render_template('result.html', job=selected_job, exposure=data["exposure"], friction=data["friction"])

# if __name__ == '__main__':
#     app.run(debug=True)






































from flask import Flask, render_template, request

app = Flask(__name__)

# Data extracted from the images
jobs_data = {
    "Management": {"exposure": 25, "friction": 10},
    "Business and financial operations": {"exposure": 20, "friction": 20},
    "Computer and mathematical": {"exposure": 35, "friction": 60},
    "Architecture and engineering": {"exposure": 10, "friction": 30},
    "Life, physical, and social science": {"exposure": 50, "friction": 40},
    "Community and social service": {"exposure": 15, "friction": 35},
    "Legal": {"exposure": 7, "friction": 15},
    "Educational instruction and library": {"exposure": 40, "friction": 60},
    "Arts, design, entertainment, sports, and media": {"exposure": 60, "friction": 90},
    "Healthcare practitioners and technical": {"exposure": 30, "friction": 50},
    "Healthcare support": {"exposure": 35, "friction": 65},
    "Protective service": {"exposure": 12, "friction": 45},
    "Food preparation and serving related": {"exposure": 20, "friction": 80},
    "Building and grounds cleaning and maintenance": {"exposure": 8, "friction": 55},
    "Personal care and service": {"exposure": 70, "friction": 75},
    "Sales and related": {"exposure": 55, "friction": 85},
    "Office and administrative support": {"exposure": 45, "friction": 70},
    "Farming, fishing, and forestry": {"exposure": 10, "friction": 60},
    "Construction and extraction": {"exposure": 15, "friction": 20},
    "Installation, maintenance, and repair": {"exposure": 5, "friction": 25},
    "Production": {"exposure": 22, "friction": 65},
    "Transportation and material moving": {"exposure": 18, "friction": 75},
}

@app.route('/')
def index():
    return render_template('index.html', jobs=jobs_data.keys())

@app.route('/job-risk', methods=['POST'])
def job_risk():
    selected_job = request.form.get('job')
    data = jobs_data[selected_job]
    return render_template('result.html', job=selected_job, exposure=data["exposure"], friction=data["friction"])

if __name__ == '__main__':
    app.run(debug=True)
