// main.js

document.addEventListener("DOMContentLoaded", () => {
    console.log("Documento listo");

    // Ejemplo: Cambiar el texto de un título
    const titulo = document.querySelector("#titulo-principal");
    if (titulo) {
        titulo.textContent = "¡Bienvenido a nuestra página de citas!";
    }

    // Ejemplo: Manejo de un formulario de registro
    const formRegistro = document.querySelector("#form-registro");
    if (formRegistro) {
        formRegistro.addEventListener("submit", (e) => {
            e.preventDefault();
            
            const nombre = document.querySelector("#nombre").value;
            const correo = document.querySelector("#correo").value;
            const edad = document.querySelector("#edad").value;

            if (nombre && correo && edad) {
                console.log("Registro exitoso:");
                console.log(`Nombre: ${nombre}`);
                console.log(`Correo: ${correo}`);
                console.log(`Edad: ${edad}`);
                alert(`Gracias por registrarte, ${nombre}`);
                formRegistro.reset();
            } else {
                alert("Por favor, completa todos los campos.");
            }
        });
    }

    // Ejemplo: Cambiar estilos al hacer clic
    const btnEstilo = document.querySelector("#btn-estilo");
    if (btnEstilo) {
        btnEstilo.addEventListener("click", () => {
            document.body.classList.toggle("modo-oscuro");
        });
    }
});
