from flask import abort, Flask, jsonify, request, render_template
import datetime

# Create application instance
app = Flask(__name__)

@app.route("/")
def index():
    """Return index page"""
    
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def caclulate():
    """Return palindromes and amount of them"""

    # Ensure dates were submitted
    if not request.form.get("start_date") or not request.form.get("end_date"):
        return abort(400)
    
    # Save dates in date objects
    try:
        start_date = datetime.date.fromisoformat(request.form.get("start_date"))
        end_date = datetime.date.fromisoformat(request.form.get("end_date"))
    except:
        return abort(400)

    # Count number of palindromes and save them in list
    pal_count = 0
    pal_list = []

    while start_date <= end_date:
        if isPalindrome(start_date.strftime("%d%m%Y")):
            pal_count += 1
            pal_list.append(start_date.strftime("%d/%m/%Y"))
        start_date += datetime.timedelta(days=1)

    return jsonify({"count": pal_count, "list": pal_list})


def isPalindrome(word):
    """Verifies if word is a palindrome"""

    if word == word[::-1]:
        return True
    
    return False
