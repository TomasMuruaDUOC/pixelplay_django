$(document).ready(function () {
    $("#contactForm").submit(function (event) {
        event.preventDefault(); // Evita el envío por defecto
        let isValid = true;

        $(".error-message").hide(); // Ocultar mensajes previos
        $(".form-control").removeClass("is-invalid"); // Quitar estilos previos

        // Validar el campo Nombre (Obligatorio)
        if ($("#nombre").val().trim() === "") {
            $("#nombre").addClass("is-invalid");
            $("#nombre").next(".error-message").text("El nombre es obligatorio.").show();
            isValid = false;
            
        }
        // Validar el nombre usuario (Obligatorio)
        if ($("#usuario").val().trim() === "") {
            $("#usuario").addClass("is-invalid");
            $("#usuario").next(".error-message").text("El nombre de Usurio es obligatorio.").show();
            isValid = false;
        }

        // Validar el campo Email (Obligatorio y formato válido)
       let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if ($("#email").val().trim() === "" || !emailPattern.test($("#email").val())) {
            $("#email").addClass("is-invalid");
            $("#email").next(".error-message").text("Por favor, ingresa un email válido.").show();
            isValid = false;
        }

         // Validar la contraseña
         let passwordPattern = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,18}$/;
         let password = $("#clave").val().trim();
         let confirmPassword = $("#clave2").val().trim(); // Nueva variable para la confirmación
 
         if (password === "" || !passwordPattern.test(password)) {
             $("#clave").addClass("is-invalid");
             $("#clave").next(".error-message").text("La contraseña debe tener entre 6 y 18 caracteres, incluir al menos una mayúscula y un número.").show();
             isValid = false;
         }
 
         // Validar que ambas contraseñas coincidan
         if (password !== confirmPassword) {
             $("#clave2").addClass("is-invalid");
             $("#clave2").next(".error-message").text("Las contraseñas no coinciden.").show();
             isValid = false;
         }
 

         //Validar la fecha de nacimiento, persona no puede tener menos de 13 años(obligatorio)
            let fecha = new Date($("#fecha_nacimiento").val());
        if ($("#fecha_nacimiento").val().trim() === "" || fecha.getFullYear() > 2008) {
            $("#fecha_nacimiento").addClass("is-invalid");
            $("#fecha_nacimiento").next(".error-message").text("Debes ser mayor de 13 años.").show();
            isValid = false;
        }
         //Validar la direccion de despacho (Opcional)
        if ($("#direccion").val().trim() === "") {
            $("#direccion").addClass("is-invalid");
            $("#direccion").next(".error-message").text("La dirección de despacho es obligatoria.").show();
            isValid = false;
        }

        // Validar el checkbox de términos
        if (!$("#terminos").is(":checked")) {
            $("#terminos").next(".error-message").text("Debes aceptar los términos.").show();
            isValid = false;
        }

        // Si todo es válido, mostrar alerta y reiniciar el formulario
        if (isValid) {
            alert("Formulario enviado con éxito!");
            $("#contactForm")[0].reset(); // Reiniciar el formulario
        }
    });
});   