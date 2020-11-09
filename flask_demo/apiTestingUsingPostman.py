from flask import Flask, request

app= Flask(__name__)


@app.route("/postman",methods=['POST'])
def math_operation():
    if (request.method=='POST'):
        op=request.form['operation']
        n1=int(request.form['num1'])
        n2 = int(request.form['num2'])
        if(op=='add'):
            r=n1+n2
        if (op == 'sub'):
            r = n1 - n2
        if (op == 'mul'):
            r = n1 * n2
        if (op == 'div'):
            r = n1 / n2

    return r


if __name__ == '__main__':
    app.run(debug=True)