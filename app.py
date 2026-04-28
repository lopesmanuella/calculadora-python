from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""

    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            operacao = request.form.get("operacao")

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    resultado = "Erro: divisão por zero"
                else:
                    resultado = num1 / num2
            else:
                resultado = "Operação inválida"

        except Exception as e:
            resultado = f"Erro: {e}"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)