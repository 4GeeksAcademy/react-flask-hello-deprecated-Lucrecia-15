const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			token: localStorage.getItem("token") || null, //busca el token del  localStorage del navegador
			user: null, //el usuario comienza como null hasta que se cargue la información del usuario.
			
		},
		actions: {
			// Acción para iniciar sesión
			login: (token, user) => {
				setStore({ token: token, user: user });
			},

			// Acción para cerrar sesión
			logout: () => {
				localStorage.removeItem("token");
				setStore({ token: null, user: null });
			},
		},
	};
};

export default getState;