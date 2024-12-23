base_conocimiento = {
    "inicio": {
        "pregunta": "INICIO\n¿Qué deseas saber sobre Desarrollo Web?\n(1: HTML, 2: CSS, 3: JavaScript, 4: Frameworks Web, 5: Backend, 6: Salir)",
        "respuestas": {
            "1": "html",
            "2": "css",
            "3": "javascript",
            "4": "frameworks_web",
            "5": "backend",
            "6": "salir"
        },
    },
    "html": {
        "pregunta": "¿Qué deseas saber sobre HTML?\n(1: Estructura, 2: Etiquetas, 3: Formularios, 4: Retroceder, 5: Salir)",
        "respuestas": {
            "1": "html_estructura",
            "2": "html_etiquetas",
            "3": "html_formularios",
            "4": "inicio",
            "5": "salir"
        },
    },
    "html_estructura": {
        "pregunta": "¿Qué deseas saber sobre la estructura de HTML?\n(1: Elementos, 2: Atributos, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "html_estructura_elementos",
            "2": "html_estructura_atributos",
            "3": "html",
            "4": "inicio",
            "5": "salir"
        },
    },
    "html_estructura_elementos": {
        "respuesta_final": "Los elementos de HTML son los bloques básicos de construcción de las páginas web.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "html_estructura",
            "2": "inicio",
            "3": "salir"
        },
    },
    "html_estructura_atributos": {
        "respuesta_final": "Los atributos de HTML proporcionan información adicional sobre los elementos, como 'class' o 'id'.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "html_estructura",
            "2": "inicio",
            "3": "salir"
        },
    },
    "html_etiquetas": {
        "pregunta": "¿Qué deseas saber sobre las etiquetas de HTML?\n(1: Etiquetas semánticas, 2: Etiquetas no semánticas, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "html_etiquetas_semanticas",
            "2": "html_etiquetas_no_semanticas",
            "3": "html",
            "4": "inicio",
            "5": "salir"
        },
    },
    "html_etiquetas_semanticas": {
        "respuesta_final": "Las etiquetas semánticas de HTML, como < header > y < article >, tienen un significado claro para los navegadores y desarrolladores.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "html_etiquetas",
            "2": "inicio",
            "3": "salir"
        },
    },
    "html_etiquetas_no_semanticas": {
        "respuesta_final": "Las etiquetas no semánticas de HTML, como < div > y < span >, no tienen un significado específico.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "html_etiquetas",
            "2": "inicio",
            "3": "salir"
        },
    },
    "html_formularios": {
        "pregunta": "¿Qué deseas saber sobre los formularios de HTML?\n(1: Campos de entrada, 2: Validación, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "html_formularios_campos",
            "2": "html_formularios_validacion",
            "3": "html",
            "4": "inicio",
            "5": "salir"
        },
    },
    "html_formularios_campos": {
        "respuesta_final": "Los formularios en HTML permiten capturar datos de usuarios mediante campos como < input >, < textarea > y < select >.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "html_formularios",
            "2": "inicio",
            "3": "salir"
        },
    },
    "html_formularios_validacion": {
        "respuesta_final": "HTML permite validar formularios con atributos como 'required', 'pattern' y 'type'.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "html_formularios",
            "2": "inicio",
            "3": "salir"
        },
    },
    "css": {
        "pregunta": "¿Qué deseas saber sobre CSS?\n(1: Estilos básicos, 2: Diseño avanzado, 3: Animaciones, 4: Retroceder, 5: Salir)",
        "respuestas": {
            "1": "css_estilos_basicos",
            "2": "css_diseno_avanzado",
            "3": "css_animaciones",
            "4": "inicio",
            "5": "salir"
        },
    },
    "css_estilos_basicos": {
        "pregunta": "¿Qué deseas saber sobre estilos básicos en CSS?\n(1: Colores, 2: Tipografía, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "css_estilos_basicos_colores",
            "2": "css_estilos_basicos_tipografia",
            "3": "css",
            "4": "inicio",
            "5": "salir"
        },
    },
    "css_estilos_basicos_colores": {
        "respuesta_final": "CSS permite aplicar colores a elementos usando palabras clave, valores hexadecimales o RGB.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "css_estilos_basicos",
            "2": "inicio",
            "3": "salir"
        },
    },
    "css_estilos_basicos_tipografia": {
        "respuesta_final": "CSS permite cambiar la tipografía con propiedades como 'font-family' y 'font-size'.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "css_estilos_basicos",
            "2": "inicio",
            "3": "salir"
        },
    },
    "css_diseno_avanzado": {
        "pregunta": "¿Qué deseas saber sobre diseño avanzado en CSS?\n(1: Flexbox, 2: Grid, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "css_diseno_avanzado_flexbox",
            "2": "css_diseno_avanzado_grid",
            "3": "css",
            "4": "inicio",
            "5": "salir"
        },
    },
    "css_diseno_avanzado_flexbox": {
        "respuesta_final": "Flexbox es un modelo de diseño unidimensional en CSS para alinear y distribuir elementos dentro de un contenedor.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "css_diseno_avanzado",
            "2": "inicio",
            "3": "salir"
        },
    },
    "css_diseno_avanzado_grid": {
        "respuesta_final": "Grid es un sistema bidimensional en CSS que permite organizar elementos en filas y columnas.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "css_diseno_avanzado",
            "2": "inicio",
            "3": "salir"
        },
    },
    "css_animaciones": {
        "pregunta": "¿Qué deseas saber sobre animaciones en CSS?\n(1: Transiciones, 2: Keyframes, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "css_animaciones_transiciones",
            "2": "css_animaciones_keyframes",
            "3": "css",
            "4": "inicio",
            "5": "salir"
        },
    },
    "css_animaciones_transiciones": {
        "respuesta_final": "Las transiciones permiten animar cambios en las propiedades CSS de un elemento.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "css_animaciones",
            "2": "inicio",
            "3": "salir"
        },
    },
    "css_animaciones_keyframes": {
        "respuesta_final": "Los keyframes permiten definir etapas en una animación CSS.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "css_animaciones",
            "2": "inicio",
            "3": "salir"
        },
    },
    "javascript": {
        "pregunta": "¿Qué deseas saber sobre JavaScript?\n(1: Fundamentos, 2: DOM, 3: ES6, 4: Retroceder, 5: Salir)",
        "respuestas": {
            "1": "javascript_fundamentos",
            "2": "javascript_dom",
            "3": "javascript_es6",
            "4": "inicio",
            "5": "salir"
        },
    },
    "javascript_fundamentos": {
        "pregunta": "¿Qué deseas saber sobre los fundamentos de JavaScript?\n(1: Variables, 2: Tipos de datos, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "javascript_fundamentos_variables",
            "2": "javascript_fundamentos_tipos",
            "3": "javascript",
            "4": "inicio",
            "5": "salir"
        },
    },
    "javascript_fundamentos_variables": {
        "respuesta_final": "En JavaScript, las variables se declaran usando 'var', 'let' o 'const'.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "javascript_fundamentos",
            "2": "inicio",
            "3": "salir"
        },
    },
    "javascript_fundamentos_tipos": {
        "respuesta_final": "JavaScript tiene varios tipos de datos, incluidos strings, números, booleanos, objetos y arrays.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "javascript_fundamentos",
            "2": "inicio",
            "3": "salir"
        },
    },
    "javascript_dom": {
        "pregunta": "¿Qué deseas saber sobre el DOM en JavaScript?\n(1: Selección de elementos, 2: Manipulación de eventos, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "javascript_dom_seleccion",
            "2": "javascript_dom_eventos",
            "3": "javascript",
            "4": "inicio",
            "5": "salir"
        },
    },
    "javascript_dom_seleccion": {
        "respuesta_final": "El DOM permite seleccionar elementos usando métodos como 'getElementById' o 'querySelector'.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "javascript_dom",
            "2": "inicio",
            "3": "salir"
        },
    },
    "javascript_dom_eventos": {
        "respuesta_final": "JavaScript permite manejar eventos como 'click' o 'mouseover' con 'addEventListener'.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "javascript_dom",
            "2": "inicio",
            "3": "salir"
        },
    },
    "javascript_es6": {
        "pregunta": "¿Qué deseas saber sobre ES6?\n(1: Arrow Functions, 2: Promesas, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "javascript_es6_arrow_functions",
            "2": "javascript_es6_promesas",
            "3": "javascript",
            "4": "inicio",
            "5": "salir"
        },
    },
    "javascript_es6_arrow_functions": {
        "respuesta_final": "Las Arrow Functions son una forma más concisa de escribir funciones en JavaScript introducidas en ES6.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "javascript_es6",
            "2": "inicio",
            "3": "salir"
        },
    },
    "javascript_es6_promesas": {
        "respuesta_final": "Las promesas en JavaScript son utilizadas para manejar operaciones asíncronas de manera más sencilla y legible.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "javascript_es6",
            "2": "inicio",
            "3": "salir"
        },
    },
    "frameworks_web": {
        "pregunta": "¿Qué deseas saber sobre Frameworks Web?\n(1: React, 2: Angular, 3: Vue, 4: Retroceder, 5: Salir)",
        "respuestas": {
            "1": "frameworks_web_react",
            "2": "frameworks_web_angular",
            "3": "frameworks_web_vue",
            "4": "inicio",
            "5": "salir"
        },
    },
    "frameworks_web_react": {
        "pregunta": "¿Qué deseas saber sobre React?\n(1: Componentes, 2: Hooks, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "frameworks_web_react_componentes",
            "2": "frameworks_web_react_hooks",
            "3": "frameworks_web",
            "4": "inicio",
            "5": "salir"
        },
    },
    "frameworks_web_react_componentes": {
        "respuesta_final": "React utiliza componentes reutilizables para construir interfaces dinámicas.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "frameworks_web_react",
            "2": "inicio",
            "3": "salir"
        },
    },
    "frameworks_web_react_hooks": {
        "respuesta_final": "Los hooks en React, como useState y useEffect, permiten manejar el estado y los efectos en componentes funcionales.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "frameworks_web_react",
            "2": "inicio",
            "3": "salir"
        },
    },
    "frameworks_web_angular": {
        "pregunta": "¿Qué deseas saber sobre Angular?\n(1: Directivas, 2: Servicios, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "frameworks_web_angular_directivas",
            "2": "frameworks_web_angular_servicios",
            "3": "frameworks_web",
            "4": "inicio",
            "5": "salir"
        },
    },
    "frameworks_web_angular_directivas": {
        "respuesta_final": "Las directivas en Angular permiten manipular el DOM, como *ngFor para iterar elementos.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "frameworks_web_angular",
            "2": "inicio",
            "3": "salir"
        },
    },
    "frameworks_web_angular_servicios": {
        "respuesta_final": "Los servicios en Angular permiten compartir datos y lógica entre componentes de forma eficiente.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "frameworks_web_angular",
            "2": "inicio",
            "3": "salir"
        },
    },
    "frameworks_web_vue": {
        "pregunta": "¿Qué deseas saber sobre Vue?\n(1: Plantillas, 2: Propiedades Reactivas, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "frameworks_web_vue_plantillas",
            "2": "frameworks_web_vue_propiedades",
            "3": "frameworks_web",
            "4": "inicio",
            "5": "salir"
        },
    },
    "frameworks_web_vue_plantillas": {
        "respuesta_final": "Las plantillas en Vue utilizan una sintaxis declarativa para vincular datos con el DOM.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "frameworks_web_vue",
            "2": "inicio",
            "3": "salir"
        },
    },
    "frameworks_web_vue_propiedades": {
        "respuesta_final": "Las propiedades reactivas en Vue permiten actualizar automáticamente el DOM al cambiar los datos.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "frameworks_web_vue",
            "2": "inicio",
            "3": "salir"
        },
    },
    "backend": {
        "pregunta": "¿Qué deseas saber sobre Backend?\n(1: Bases de datos, 2: Servidores, 3: APIs, 4: Retroceder, 5: Salir)",
        "respuestas": {
            "1": "backend_bases_datos",
            "2": "backend_servidores",
            "3": "backend_apis",
            "4": "inicio",
            "5": "salir"
        },
    },
    "backend_bases_datos": {
        "pregunta": "¿Qué deseas saber sobre bases de datos?\n(1: Tipos de bases de datos, 2: Consultas SQL, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "backend_bases_datos_tipos",
            "2": "backend_bases_datos_consultas",
            "3": "backend",
            "4": "inicio",
            "5": "salir"
        },
    },
    "backend_bases_datos_tipos": {
        "respuesta_final": "Las bases de datos pueden ser relacionales como MySQL o no relacionales como MongoDB.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "backend_bases_datos",
            "2": "inicio",
            "3": "salir"
        },
    },
    "backend_bases_datos_consultas": {
        "respuesta_final": "Las consultas SQL permiten recuperar y manipular datos almacenados en bases de datos relacionales.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "backend_bases_datos",
            "2": "inicio",
            "3": "salir"
        },
    },
    "backend_servidores": {
        "pregunta": "¿Qué deseas saber sobre servidores?\n(1: Tipos de servidores, 2: HTTP y Sockets, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "backend_servidores_tipos",
            "2": "backend_servidores_http_sockets",
            "3": "backend",
            "4": "inicio",
            "5": "salir"
        },
    },
    "backend_servidores_tipos": {
        "respuesta_final": "Los servidores pueden ser dedicados, compartidos o en la nube, según su propósito y escalabilidad.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "backend_servidores",
            "2": "inicio",
            "3": "salir"
        },
    },
    "backend_servidores_http_sockets": {
        "respuesta_final": "HTTP es un protocolo para transferir datos, mientras que Sockets permite la comunicación en tiempo real entre cliente y servidor.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "backend_servidores",
            "2": "inicio",
            "3": "salir"
        },
    },
    "backend_apis": {
        "pregunta": "¿Qué deseas saber sobre APIs?\n(1: REST, 2: GraphQL, 3: Retroceder, 4: Inicio, 5: Salir)",
        "respuestas": {
            "1": "backend_apis_rest",
            "2": "backend_apis_graphql",
            "3": "backend",
            "4": "inicio",
            "5": "salir"
        },
    },
    "backend_apis_rest": {
        "respuesta_final": "REST es un estándar para crear APIs basadas en recursos y operaciones HTTP como GET, POST, PUT y DELETE.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "backend_apis",
            "2": "inicio",
            "3": "salir"
        },
    },
    "backend_apis_graphql": {
        "respuesta_final": "GraphQL es un lenguaje de consulta para APIs que permite a los clientes solicitar datos específicos de manera eficiente.\n(1: Retroceder, 2: Inicio, 3: Salir)",
        "respuestas": {
            "1": "backend_apis",
            "2": "inicio",
            "3": "salir"
        },
    },
    "salir": {
        "respuesta_final": "Gracias por usar el chat de Desarrollo Web. :D",
        "respuestas": {}
    },
}

def obtener_pregunta(estado):
    nodo_actual = base_conocimiento.get(estado, {})
    return nodo_actual.get("pregunta"), nodo_actual.get("respuestas")

def obtener_respuesta_final(estado):
    nodo_actual = base_conocimiento.get(estado, {})
    return nodo_actual.get("respuesta_final")
