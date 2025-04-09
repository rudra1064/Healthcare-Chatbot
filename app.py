from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Simple rule-based chatbot responses
def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hello! How can I assist you today?",
        "timing":"Hospital opens Every day from 9am to 10pm",
        "appointment": "You can book an appointment by calling +1234567890 or visiting our website.",
        "emergency": "In case of an emergency, call 911 immediately or visit the nearest hospital.",
        "services": "We offer General Checkups, Surgery, Pediatrics, and more. What do you need help with?",
        "covid symptoms": "Common symptoms include fever, cough, and difficulty breathing. Please consult a doctor if severe.",
        "diabetes": "Diabetes is a chronic disease affecting blood sugar levels. Regular checkups and a healthy diet can help manage it.",
        "blood pressure": "Normal blood pressure is around 120/80. High blood pressure can lead to heart issues.",
        "asthma": "Asthma causes breathing difficulties due to airway inflammation. Use an inhaler and avoid triggers like dust and smoke.",
    "heart attack": "Symptoms include chest pain, shortness of breath, and dizziness. Seek immediate medical help by calling emergency services.",
    "migraine": "Migraines cause severe headaches, nausea, and sensitivity to light. Rest in a dark room and stay hydrated.",
    "flu": "Flu symptoms include fever, body aches, and fatigue. Rest, drink fluids, and take antiviral medications if necessary.",
    "pneumonia": "Pneumonia is a lung infection causing cough, fever, and difficulty breathing. Antibiotics may be required for treatment.",
    "thyroid problems": "Thyroid disorders affect metabolism and energy levels. Symptoms may include fatigue, weight changes, and mood swings.",
    "anemia": "Anemia is a condition with low red blood cells, causing fatigue and weakness. Iron-rich foods and supplements can help.",
    "depression": "Symptoms include persistent sadness, loss of interest, and fatigue. Therapy and medication can help manage it.",
    "stroke": "A stroke happens due to reduced blood flow to the brain. Symptoms include weakness, slurred speech, and confusion. Seek emergency help.",
    "arthritis": "Arthritis causes joint pain and stiffness. Exercise, medications, and therapy can help manage symptoms.",
    "food poisoning": "Symptoms include nausea, vomiting, and diarrhea. Stay hydrated and rest. Seek medical help if severe.",
    "kidney stones": "Symptoms include severe lower back pain and painful urination. Drink plenty of fluids and consult a doctor.",
    "allergies": "Allergy symptoms include sneezing, itching, and skin rash. Avoid allergens and take antihistamines if needed.",
    "tuberculosis": "TB is a bacterial infection affecting the lungs, causing persistent cough and weight loss. Long-term antibiotics are needed for treatment.",
    "malaria": "Malaria is a mosquito-borne disease causing fever and chills. Seek medical help for proper treatment.",
    "dengue": "Dengue fever causes high fever, severe body aches, and rashes. Stay hydrated and consult a doctor.",
    "chickenpox": "A contagious viral infection causing itchy blisters. Rest, stay hydrated, and avoid scratching the blisters.",
     "aids": "HIV is a virus that weakens the immune system, and AIDS is its advanced stage. It spreads through unprotected sex, blood transfusion, or sharing needles. Antiretroviral therapy (ART) helps manage the disease.",
    "cancer": "Cancer is the abnormal growth of cells in the body. Treatments include chemotherapy, radiation, and surgery depending on the type.",
    "obesity": "Obesity increases the risk of heart disease, diabetes, and joint problems. Regular exercise and a healthy diet can help.",
    "parkinson's disease": "A neurodegenerative disorder that affects movement. Symptoms include tremors, stiffness, and slow movement.",
    "alzheimer's disease": "A progressive brain disorder causing memory loss and cognitive decline. There is no cure, but treatment can slow progression.",
    "hepatitis": "Hepatitis is liver inflammation caused by viruses like Hepatitis A, B, and C. Symptoms include jaundice, fatigue, and nausea.",
    "gallstones": "Gallstones are solid deposits in the gallbladder that can cause severe pain. Surgery may be needed for removal.",
    "appendicitis": "Appendicitis causes severe abdominal pain and requires immediate surgery to remove the appendix.",
    "sinusitis": "Sinusitis is an inflammation of the sinuses causing headaches, congestion, and facial pain. Steam inhalation and medication can help.",
    "eczema": "A skin condition causing itching, redness, and dryness. Moisturizing and avoiding allergens can help manage it.",
    "psoriasis": "A chronic skin condition causing red, scaly patches. Treatment includes creams, light therapy, and medications.",
    "ulcer": "Ulcers are sores in the stomach lining, causing pain and acidity. Avoid spicy foods and take prescribed medication.",
    "insomnia": "Insomnia is difficulty falling asleep or staying asleep. Reduce screen time and follow a sleep routine for better rest.",
    "bye": "Thank you for reaching out. Stay healthy!",
    "goodbye": "Thank you for reaching out. Stay healthy!"
    }
    
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    
    return "I'm sorry, I don't understand. Please contact our hospital directly."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
