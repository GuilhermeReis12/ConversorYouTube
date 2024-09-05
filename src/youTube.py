from download_audio import download_audio
from process_audio import process_audio

def main():
    youtube_url = input("Digite a URL do vídeo do YouTube: ")
    
    audio_filename = input("Digite o nome do arquivo de áudio (sem a extensão .mp3): ")
    
    audio_path = f"audio/{audio_filename}.mp3"
    fixed_audio_path = f"audio/{audio_filename}_fixed.mp3"

    download_audio(youtube_url, audio_path)

    # Processar e converter o áudio se necessário
    process_audio(audio_path, fixed_audio_path)

if __name__ == "__main__":
    main()
