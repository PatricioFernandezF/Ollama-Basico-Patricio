
# Uso Básico de la API de Ollama con LLM

Este proyecto demuestra cómo utilizar la API de Ollama para interactuar con modelos de lenguaje grande (LLM), específicamente Llama3. El script proporciona una interfaz sencilla para generar respuestas basadas en una lista de prompts predefinidos y para simular una conversación en un chat de pedidos.

## Requisitos

Para ejecutar este código, necesitarás Python y la biblioteca Ollama. Puedes instalar Ollama mediante pip:

```bash
pip install ollama
```

## Estructura del Código

El código consta de varias funciones principales:

- `generar()`: Esta función itera sobre una lista de prompts predefinidos y utiliza el modelo Llama3 para generar respuestas. Cada prompt se procesa individualmente y se muestra su respuesta correspondiente.

- `chat()`: Simula una conversación en un chat de pedidos de pizza. Utiliza el modelo Llama3 para manejar mensajes de entrada y salida en tiempo real, mostrando la conversación continuamente.

- `main()`: Función principal que inicia la ejecución del programa, actualmente configurada para ejecutar sólo la función `generar()`.

## Cómo Ejecutar

1. Asegúrate de tener Python y Ollama instalados.
2. Guarda el script en un archivo, por ejemplo, `main.py`.
3. Ejecuta el script desde la línea de comandos:

```bash
python main.py
```

El script mostrará las respuestas generadas para cada uno de los prompts en la consola.

## Contribuciones

Si deseas contribuir a este proyecto, puedes hacerlo de la siguiente manera:
- Clona este repositorio.
- Realiza tus cambios y envía un pull request.

## Licencia

Este proyecto está bajo una licencia libre. Puedes utilizarlo y modificarlo libremente para tus propios proyectos.
