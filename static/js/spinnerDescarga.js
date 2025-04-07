document.getElementById('generarForm').addEventListener('submit', function(event) {
    // Evitar que el formulario se envíe de forma predeterminada
    event.preventDefault();

    // Mostrar el spinner
    document.getElementById('spinner-container').style.display = 'block';

    // Ocultar el botón de generación de archivo
    document.getElementById('form-xlsx').style.display = 'none';

    // Hacer la solicitud AJAX
    var formData = new FormData(this); // Tomamos los datos del formulario
    fetch(this.action, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json()) // Suponiendo que el backend responde con JSON
    .then(data => {
        // Aquí manejamos la respuesta del servidor
        if (data.success) {
            // Mostrar el botón de descarga
            document.getElementById('form-csv').style.display = 'block';
        } else {
            // Si hay un error, mostrar un mensaje
            alert('Hubo un problema generando el archivo');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error en la solicitud');
    })
    .finally(() => {
        // Ocultar el spinner después de completar la solicitud
        document.getElementById('spinner-container').style.display = 'none';
    });
});