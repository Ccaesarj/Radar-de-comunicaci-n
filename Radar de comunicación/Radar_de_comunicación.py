import flet as ft

dispositivos = [
    {"nombre": "Router A", "hijos": ["PC 1", "PC 2"]},
    {"nombre": "Router B", "hijos": ["PC 3", "Tablet"]},
]

def main(page: ft.Page):
    page.title = "Red Visual con Flet"
    page.vertical_alignment = "start"
    page.bgcolor = ft.colors.GREY_200

    routers_row = ft.Row(spacing=20, wrap=False)
    hijos_row = ft.Row(spacing=20, wrap=False)

    titulo = ft.Text("Red de Dispositivos", size=30, weight="bold")

    def mostrar_hijos(hijos):
        hijos_row.controls.clear()
        for hijo in hijos:
            hijos_row.controls.append(
                ft.Container(
                    content=ft.Text(hijo, size=18, color=ft.colors.WHITE),
                    bgcolor=ft.colors.BLUE_GREY_400,
                    padding=20,
                    border_radius=10,
                )
            )
        page.update()

    for disp in dispositivos:
        boton = ft.ElevatedButton(
            disp["nombre"],
            on_click=lambda e, hijos=disp["hijos"]: mostrar_hijos(hijos),
            style=ft.ButtonStyle(bgcolor=ft.colors.BLUE, padding=20)
        )
        routers_row.controls.append(boton)

    page.add(
        titulo,
        ft.Container(routers_row, padding=20),
        ft.Container(hijos_row, padding=20),
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000)

