import pyttsx3
def text_to_audio(text,output_files="output.mp3"):
  if text:
    engine=pyttsx3.init()
    engine=save_to_file(text,output_files)
    engine.runAndWait()
    print("audio saved as (output_file)")
  else:
    print("error:no text provided for conversion")
text_output="hello welcome to hyderabad"
text_to_audio(text_audio,"converted_audio.mp3")

    
