# Conversor YouTube

O Conversor YouTube é uma aplicação que permite baixar áudio de vídeos do YouTube e transcrevê-lo para texto. A aplicação utiliza `yt-dlp` para o download de áudio, `ffmpeg` para processamento de áudio e `SpeechRecognition` para transcrição.

## Funcionalidades

- Baixar áudio de vídeos do YouTube.
- Processar e converter o áudio para o formato MP3, se necessário.
- Transcrever o áudio para texto em inglês ou português.
- Salvar o texto transcrito em arquivos `.txt`.

## Requisitos

- Python 3.7 ou superior
- `yt-dlp`
- `ffmpeg`
- `pydub`
- `speech_recognition`
- `pytesseract` (para reconhecimento óptico de caracteres, se necessário)

## Instalação

1. Clone este repositório:

   ```
   git clone https://github.com/GuilhermeReis12/ConversorYouTube



Navegue até o diretório do projeto:

cd ConversorYouTube
Crie e ative um ambiente virtual (opcional, mas recomendado):


python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
Instale as dependências:

pip install -r requirements.txt
Se você não tem um arquivo requirements.txt, você pode instalar manualmente:



pip install yt-dlp pydub SpeechRecognition
Instale o ffmpeg:

No macOS, você pode usar Homebrew:


brew install ffmpeg
No Windows, baixe o instalador do site oficial do FFmpeg e siga as instruções de instalação.

Uso
Execute o script principal:



python src/youTube.py
Digite a URL do vídeo do YouTube e o nome do arquivo de áudio (sem a extensão .mp3) quando solicitado.

O áudio será baixado e processado. O texto transcrito será salvo no diretório text/.



Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Nome: Guilherme Reis
Email: seu-email@exemplo.com
GitHub: seuusuario


### Explicações:

- **Descrição do Projeto**: Explica o que o projeto faz.
- **Funcionalidades**: Lista as principais funcionalidades.
- **Requisitos**: Ferramentas e bibliotecas necessárias.
- **Instalação**: Passos para configurar o ambiente e instalar dependências.
- **Uso**: Instruções sobre como executar o projeto.
- **Estrutura do Projeto**: Descreve a estrutura do projeto.
- **Contribuições**: Orientações para quem deseja contribuir.
- **Licença**: Tipo de licença do projeto.
- **Contato**: Informações de contato para dúvidas ou sugestões.

Certifique-se de substituir os valores de exemplo, como URLs e e-mails, pelos detalhes reais do seu projeto e informações de contato.


