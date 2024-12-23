let estado = "inicio";
let estadoAnterior = null;
let mensajeSistemaAnterior = "";
const inputMensaje = document.getElementById("input-mensaje");
const enviarBtn = document.getElementById("enviar-btn");

inputMensaje.addEventListener("input", function (e) {
    const valor = e.target.value;
    if (!/^[1-6]?$/.test(valor)) {
        e.target.value = valor.slice(0, -1);
    }
});

inputMensaje.addEventListener("keypress", function (e) {
    if (e.key === "Enter" && /^[1-6]$/.test(inputMensaje.value)) {
        enviarMensaje();
    }
});

enviarBtn.addEventListener("click", function () {
    if (/^[1-6]$/.test(inputMensaje.value)) {
        enviarMensaje();
    } else {
        alert("Ingresa un número entre 1 y 6.");
    }
});

function enviarMensaje() {
    const mensaje = inputMensaje.value.trim();
    if (!mensaje) return;
    const chatBox = document.getElementById("chat-box");

    const nuevoMensajeUsuario = document.createElement("div");
    nuevoMensajeUsuario.classList.add("mensaje-usuario", "slide-in");
    nuevoMensajeUsuario.innerText = mensaje;
    chatBox.appendChild(nuevoMensajeUsuario);

    estadoAnterior = estado;

    inputMensaje.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    fetch("/respuesta", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ estado: estado, respuesta: mensaje })
    })
    .then(response => response.json())
    .then(data => {
        if (data.mensaje === "No entiendo tu respuesta. Intenta de nuevo.") {
            const mensajeError = document.createElement("div");
            mensajeError.classList.add("mensaje-sistema", "fade-in");
            mensajeError.innerText = "No entiendo tu respuesta. Intenta de nuevo.";
            chatBox.appendChild(mensajeError);

            const mensajeAnteriorSistema = document.createElement("div");
            mensajeAnteriorSistema.classList.add("mensaje-sistema", "fade-in");
            mensajeAnteriorSistema.innerText = `${mensajeSistemaAnterior}`;
            chatBox.appendChild(mensajeAnteriorSistema);

            estado = estadoAnterior;
        } else {
            mensajeSistemaAnterior = data.mensaje;

            const nuevoMensajeSistema = document.createElement("div");
            nuevoMensajeSistema.classList.add("mensaje-sistema", "fade-in");
            nuevoMensajeSistema.innerText = data.mensaje;
            chatBox.appendChild(nuevoMensajeSistema);

            estado = data.estado;
        }
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(err => console.error("Error:", err));
}
