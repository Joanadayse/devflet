import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Hashzap"
    pagina.horizontal_alignment = "center"
    pagina.vertical_alignment = "center"
    pagina.bgcolor = "#e0e0e0"  # um fundo cinza claro, mas não branco

    titulo = ft.Text("Hashzap", size=30, weight="bold", color=ft.colors.BLACK)

    campo_nome = ft.TextField(label="Digite o seu nome", width=300)
    botao_entrar = ft.ElevatedButton("Entrar no chat", width=300, style=ft.ButtonStyle(bgcolor=ft.colors.BLUE))

    # Modal com fundo branco, texto preto e sombra
    modal_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Bem-vindo ao Hashzap 👋", size=22, weight="bold", text_align="center", color=ft.colors.BLACK),
                campo_nome,
                botao_entrar
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20
        ),
        padding=30,
        border_radius=15,
        bgcolor=ft.colors.WHITE,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color=ft.colors.BLACK12,
            offset=ft.Offset(0, 4)
        ),
        visible=False
    )

    campo_mensagem = ft.TextField(label="Escreva sua mensagem", expand=True)
    botao_enviar = ft.ElevatedButton("Enviar", style=ft.ButtonStyle(bgcolor=ft.colors.BLUE))
    chat = ft.Column()
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
    
    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem, color=ft.colors.BLACK87)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        mensagem = f"{campo_nome.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()

    botao_enviar.on_click = enviar_mensagem

    def entrar_chat(evento):
        pagina.pubsub.send_all(f"{campo_nome.value} entrou no chat")
        modal_container.visible = False
        pagina.controls.clear()
        pagina.add(chat, linha_mensagem)
        pagina.update()

    botao_entrar.on_click = entrar_chat

    def abrir_modal(evento):
        modal_container.visible = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_modal, style=ft.ButtonStyle(bgcolor=ft.colors.BLUE))

    pagina.add(titulo, botao_iniciar, modal_container)

ft.app(target=main, view=ft.WEB_BROWSER)
