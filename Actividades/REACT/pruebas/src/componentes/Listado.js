import React from "react";

function Listado({ elementos }) {
    return (
        <ul>
            {elementos.map((elemento) => (
                <li key={elemento.id}>{elemento.titulo}</li>
            ))}
        </ul>
    );
}
export default Listado;
