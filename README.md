# Spirit Animal Quiz 🦊✨

An interactive quiz web application that predicts your **spirit animal** based on your answers to a set of personality and preference questions.  
The app uses a **machine learning model** in a Python/FastAPI backend and a **Vue 3** frontend for a smooth, dynamic user experience.

---

## 🚀 Features
- **Step-by-step quiz**: Answer questions one at a time with a clean, responsive UI.
- **Machine learning prediction**: Backend model trained using scikit-learn to predict an animal based on your answers.
- **Dynamic results page**: Shows your predicted spirit animal along with an image and description.
- **Complementary styling**: Vibrant purple gradient theme with a complementary button color.
- **Future feedback system** *(planned)*: Users can correct predictions and submit their intended animal, helping to improve the dataset and retrain the model.

---

## 🛠️ Tech Stack
**Frontend**
- Vue 3 (Composition API)
- Vue Router
- Axios

**Backend**
- Python 3
- FastAPI
- scikit-learn
- pandas
- joblib

**Other**
- Node.js & npm
- Virtual environment for Python dependencies

---

## 📂 Project Structure
```
spirit_animal/
├── backend/
│   ├── api/            # FastAPI routes
│   ├── models/         # Trained ML model and encoder
│   ├── data/           # Dataset CSV file
│   ├── venv/           # Python virtual environment (ignored by git)
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── views/      # Quiz.vue, Results.vue, etc.
│   │   ├── components/
│   │   └── main.js
│   ├── package.json
│   └── vite.config.js
└── README.md
```

---

## ⚙️ Setup & Installation

### Backend
```bash
cd backend
python -m venv venv
# Activate venv (Windows PowerShell)
.\venv\Scripts\Activate.ps1
# Activate venv (Linux/Mac)
source venv/bin/activate

pip install -r requirements.txt

# Run FastAPI server
uvicorn api.main:app --reload
```
Backend runs on `http://127.0.0.1:8000`.

---

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend runs on `http://localhost:5173`.

---

## 🧠 How It Works
1. The user answers multiple-choice questions in the quiz.
2. The frontend sends the answers to the FastAPI `/predict` endpoint.
3. The backend encodes the answers and passes them to the trained ML model.
4. The model predicts the most likely spirit animal and returns it to the frontend.
5. The results page shows the prediction with a short description and image.

---

## 📈 Future Improvements
- **Feedback & retraining loop**: Collect user corrections and retrain the model to support new animals.
- **Image curation for new animals**: Add placeholder/fallback images for unseen predictions.
- **Better model**: Experiment with Gradient Boosting, XGBoost, or neural networks.
- **UI polish**: Animations, transitions, and mystical effects.

---

## 📜 License
MIT License — free to use and modify with attribution.

---

## ✨ Acknowledgements
- [Vue.js](https://vuejs.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [scikit-learn](https://scikit-learn.org/)
