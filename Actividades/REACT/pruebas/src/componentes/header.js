import React from "react";
const Header = () => {
  return (
    <header className="header">
      <img
        style={{ width: "100vw", height: "25vh" }}
        src="https://picsum.photos/seed/picsum/200/300"
        alt=" montaña"
        className="imagen"
      />
      <h1 style={{ textAlign: "center" }} className="titulo">
        cabecera para proyecto react web
      </h1>
      <p style={{ textAlign: "center", fontSize: "18px" }} className="Slogan">
        Genera tus webs de forma rapida con componentes{" "}
      </p>
      <hr />
    </header>
  );
};
export default Header;
