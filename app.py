from flask import Flask, render_template

app = Flask(__name__)

# Default project placeholders (update links later)
PROJECTS = [
     {
                    
        "title": "Fikra AI - Multi-Modal Intelligence Platform",
        "description": "A professional AI chat interface built with Next.js and PostgreSQL. Fikra AI allows seamless interaction with multiple LLMs via a unified routing system. It features a robust model-switching architecture, utilizing Groq (openai/gpt-oss-120b & qwen/qwen3.8-27b) for high-speed text and vision tasks, alongside MagicHour APIs (z-image-turbo & qwen-image-2.1) for generative image creation and editing. The platform includes document generation capabilities and a frictionless onboarding flow, allowing guests to test general text features while gating premium actions like file uploads/downloads behind a secure Google Authentication gate.",
        "link": "https://fikra-ai-nine.vercel.app"
    },
    {
        "title": "LoadMaster - Premium Dispatch System",
        "description": "A web-based software solution for dispatching and logistics management. The system is presumably used to centrally plan, coordinate and monitor transports, freight loads, vehicles and drivers.",
        "link": "https://loadmaster-dispatch.netlify.app"
    },
    {
            "title": "Retail Workspace",
            "description": "Retail management workspace designed to streamline daily operations for small shops and independent retailers. It provides a centralized platform for tracking product inventory, managing point-of-sale transactions, and monitoring sales performance, helping store owners organize workflows and run their business more efficiently.",
            "link": "https://danny-minishop.netlify.app"
        },



    {
        "title": "Real-time Collaboration Platform",
        "description": "Interactive web app with live updates, authentication and responsive UI using Flask, TypeScript and PostgreSQL.",
        "link": "#"
    }
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
