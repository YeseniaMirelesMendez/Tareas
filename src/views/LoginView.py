import flet as ft

def LoginView(page, auth_controller):

    page.bgcolor = "#1E1E2E"

    email_input = ft.TextField(
        label="Correo electrónico",
        hint_text="ejemplo@gmail.com",
        width=380,
        border_radius=15,
        filled=True,
        bgcolor="#2A2A40",
        color=ft.Colors.WHITE,
        border_color="#6C63FF",
        icon=ft.Icons.EMAIL,
    )

    pass_input = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa tu contraseña",
        width=380,
        password=True,
        can_reveal_password=True,
        border_radius=15,
        filled=True,
        bgcolor="#2A2A40",
        color=ft.Colors.WHITE,
        border_color="#6C63FF",
        icon=ft.Icons.LOCK,
    )

    mensaje_recuperacion = ft.Text(
        "Correo de recuperación enviado",
        color="#A6E3A1",
        visible=False,
        size=14
    )

    def mostrar_mensaje(e):
        mensaje_recuperacion.visible = True
        page.update()

    def cerrar_alerta(e):
        alerta.open = False
        page.update()

    alerta = ft.AlertDialog(
        title=ft.Text("Error"),
        content=ft.Text("Tus datos son incorrectos"),
        bgcolor="#313244",
        actions=[
            ft.TextButton(
                "Cerrar",
                on_click=cerrar_alerta,
                style=ft.ButtonStyle(
                    color=ft.Colors.WHITE
                )
            )
        ]
    )

    def login_click(e):

        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor llena todos los campos")
            )
            page.snack_bar.open = True
            page.update()
            return

        user, msg = auth_controller.login(
            email_input.value,
            pass_input.value
        )

        if user:
            page.user_data = user
            page.go("/dashboard")

        else:
            page.dialog = alerta
            alerta.content = ft.Text(msg)
            alerta.open = True
            page.update()

    login_button = ft.ElevatedButton(
        "Iniciar sesión",
        on_click=login_click,
        width=380,
        height=50,
        bgcolor="#6C63FF",
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
        )
    )

    return ft.View(
        route="/",
        bgcolor="#1E1E2E",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            "Bienvenido",
                            size=34,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE
                        ),

                        ft.Text(
                            "Inicia sesión para continuar",
                            size=16,
                            color="#C0CAF5"
                        ),

                        email_input,
                        pass_input,

                        ft.TextButton(
                            "¿Olvidaste la contraseña?",
                            on_click=mostrar_mensaje,
                            style=ft.ButtonStyle(
                                color="#89B4FA"
                            )
                        ),

                        login_button,

                        mensaje_recuperacion,

                        ft.TextButton(
                            "Crear una cuenta nueva",
                            on_click=lambda _: page.go("/registro"),
                            style=ft.ButtonStyle(
                                color="#F9E2AF"
                            )
                        )

                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=18
                ),

                padding=40,
                border_radius=25,
                bgcolor="#181825",
                width=450,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=20,
                    color=ft.Colors.BLACK54
                )
            )
        ]
    )
