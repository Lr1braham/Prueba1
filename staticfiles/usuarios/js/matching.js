// matching.js

// Simulación de usuarios registrados
const usuarios = [
    { id: 1, nombre: "Ana", edad: 28, intereses: ["música", "cine", "viajes"] },
    { id: 2, nombre: "Carlos", edad: 30, intereses: ["deportes", "viajes", "tecnología"] },
    { id: 3, nombre: "Luisa", edad: 26, intereses: ["lectura", "cine", "música"] },
    { id: 4, nombre: "Javier", edad: 29, intereses: ["viajes", "fotografía", "cine"] },
    { id: 5, nombre: "Sofía", edad: 31, intereses: ["música", "deportes", "lectura"] }
];

// Función para calcular afinidad por intereses compartidos
function calcularAfinidad(usuarioA, usuarioB) {
    const interesesComunes = usuarioA.intereses.filter(interes =>
        usuarioB.intereses.includes(interes)
    );
    return interesesComunes.length;
}

// Función para encontrar los mejores matches de un usuario
function encontrarMatches(usuarioActual) {
    const posiblesMatches = usuarios.filter(u => u.id !== usuarioActual.id);
    
    const matchesOrdenados = posiblesMatches
        .map(u => ({
            usuario: u,
            afinidad: calcularAfinidad(usuarioActual, u)
        }))
        .sort((a, b) => b.afinidad - a.afinidad);

    return matchesOrdenados;
}

// Ejemplo de uso
const usuarioEjemplo = { id: 99, nombre: "Tú", edad: 27, intereses: ["música", "cine", "viajes"] };
const matches = encontrarMatches(usuarioEjemplo);

// Mostrar resultados
console.log(`Mejores matches para ${usuarioEjemplo.nombre}:`);
matches.forEach(match => {
    console.log(`- ${match.usuario.nombre} (Afinidad: ${match.afinidad})`);
});
