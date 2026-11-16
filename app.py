from flask import Flask, render_template

app = Flask(__name__)

# Default project placeholders (update links later)
PROJECTS = [
    {
        "title": "Underwater Object Detection System",
        "description": "Real-time adaptive detection framework integrating Transweather Attention Block with YOLOv12 for robust object detection in turbid marine environments.",
        "link": "#"
    },
    {
        "title": "Full-Stack Inventory Management",
        "description": "Scalable web application for product tracking, stock management and reporting built with Python, TypeScript, MySQL and modern frontend.",
        "link": "#"
    },
    {
        "title": "Real-time Collaboration Platform",
        "description": "Interactive web app with live updates, authentication and responsive UI using Flask, TypeScript and PostgreSQL.",
        "link": "#"
    },
    {
        "title": "Smart Dashboard & Analytics",
        "description": "Data visualization and analytics dashboard with dynamic charts, filters and backend APIs powered by Python and PSQL.",
        "link": "#"
    },
    {
        "title": "API-Driven Web Services",
        "description": "RESTful services and frontend clients using Python, TypeScript, MySQL/PostgreSQL with clean architecture and responsive design.",
        "link": "#"
    },
]

RESEARCH_PAPER = {
    "title": "An Adaptive Underwater Object Detection Framework Using YOLOv12 with Transweather Attention Block",
    "description": "Underwater environments present severe visual challenges—such as light refraction, color distortion, low contrast, and suspended particles—that degrade the accuracy of standard computer vision models. This research develops an adaptive real-time object detection framework that integrates a Transweather Attention Block into the YOLOv12 architecture. By dynamically filtering out environmental degradation and enhancing feature extraction, the proposed model significantly improves detection precision and robustness for submerged objects in turbid and complex marine conditions.",
    "link": "https://www.isroset.org/pdf_paper_view.php?paper_id=4161&12-ISROSET-IJSRMS-11250.pdf",
    "publisher": "International Journal of Scientific Research in Multidisciplinary Studies (IJSRMS), Vol. 12 — Paper ID: 4161"
}

@app.route("/")
def index():
    return render_template(
        "index.html",
        projects=PROJECTS,
        research=RESEARCH_PAPER
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
