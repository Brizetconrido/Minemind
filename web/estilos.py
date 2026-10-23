
import streamlit as st


def aplicar_estilos():
    # Estilos generales de la página
    st.markdown(
        """
        <style>
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
            }

            .main-title {
                font-size: 2.5rem;
                font-weight: 700;
                color: #2563eb;
            }

            .subtitle {
                color: #64748b;
                font-size: 1.05rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
