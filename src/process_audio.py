import subprocess
import os

def convert_audio(input_file: str, output_file: str):
 
    try:
        subprocess.run([
            'ffmpeg', '-i', input_file,
            '-acodec', 'libmp3lame',
            '-ab', '192k',
            output_file
        ], check=True)
        print(f"Áudio convertido com sucesso para {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao converter o áudio: {e}")

def process_audio(input_path: str, output_path: str):
    
    if input_path.endswith('.mp3.mp3'):
        input_path = input_path[:-4]
    
    if not is_valid_mp3(input_path):
        print("O arquivo MP3 não é válido, convertendo...")
        convert_audio(input_path, output_path)
    else:
        print("O arquivo MP3 já está no formato correto. Copiando...")
        try:
            os.rename(input_path, output_path)  
            print(f"Arquivo copiado para {output_path}.")
        except OSError as e:
            print(f"Erro ao copiar o arquivo: {e}")

def is_valid_mp3(file_path: str) -> bool:
  
    return file_path.endswith('.mp3') and os.path.exists(file_path) and os.path.getsize(file_path) > 0
