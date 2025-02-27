import React from "react";

function Listado({ elementos }) {
  return (
    <ul>
      <hr></hr>
      {elementos.map((elemento) => (
        <p
          style={{ background: "grey", color: "white", fontWeight: "bold" }}
          key={elemento.id}>
          {elemento.id} - {elemento.titulo}
        </p>
      ))}
      <hr></hr>
    </ul>
  );
}
export default Listado;
