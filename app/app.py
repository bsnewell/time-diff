from flask import Flask, request, render_template
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

def calculate_time_difference(target_date_str):
    target_date = datetime.strptime(target_date_str, '%Y-%m-%d %H:%M:%S')
    now = datetime.now()
    delta = relativedelta(target_date, now)
    total_seconds = (target_date - now).total_seconds()
    total_hours = total_seconds // 3600
    total_days = total_seconds // (3600 * 24)
    total_weeks = total_days // 7
    total_months = delta.years * 12 + delta.months

    return {
        "years": delta.years,
        "months": total_months,
        "weeks": total_weeks,
        "days": total_days,
        "hours": total_hours,
        "seconds": total_seconds
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target_date_str = request.form['target_date']
        result = calculate_time_difference(target_date_str)
        return render_template('index.html', result=result, target_date=target_date_str)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)