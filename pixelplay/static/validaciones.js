document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("formRegistro");

  form.addEventListener("submit", function (event) {
    if (!validarFormulario()) {
      event.preventDefault();
      event.stopPropagation();
    } else {
      guardarDatos();
      alert("Registro exitoso. ¡Bienvenido a PixelPlay!");
    }
  });

  function guardarDatos() {
    const usuario = {
      nombre: document.getElementById("nombreCompleto").value,
      username: document.getElementById("usuario").value,
      correo: document.getElementById("correo").value,
      fechaNacimiento: document.getElementById("fechaNacimiento").value,
    };
    localStorage.setItem("usuarioPixelPlay", JSON.stringify(usuario));
  }

  function validarFormulario() {
    let valido = true;
    let mensajeError = "";

    // Validar Nombre Completo
    const nombre = document.getElementById("nombreCompleto").value.trim();
    if (nombre === "") {
      valido = false;
      mensajeError += "Por favor ingrese su nombre completo.\n";
    }

    // Validar Nombre de Usuario
    const usuario = document.getElementById("usuario").value.trim();
    if (usuario === "") {
      valido = false;
      mensajeError += "Debe ingresar un nombre de usuario.\n";
    }

    // Validar Correo Electrónico
    const correo = document.getElementById("correo").value.trim();
    const regexCorreo = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!regexCorreo.test(correo)) {
      valido = false;
      mensajeError += "Ingrese un correo válido.\n";
    }

    // Validar Contraseña
    const clave = document.getElementById("clave").value;
    const repetirClave = document.getElementById("repetirClave").value;
    const regexClave = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,18}$/;
    if (!regexClave.test(clave)) {
      valido = false;
      mensajeError +=
        "La contraseña debe tener al menos 6 caracteres y una mayúscula.\n";
    }

    // Validar que las contraseñas coincidan
    if (clave !== repetirClave) {
      valido = false;
      mensajeError += "Las contraseñas deben coincidir.\n";
    }

    // Validar Fecha de Nacimiento (mayor de 13 años)
    const fechaNacimiento = new Date(
      document.getElementById("fechaNacimiento").value
    );
    const hoy = new Date();
    const edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
    if (edad < 13) {
      valido = false;
      mensajeError += "Debes ser mayor de 13 años.\n";
    }

    if (!valido) {
      alert(mensajeError);
    }

    return valido;
  }
});
