document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const searchBtn = document.getElementById("searchBtn");
    const resultsContainer = document.getElementById("resultsContainer");

    // Función principal de búsqueda asíncrona
    async function realizarBusqueda() {
        const query = searchInput.value.trim();
        console.info(`[Frontend DevTools] Iniciando petición GET a /api/buscar con parámetro: "${query}"`);

        try {
            const response = await fetch(`/api/buscar?q=${encodeURIComponent(query)}`);
            
            if (!response.ok) {
                throw new Error(`Error en la respuesta del servidor: ${response.status}`);
            }

            const data = await response.json();
            console.table(data); // Muestra los resultados estructurados en forma de tabla en la consola de Google
            renderizarResultados(data);

        } catch (error) {
            console.error("[Frontend DevTools Error] Fallo al conectar con la API:", error);
            resultsContainer.innerHTML = `<p style="color: red;">Error al consultar los registros legales.</p>`;
        }
    }

    // Renderizar los resultados en el DOM
    function renderizarResultados(data) {
        resultsContainer.innerHTML = "";

        if (data.length === 0) {
            resultsContainer.innerHTML = `<p>No se encontraron registros legales coincidentes.</p>`;
            return;
        }

        data.forEach(item => {
            const div = document.createElement("div");
            div.className = "legal-item";
            div.innerHTML = `
                <h4>${item.codigo} - ${item.articulo}</h4>
                <span>${item.titulo}</span>
                <p>${item.contenido}</p>
            `;
            resultsContainer.appendChild(div);
        });
    }

    // Eventos de interacción
    searchBtn.addEventListener("click", realizarBusqueda);
    searchInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            realizarBusqueda();
        }
    });

    // Carga inicial al abrir la página
    realizarBusqueda();
});