from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "llave contador"


@app.route('/')
def counter():
    if 'visit' in session:
        session['visit'] += 0
        print("no existe")
    else:
        session['visit'] = 0
        print("existe")
    return render_template("index.html")

@app.route('/2')
def contador2():
    if 'visit' in session:
        session['visit'] += 2
    return redirect('/') 

@app.route('/destroy_session', methods = ['GET', 'POST'] )
def destroy_cache():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Reset') == 'Reset':
            print("cache limpio")
            session.pop('visit', None)
        elif request.form.get('Click') == 'Click':
            session['visit'] += 1
            print("se añadio 2 visitas nuevas")
        elif request.form.get('2Click') == '2Click':
            session['visit'] += 2
            print("se añadio 2 visitas nuevas")
        else:
            pass
    elif request.method == 'GET':
        print("no post")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
