import React, { useState, useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

export const Home = () => {
  const { store, actions } = useContext(Context);
  const navigate = useNavigate();
  const [user, setUser] = useState();
  const token = localStorage.getItem("token");

  const logoutUser = () => {
		actions.logout(); // Elimina el token en el store y localStorage
		navigate("/login"); // Redirige al login
	};

  useEffect(() => {
    if (!token) {
        navigate("/login", { replace: true });
    };
}, [token, navigate]);



  return (
    <div className="container d-flex justify-content-center">
      <div className="row">
      <h1>Welcome Geek!</h1>  
      <div className="logout btn btn-primary"
									onClick={() => {
										logoutUser();
									}} >Cerrar Sesión</div>
      </div>
    </div>
  );
};

export default Home;