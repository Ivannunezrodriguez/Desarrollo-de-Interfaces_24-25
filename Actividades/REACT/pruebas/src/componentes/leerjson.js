import React, { useState, useEffect } from "react";

function Leerjson() {
  const [datos, setDatos] = useState([]);
  useEffect(() => {
    leerDatos();
  }, []);

  const leerDatos = async () => {
    try {
      const respuesta = await fetch("/datos.json");
      const jsonDatos = await respuesta.json();
      setDatos(jsonDatos);
    } catch (error) {
      console.error("error en la carga de datos: ", error);
    }
  };
  return (
    <div style={{ textAlign: "center" }}>
      <h2>Leer datos de un archivo json</h2>

        {datos.map((elemento,index) => (
          <h5 key={index}>
                {index +1} . {elemento.nombre} - {elemento.edad} - {elemento.ciudad}
          </h5>
        ))}
 
    </div>
  );
}

export default Leerjson;
