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

    def recognize_audio(language):
        try:
            with sr.AudioFile(wav_path) as source:
                audio_data = recognizer.record(source)
                return recognizer.recognize_google(audio_data, language=language)
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print(f"Erro ao solicitar resultados da API do Google para o idioma {language}.")
            return None

    text = recognize_audio('pt-BR')
    if text is None:
        text = recognize_audio('en-US')

    if text:
        with open(text_path, 'w') as text_file:
            text_file.write(text)
        print("Transcrição concluída e salva em:", text_path)
    else:
        print("Não consegui entender o áudio em nenhum dos idiomas.")
    
    if os.path.exists(wav_path):
        os.remove(wav_path)
