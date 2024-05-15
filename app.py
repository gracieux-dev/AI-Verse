# streamlit app.py
import streamlit as st
import streamlit_shadcn_ui as ui
from streamlit_extras.stylable_container import stylable_container
from streamlit_option_menu import option_menu

st.set_page_config(page_title="LANGUATOUR AI", page_icon="", layout="wide")

st.markdown("""
            <style>

            </style>

            """,
            unsafe_allow_html=True)


value = ui.tabs(options=['DISCOVERY', 'TRANSLATION', 'LEARN'], default_value='DISCOVERY', key="kanaries")

with ui.card(key="image"):
    if value == "DISCOVERY":
        with stylable_container(
                key="card2",
                css_styles="""
                    
                """    
            ):
            with ui.card(key="card2"):
                
                ui.element("button", key="card2_btn", text="Nest Submmit", variant="outline")
        with ui.card(key="card"):
            ui.element("button", key="card2_btn", text="Nest Submmit", variant="outline")
        with ui.card(key="card"):
            ui.element("button", key="card2_btn", text="Nest Submmit", variant="outline")
        with ui.card(key="card"):
            ui.element("button", key="card2_btn", text="Nest Submmit", variant="outline")
    elif value == "LEARN":
        with ui.card(key="learn"):
            col1, col2 = st.columns([1, 2], gap="medium")

            with col1:
                st.image('icon.png', width=50)

            with col2:
                with stylable_container(
                    key="text",
                    css_styles="""

                    """
                ):
                    st.markdown("BEGINNERS")
                    st.markdown("cotent for beginner")

                

