\# 💬 Bimbam Buy AI Agent (RAG System)



Asistente inteligente basado en IA que responde preguntas utilizando documentos internos de la empresa Bimbam Buy.



Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation), combinando búsqueda semántica con un modelo LLM local.



\---



\## 🚀 Características



\- Consulta documentos PDF empresariales

\- Respuestas basadas en información real

\- Soporte multilenguaje (español, inglés, portugués)

\- Interfaz web simple tipo chat

\- Uso de modelo local (Ollama, sin costo de API)

\- Arquitectura RAG real (embedding + retrieval + generación)



\---



\## 📚 Documentos utilizados



Ubicados en la carpeta `data/`:



\- Política de Reembolsos y Devoluciones

\- Programa de Afiliados

\- Guía de Envíos

\- Métodos de Pago

\- Manual de Garantía



\---



\## 🧠 Arquitectura



Flujo del sistema:



PDF → carga → fragmentación → embeddings → FAISS → consulta → respuesta IA



Tecnologías:



\- Python

\- FastAPI

\- LangChain

\- FAISS

\- Ollama (llama3 + embeddings)

\- HTML + JavaScript



\---



\## ⚙️ Instalación



\### 1. Clonar repositorio



```bash

git clone https://github.com/danielc149/bimbam-buy-ai-agent.git

cd bimbam-buy-ai-agent



2\. Crear entorno virtual

python -m venv venv

Activar:

source venv/Scripts/activate



3\. Instalar dependencias

pip install -r requirements.txt



4\. Instalar Ollama

Descargar desde:

https://ollama.com



5\. Descargar modelos

ollama pull llama3

ollama pull nomic-embed-text



6\. Ejecutar la aplicación

python -m uvicorn app:app --reload



7\. Abrir en navegador

http://127.0.0.1:8000/chat



💬 Uso

Ejemplos de preguntas:



¿Qué hacer si un pago fue rechazado?

¿Qué cubre la garantía?

How many days does a refund take?

¿Cómo funciona el programa de afiliados?





⚠️ Limitaciones



Algunos PDFs pueden no contener respuestas explícitas

El sistema puede responder de forma interpretativa cuando la información es parcial

El idioma puede variar en algunos casos debido a limitaciones del modelo local

La precisión depende de cómo se formule la pregunta (RAG es sensible al wording)





✅ Mejoras implementadas



Aumento de fragmentos (chunk\_size)

Retriever con MMR

Respuestas interpretativas

Limpieza de texto para usuario final

Interfaz sin recarga con feedback visual





🎨 Interfaz



Input persistente

Respuestas dinámicas sin recargar

Historial local en navegador

Botón con estado "Enviando..."





🔒 Consideraciones técnicas



No hay base de datos

No hay almacenamiento de historial en backend

Optimizado para bajo consumo (OCI 1GB RAM)

Sin uso de APIs externas





🚫 Decisiones de diseño



No uso de OpenAI (costos)

No uso de Streamlit (consumo alto)

Uso de Ollama local

Backend simple con FastAPI





🏁 Estado del proyecto

Proyecto funcional que demuestra:



Implementación de RAG

Integración backend + frontend

Manejo de limitaciones reales de IA

Experiencia de usuario básica





👨‍💻 Autor 

Daniel Cañete

Proyecto desarrollado como parte de un challenge técnico en IA aplicada.





