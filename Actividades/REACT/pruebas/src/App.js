import React from "react";
import Listado from "./componentes/listado";
import "bootstrap/dist/css/bootstrap.min.css";
import { Button, Container } from "react-bootstrap";

function App() {
  const elementos = [
    { id: 1, titulo: "Invierno" },
    { id: 2, titulo: "Primavera" },
    { id: 3, titulo: "Verano" },
    { id: 4, titulo: "Otoño" },
  ];
  return (
    <Container>
      <div className="App">
        <h1>Lista de elementos anuales</h1>
        <Listado elementos={elementos} />
        <strong>
          {" "}
          <Listado elementos={elementos} />
        </strong>
      </div>
      <Button variant="primary">enviar</Button>
    </Container>
  );
}
export default App;
