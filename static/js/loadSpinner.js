// Esperar a que el contenido de la página se cargue completamente
window.addEventListener('load', function() {
    // Hacer desaparecer la pantalla de carga
    var loadingScreen = document.getElementById('loading-screen');
    if (loadingScreen) {
        loadingScreen.style.display = 'none';
    }
});