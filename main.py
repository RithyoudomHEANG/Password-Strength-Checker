from flask import Flask, render_template, request
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        password = request.form['password']
        score = 0
        length = len(password)

        upper_case = any(c in string.ascii_uppercase for c in password)
        lower_case = any(c in string.ascii_lowercase for c in password)
        special = any(c in string.punctuation for c in password)
        digits = any(c in string.digits for c in password)
        characters = [upper_case, lower_case, special, digits]

        # Check against common passwords
        found_in_common = False
        try:
            with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    if password == line.strip():
                        found_in_common = True
                        break
        except FileNotFoundError:
            found_in_common = False

        if found_in_common:
            result = {
                "message": "⚠️ Your password is in a common password list!",
                "score": 0,
                "strength": "Very Weak"
            }
        else:
            if length > 8:
                score += 1
            if length > 12:
                score += 1
            if length > 17:
                score += 1
            if length > 20:
                score += 1

            if sum(characters) > 1:
                score += 1
            if sum(characters) > 2:
                score += 1
            if sum(characters) > 3:
                score += 1

            if score < 4:
                strength = "Weak"
            elif score == 4:
                strength = "Okay"
            elif 4 < score < 6:
                strength = "Good"
            else:
                strength = "Strong"

            result = {
                "message": f"✅ Password checked successfully!",
                "score": score,
                "strength": strength
            }

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
