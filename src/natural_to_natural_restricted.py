import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_natural_to_natural_restricted(sentence: str) -> str:
    prompt_template = get_text_from_file("prompt_template.txt")
    # print(prompt_template)

    # Crear el prompt para el modelo
    prompt = prompt_template.format(sentence=sentence)

    try:
        # Llamada a la API de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en transformar oraciones lógicas."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Extraer la respuesta generada por el modelo
        generated_text = response['choices'][0]['message']['content']

        return generated_text.strip()

    except Exception as e:
        print(f"Error inesperado: {e}")
        return ""

# input_sentence = "If desire is the root of all suffering, and suffering is the root of all greatness, then desire is the root of all greatness"
# transformed_sentence = get_natural_to_natural_restricted(input_sentence)

# if transformed_sentence:
#     print("\nTransformación lógica:")
#     print(transformed_sentence)
# else:
#     print("No se generó la transformación.")
