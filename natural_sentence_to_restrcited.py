import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def transform_sentence_with_chatgpt(sentence: str) -> str:
    """
    Toma una oración y la transforma al formato lógico utilizando la API de OpenAI.

    Args:
        sentence (str): La oración original a transformar.

    Returns:
        str: La transformación en formato lógico.
    """
    prompt_template = (
        "Transforma la siguiente oración a formato lógico como este ejemplo:\n"
        "Si la entrada es: \"If desire is the root of all suffering, and suffering is the root of all greatness, then desire is the root of all greatness\"\n"
        "Transforma a: \"If (desire_is_the_root_of_all_suffering and suffering_is_the_root_of_all_greatness) then desire_is_the_root_of_all_greatness\"\n"
        "Oración original: \"{sentence}\"\n"
        "Devuelve la transformación lógica asegurándote de mantener el significado original."
    )

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

# Ejemplo de uso
input_sentence = "If desire is the root of all suffering, and suffering is the root of all greatness, then desire is the root of all greatness"
transformed_sentence = transform_sentence_with_chatgpt(input_sentence)

if transformed_sentence:
    print("\nTransformación lógica:")
    print(transformed_sentence)
else:
    print("No se generó la transformación.")
