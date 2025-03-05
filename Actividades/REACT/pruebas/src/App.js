import React from "react";
import Header from "./componentes/header";
import "bootstrap/dist/css/bootstrap.min.css";
import Listado from "./componentes/listado";
import Leerjson from "./componentes/leerjson";

function App() {
  /**
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
  );*/

return (
    <div>
      <Header></Header>
      <Leerjson></Leerjson>
    </div>
  );


}
export default App;
