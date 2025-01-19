# Chatzinho - Documentação

### Descrição

Este projeto implementa uma aplicação de chat simples utilizando a biblioteca Flet. O usuário pode iniciar o chat, digitar seu nome, enviar mensagens e visualizar mensagens enviadas por outros participantes em tempo real.

---

## Funcionalidades

1. **Tela Inicial**:
   - **Título**: "Chatzinho".
   - **Botão**: "Iniciar chat".
     - Ao clicar, abre um popup/modal com as seguintes opções:
       - **Título**: "Bem vindo ao Chatzinho".
       - **Caixa de texto**: Campo para o usuário digitar seu nome.
       - **Botão**: "Entrar no chat".

2. **Entrada no Chat**:
   - Remove o título e o botão "Iniciar chat".
   - Adiciona:
     - Área de mensagens (chat).
     - Campo para digitar mensagens.
     - Botão para enviar mensagens.
   - Exibe mensagem no chat informando que o usuário entrou no chat.

3. **Envio de Mensagens**:
   - O usuário pode enviar mensagens, que aparecem na área do chat.
   - Após o envio, o campo de texto é limpo automaticamente.

---

## Código

```python
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

    # criando o túnel de comunicação
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
    titulo_popup = ft.Text("Bem vindo ao Chatzinho")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(
        title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    # botao de iniciar chat
    def entrar_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_popup)

    # colocar elementos na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER)
```

---

## Como Executar o Projeto

1. **Instale a biblioteca Flet**:
   ```bash
   pip install flet
   ```

2. **Salve o código acima em um arquivo Python (e.g., `chatzinho.py`).**

3. **Execute o arquivo:**
   ```bash
   python chatzinho.py
   ```

4. **Interaja com o chat:**
   - Acesse a aplicação no navegador.
   - Clique em "Iniciar chat".
   - Digite seu nome no popup e entre no chat.
   - Envie mensagens e veja o fluxo de comunicação.

---

## Estrutura do Código

1. **Função `main`**:
   - Configura e organiza os elementos visuais e as interações da aplicação.

2. **Componentes Principais**:
   - `Text`: Exibe textos na interface.
   - `ElevatedButton`: Botões para interações.
   - `TextField`: Campo de entrada de texto.
   - `AlertDialog`: Popup para inserção do nome.

3. **Fluxo de Mensagens**:
   - As mensagens são transmitidas usando `pagina.pubsub`, garantindo comunicação em tempo real entre usuários conectados.

---

## Melhorias Futuras

- Implementar autenticação de usuários.
- Adicionar timestamps às mensagens.
- Melhorar o design da interface com estilos personalizados.
- Suporte a diferentes salas de chat.

---

Explore, modifique e divirta-se com o Chatzinho!

