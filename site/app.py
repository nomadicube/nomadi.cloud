# create a flask app with two routes, one to index.html and another to pgp.html 
# ^yeah i just told the ai to do it lol
from flask import * 

app = Flask(__name__) 

@app.route('/')     
def index(): 
    return render_template('index.html') 

@app.route('/pgp')     
def pgp(): 
    return render_template('pgp.html') 

@app.route('/nomad.asc')
def pgp_asc():
    return send_from_directory('static', 'nomad.asc', as_attachment=True)

if __name__ == '__main__': 
    #app.run(debug=True, host='0.0.0.0', port=80)
    app.run()
