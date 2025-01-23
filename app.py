from flask import Flask, request, jsonify, render_template
import yagmail

# Configuração do Flask
app = Flask(__name__)

# Configurações do Yagmail
EMAIL_ADDRESS = "gustavocandido044@gmail.com"  # Substitua pelo seu email
EMAIL_PASSWORD = "sua_senha"  # Senha do aplicativo (não a senha normal, veja instruções abaixo)

# Rota principal para exibir o formulário
@app.route("/")
def index():
    return render_template("index.html")  # Seu HTML do formulário

# Rota para processar o envio do formulário
@app.route("/enviar", methods=["POST"])
def enviar_email():
    try:
        # Captura os dados do formulário
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Validações básicas
        if not name or not email or not message:
            return jsonify({"status": "error", "message": "Todos os campos são obrigatórios."})

        # Configura e envia o email
        yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)
        assunto = f"Nova mensagem de {name}"
        conteudo = f"Nome: {name}\nEmail: {email}\n\nMensagem:\n{message}"
        yag.send(to=EMAIL_ADDRESS, subject=assunto, contents=conteudo)

        # Resposta JSON para feedback no frontend
        return jsonify({"status": "success", "message": "Mensagem enviada com sucesso!"})

    except Exception as e:
        return jsonify({"status": "error", "message": f"Erro ao enviar a mensagem: {e}"})

if __name__ == "__main__":
    app.run(debug=True)