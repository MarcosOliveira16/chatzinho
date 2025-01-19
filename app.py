# Tela inical
# Titulo: Chatzinho
# Botao: Iniciar chat
# quando clicar no botão:
# abrir um popup/modal/alerta
# Titulo: Bem vindo ao Chatzinho
# Caixa de texto: Digite seu nome
# Botao: Entrar no chat
# quando clicar no botao:
# sumir com o titulo
# sumir com o botão de inicar chat
# carregar o chat
# carregar o campo de mensagem
# carregar o botao de enviar mensagem
# quando clicar no botão:
# enviar a mensagem
# limpar o campo de mensagem

# flet

# importar o flet
import flet as ft

# criar uma função principal para rodar o seu app


def main(pagina):
    # titulo da pagina
    titulo = ft.Text("Chatzinho")

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)

        pagina.update()

    # crianddo o tunel de communicacao
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        # limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()

    campo_enviar_mensagem = ft.TextField(
        label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton(
        "Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row(
        [campo_enviar_mensagem, botao_enviar_mensagem]
    )

    chat = ft.Column()

    def entrar_chat(evento):
        # fechar o popup
        popup.open = False
        # remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(titulo)
        # adicionar o chat
        pagina.add(chat)
        # criar o campo de mensagem do usuario
        # criar o botao de enviar mensagem do usuario
        pagina.add(linha_enviar)

        # add no chat 'fulano entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    # criar o popup
    titulo_poup = ft.Text("Bem vindo ao Chatzinho")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(
        title=titulo_poup, content=caixa_nome, actions=[botao_popup])

    # botao de iniciar chat
    def entrar_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()  # sempre q editar algo na tela, usa o 'pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_popup)

    # colocar elementos na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)


# executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER)
