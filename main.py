
#pip install ollama
import ollama

def generar():
    prompts = [
        "Explica el teorema de Pitágoras",
        "Describe un atardecer en la playa",
        "¿Cuáles son los beneficios de la meditación?",
    ]

    for prompt in prompts:
        print("Prompt:", prompt)
        result = ollama.generate(model='llama3', prompt=prompt,system="Eres un robot, debes empezar cada mensaje con beep beep.")
        print("Respuesta:", result["response"])
        print("-" * 50)

def chat():
    stream = ollama.chat(
    model='llama3',
    messages=[
        {"role": "system", "content": "Bienvenido al sistema de pedidos de pizza."},
        {"role": "user", "content": "Hola, me gustaría hacer un pedido para entrega a domicilio."},
        ],
    stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def main():
    #print(ollama.show('llama3'))
    generar()
    #chat()

if __name__ == "__main__":
    main()
