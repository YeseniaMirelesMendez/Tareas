import flet as ft

def Dashboardview(page, tarea_controller):
    user = page.session.get("user")
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    
    def refresh():
    lista_tareas.controls.clear()
<<<<<<< HEAD
    for t in tarea_controller.obtener_lista(user['id_usuario']):
=======
    for t in tarea_controller.obtener_lista(user['id_usuario]):
>>>>>>> bfb3a7d2b98bc81ecf5393a1953ff0595ad30fff
        lista_tareas.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft-ListTile(
                        title=ft.Text(f"{t['description']}\nPrioridad: {t['´prioridad']}"),
<<<<<<< HEAD
                        subtitle=ft.Badge(f"{t['description']}\nPrioridad: {t['prioridad']}"),
                        trailing=ft.Badge(content=ft.Text(t['estado']), bgcolor=ft.Colors.ORANGE_300)
                    ), padding=10
                )
            )
        )
        page.update()
=======
                    )
                )
                )
            
            )
>>>>>>> bfb3a7d2b98bc81ecf5393a1953ff0595ad30fff
