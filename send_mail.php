<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Capture os dados  do formulário
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    // Configurações do email
    $to = "gustavocandido044@gmail.com";
    $subject = "Nova mensagem do formulário contato";
    $body = "Nome: $name\nEmail: $email\nMensagem: \n$message";
    $headers = "From: $email\r\n";

    // Envia o email
    if (mail($to, $subject, $body, $headers)) {
        echo "Mensagem enviada com sucesso";
    } else {
        echo "Ocorreu um erro ao enviar sua mensagem. Tente novamente mais tarde.";
    }
} else {
    echo "Método inválido.";
}
?>