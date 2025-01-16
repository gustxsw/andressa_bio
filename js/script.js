// Exibe uma mensagem no console ao carregar a página
console.log("Página carregada!");

// Captura cliques nos links e registra no console
document.querySelectorAll(".links a").forEach(link => {
    link.addEventListener("click", event => {
        console.log(`Link clicado: ${event.target.textContent}`);
    });
});

// Animação suave ao carregar o conteúdo da página
window.addEventListener("load", () => {
    document.querySelector(".card").classList.add("fade-in");
});

const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();

        // Adicione a mensagem de feedback
        const feedbackElement = document.getElementById('form-feedback');
        if (feedbackElement) {
            feedbackElement.textContent = 'Obrigado por entrar em contato! Responderemos em breve.';
        }

        // Reseta o formulário
        contactForm.reset();
    });
}

// Suaviza transições de foco nos links
document.querySelectorAll(".links a, .footer a").forEach(link => {
    link.addEventListener("focus", () => {
        link.style.outline = "2px solid var(--primary-color)";
    });

    link.addEventListener("blur", () => {
        link.style.outline = "none";
    });
});
