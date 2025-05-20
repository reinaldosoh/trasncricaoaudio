# Sistema de Transcrição de Áudio em Tempo Real

## Sobre o Projeto

Este projeto é um sistema de transcrição de áudio em tempo real que permite capturar fala através do microfone e convertê-la para texto. O sistema possui duas versões:

1. **Versão de linha de comando**: Utiliza bibliotecas Python para reconhecimento de voz
2. **Versão web**: Interface web interativa que utiliza a Web Speech API para transcrição em tempo real

## Funcionalidades

- Transcrição de áudio para texto em português do Brasil
- Interface web responsiva e moderna
- Visualização do texto sendo transcrito em tempo real
- Edição do texto transcrito
- Salvamento da transcrição como arquivo de texto

## Tecnologias Utilizadas

### Backend
- Python 3
- Flask (framework web)
- SpeechRecognition (biblioteca de reconhecimento de voz)
- PyAudio (para captura de áudio)

### Frontend
- HTML5
- CSS3
- JavaScript
- Web Speech API

## Como Instalar

### Requisitos
- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)
- Navegador moderno (preferencialmente Google Chrome)

### Instalação de Dependências

```bash
# Instalar dependências Python
pip install flask flask-cors SpeechRecognition pyaudio gtts playsound
```

## Como Usar

### Versão Web

1. Inicie o servidor Flask:
   ```bash
   python app.py
   ```

2. Acesse a aplicação no navegador:
   ```
   http://127.0.0.1:5000
   ```

3. Clique em "Iniciar Transcrição" e comece a falar
4. O texto será transcrito em tempo real na área de transcrição
5. Quando terminar, clique em "Parar"
6. Você pode editar o texto diretamente na caixa de transcrição
7. Para salvar, clique no botão "Salvar"

### Versão de Linha de Comando

```bash
python transcrever_audio.py
```

## Estrutura do Projeto

- `app.py`: Servidor Flask para a versão web
- `templates/index.html`: Interface HTML da aplicação web
- `static/css/style.css`: Estilos da interface web
- `static/js/script.js`: Lógica JavaScript para transcrição em tempo real
- `transcrever_audio.py`: Script para transcrição via linha de comando
- `falaParaTexto.py`: Módulo para reconhecimento de voz
- `textoParaFala.py`: Módulo para síntese de voz (não utilizado na versão atual)

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT.

## Agradecimentos

Este projeto é uma evolução do [Virtual Assistant](https://github.com/matheusjohannaraujo/virtual_assistant) original criado por Matheus Johann Araújo.
