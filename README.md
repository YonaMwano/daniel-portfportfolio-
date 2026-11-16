# Daniel Gift Mapepele — Portfolio Website

A professional, fully responsive portfolio website built with **Python Flask**, **Bootstrap 5**, and **Tailwind CSS** (CDN).

## Features

- Clean, modern, mobile-first design
- Working hamburger menu (Bootstrap collapse fixed)
- Profile picture placeholder
- About, Skills, Projects, Research & Contact sections
- 5 default project cards (ready for real links)
- Published research paper section (ISROSET / IJSRMS)
- Bootstrap Icons (professional icons)
- Sticky navigation with smooth scrolling

## Quick Start

```bash
# 1. Create & activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Open your browser at: **http://127.0.0.1:5000**

## Replace the Profile Picture

1. Place your photo in:
   ```
   static/img/profile.jpg
   ```
2. In `templates/index.html`, find the hero `<img>` and change the `src` to:
   ```html
   src="{{ url_for('static', filename='img/profile.jpg') }}"
   ```

## Update Project Links

Edit the `PROJECTS` list in `app.py` and replace `"#"` with the real project URL when ready.

## Tech Stack

- **Backend:** Python Flask
- **Frontend:** Bootstrap 5 + Tailwind CSS (CDN, preflight disabled to avoid conflicts)
- **Icons:** Bootstrap Icons
- **Fonts:** Inter + Poppins (Google Fonts)

## Contact

- Email: danielgift528@gmail.com
- Phone: +255 762 109 902
- GitHub: https://github.com/Danny3026
