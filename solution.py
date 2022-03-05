from flask import render_template, Flask

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/training/<prof>')
def training(prof):
    prof = prof.split()
    return render_template('simulator.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
                   'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
                   'киберинженер', 'штурман', 'пилот дронов']
    return render_template('profs.html', list=list, prof=professions)


if __name__ == '__main__':
    app.run(port=88, host='127.0.0.1')
