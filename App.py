from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Path to the directory containing PDF files
PDF_DIR = os.path.join(os.path.dirname(__file__), 'pdfs')

# Study materials for AI and Data Science
study_materials = {
    "artificial intelligence": [
        {"title": "AI Syllabus", "file": "ai_syllabus.pdf"},
        {"title": "Introduction to AI Notes", "file": "ai_notes_intro.pdf"}
    ],
    "data science": [
        {"title": "Data Science Syllabus", "file": "data_science_syllabus.pdf"},
        {"title": "Introduction to Data Science Notes", "file": "data_science_notes_intro.pdf"}
    ]
}

@app.route('/')
def home():
    return "Welcome to the Anna University Study Material Chatbot!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    response = {"message": "Sorry, I couldn't find any information on that topic."}

    for topic, materials in study_materials.items():
        if topic in user_message:
            response = {"message": f"Here are some materials on {topic}:"}
            response['materials'] = [
                {"title": material["title"], "link": f"/pdfs/{material['file']}"}
                for material in materials
            ]
            break

    return jsonify(response)

@app.route('/pdfs/<filename>')
def download_file(filename):
    return send_from_directory(PDF_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)