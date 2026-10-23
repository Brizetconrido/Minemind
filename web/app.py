
import streamlit as st
import pandas as pd
from io import BytesIO

from estilos import aplicar_estilos


st.set_page_config(
    page_title="MineMind | Minería de Datos",
    layout="wide"
)

# Aplicar estilos
aplicar_estilos()

# Encabezado
st.markdown(
    '<div class="main-title">MineMind</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Plataforma de administración de minería de datos</div>',
    unsafe_allow_html=True
)
st.divider()

# Menú principal
seccion = st.sidebar.radio(
    "Navegación principal",
    [
        "Inicio",
        "Carga de datos",
        "Limpieza de datos",
        "Árbol de decisión",
        "Reglas de asociación",
        "Dashboard",
        "Informes"
    ]
)

# Datos de la sesión
if "datos" not in st.session_state:
    st.session_state["datos"] = None


if seccion == "Inicio":
    st.subheader("Bienvenido a MineMind")
    st.write(
        "Esta plataforma permitirá cargar, preparar y analizar "
        "datos mediante técnicas de minería de datos."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("**01 · Datos**\n\nCarga y revisión de archivos CSV.")

    with col2:
        st.info(
            "**02 · Análisis**\n\n"
            "Árboles de decisión y reglas de asociación."
        )

    with col3:
        st.info(
            "**03 · Resultados**\n\n"
            "Gráficos, métricas e informes."
        )

    st.subheader("Comienza aquí")
    st.write(
        "Selecciona **Carga de datos** en el menú lateral "
        "para comenzar a trabajar con un archivo CSV."
    )


elif seccion == "Carga de datos":
    st.subheader("Carga y revisión de datos")
    st.write(
        "Selecciona un archivo CSV para revisar su contenido "
        "antes de realizar la limpieza."
    )

    archivo = st.file_uploader(
        "Seleccionar archivo CSV",
        type=["csv"],
        help="Se admiten archivos con extensión .csv."
    )

    if archivo is not None:
        try:
            contenido = archivo.getvalue()
            datos = None

            # Probar codificaciones habituales
            for codificacion in ["utf-8-sig", "utf-8", "latin-1"]:
                try:
                    datos = pd.read_csv(
                        BytesIO(contenido),
                        sep=None,
                        engine="python",
                        encoding=codificacion
                    )
                    break
                except (UnicodeDecodeError, pd.errors.ParserError):
                    continue

            if datos is None:
                st.error(
                    "No fue posible leer el archivo. "
                    "Revisa su formato y codificación."
                )

            elif datos.empty or len(datos.columns) == 0:
                st.warning("El archivo no contiene datos para analizar.")

            else:
                st.session_state["datos"] = datos

                st.success("El archivo CSV se cargó correctamente.")

                col1, col2, col3 = st.columns(3)

                col1.metric("Filas", f"{datos.shape[0]:,}")
                col2.metric("Columnas", f"{datos.shape[1]:,}")
                col3.metric(
                    "Valores vacíos",
                    f"{int(datos.isna().sum().sum()):,}"
                )

                st.subheader("Vista previa")
                st.dataframe(
                    datos.head(10),
                    use_container_width=True
                )

                st.subheader("Tipos de datos")

                tipos = pd.DataFrame({
                    "Columna": datos.columns.astype(str),
                    "Tipo de dato": datos.dtypes.astype(str).values,
                    "Valores vacíos": datos.isna().sum().values,
                    "Valores únicos": datos.nunique().values
                })

                st.dataframe(tipos, use_container_width=True)

        except Exception as error:
            st.error(f"No se pudo procesar el archivo: {error}")

    elif st.session_state["datos"] is not None:
        st.info("Ya hay un archivo cargado en esta sesión.")


elif seccion == "Limpieza de datos":
    st.subheader("Limpieza de datos")
    st.write(
        "En esta sección se revisarán los valores vacíos, "
        "duplicados, tipos de datos y posibles valores atípicos."
    )

    if st.session_state["datos"] is None:
        st.warning(
            "Primero carga un archivo en la sección Carga de datos."
        )
    else:
        st.info(
            "Los datos están cargados. "
            "Aquí incorporaremos las funciones de limpieza."
        )


elif seccion == "Árbol de decisión":
    st.subheader("Árbol de decisión")
    st.write(
        "Aquí se configurarán las variables, "
        "los parámetros del árbol y sus métricas."
    )


elif seccion == "Reglas de asociación":
    st.subheader("Reglas de asociación")
    st.write(
        "Aquí se analizarán las reglas mediante "
        "soporte, confianza y lift."
    )


elif seccion == "Dashboard":
    st.subheader("Dashboard de análisis")
    st.write(
        "Aquí se incorporarán gráficos y visualizaciones "
        "de los datos y resultados."
    )


elif seccion == "Informes":
    st.subheader("Informes")
    st.write(
        "Aquí se generarán informes con los datos, "
        "la limpieza, los modelos y sus conclusiones."
    )


st.divider()
st.caption("MineMind | Proyecto de minería de datos")
