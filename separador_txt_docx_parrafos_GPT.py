import openai
import docx2txt
import os
# Configurar la clave de API de OpenAI
openai_api_key = os.environ['OPENAI_API_KEY']

# Pedir al usuario el nombre del archivo
nombre_archivo = input("Introduce el nombre del archivo (incluyendo la extensión): ")

# Leer el contenido del archivo
if nombre_archivo.endswith(".txt"):
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
elif nombre_archivo.endswith(".docx"):
    contenido = docx2txt.process(nombre_archivo)
else:
    print("Lo siento, el formato de archivo no es compatible.")
    exit()

# Solicitar a OpenAI que separe el contenido en párrafos de ideas principales
respuesta = openai.Completion.create(
    engine="davinci",
    prompt=f"Separa el siguiente texto en párrafos de ideas principales:\n{contenido}",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

# Mostrar la respuesta de OpenAI
print(respuesta.choices[0].text)
