document.addEventListener('DOMContentLoaded', function() {
    // Obtener todas las imágenes en la página
    var images = document.querySelectorAll('img');
    var totalImages = images.length;
    var loadedImages = 0;

    // Función para ocultar el spinner
    function hideSpinner() {
        var loadingScreen = document.getElementById('loading-screen');
        if (loadingScreen) {
            loadingScreen.style.transition = 'opacity 0.5s ease-out'; // Transición suave
            loadingScreen.style.opacity = '0'; // Desvanecer el spinner
            setTimeout(function() {
                loadingScreen.style.visibility = 'hidden'; // Hacerlo invisible después de la transición
            }, 500); // Asegura que el spinner quede oculto después de la transición
        }
    }

    // Verificar si todas las imágenes se han cargado
    images.forEach(function(image) {
        image.onload = function() {
            loadedImages++;
            // Cuando todas las imágenes están cargadas, ocultamos el spinner
            if (loadedImages === totalImages) {
                hideSpinner();
            }
        };
    });

    // Si no hay imágenes, ocultamos el spinner inmediatamente
    if (totalImages === 0) {
        hideSpinner();
    }
});