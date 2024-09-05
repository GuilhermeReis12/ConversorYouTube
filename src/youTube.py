from download_audio import download_audio
from process_audio import process_audio
import speech_recognition as sr
from pydub import AudioSegment
import os

def transcribe_audio(audio_path, text_path):
    if not os.path.exists(audio_path):
        print(f"Erro: O arquivo {audio_path} não foi encontrado.")
        return

    recognizer = sr.Recognizer()
    
    wav_path = audio_path.replace('.mp3', '.wav')
    try:
        audio = AudioSegment.from_mp3(audio_path)
        audio.export(wav_path, format='wav')
    except Exception as e:
        print(f"Erro ao converter o arquivo MP3 para WAV: {e}")
        return

    try:
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            with open(text_path, 'w') as text_file:
                text_file.write(text)
            print("Transcrição concluída e salva em:", text_path)
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
    except sr.RequestError:
        print("Erro ao solicitar resultados da API do Google.")
    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path) 

def main():
    youtube_url = input("Digite a URL do vídeo do YouTube: ")
    audio_filename = input("Digite o nome do arquivo de áudio (sem a extensão .mp3): ")
    
    audio_path = f"audio/{audio_filename}.mp3"
    fixed_audio_path = f"audio/{audio_filename}_fixed.mp3"
    text_path = f"text/{audio_filename}.txt"

    os.makedirs('audio', exist_ok=True)
    os.makedirs('text', exist_ok=True)

    download_audio(youtube_url, audio_path)
    process_audio(audio_path, fixed_audio_path)
    
    if os.path.exists(fixed_audio_path):
        transcribe_audio(fixed_audio_path, text_path)
    else:
        print(f"Erro: O arquivo processado {fixed_audio_path} não foi encontrado.")

if __name__ == "__main__":
    main()
