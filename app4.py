from flask import Flask, request, render_template
import pickle
vector = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open("finalized_model.pkl",'rb'))
app = Flask(__name__, template_folder='C:\\Users\\vamsi\\OneDrive\\Documents\\my project\\tamplets')
@app.route('/')
def home():
    return render_template("index2.html")
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        predict = model.predict(vector.transform([news]))
        return render_template("prediction2.html", prediction_text="news headline is -> {}".format(predict))
    else:
        return render_template("prediction2.html")
if __name__ == "__main__":
    app.run(debug=True)
