import flet as ft
from flet import *


def main(page: ft.Page):

    #constant
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#303030"


    page.add(
        Card(
            width=360,
            height=200,
            elevation=7
        )
    )



ft.app(main)
