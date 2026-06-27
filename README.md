# 💬 Bimbam Buy AI Agent (RAG System)

Asistente inteligente basado en IA que responde preguntas utilizando documentos internos de la empresa Bimbam Buy.

Este proyecto implementa un sistema RAG (Retrieval-Augmented Generation) combinando búsqueda semántica con un modelo LLM local.

---

## 📸 Demo

![Demo](screenshot.png)

---

## 🚀 Características

- Consulta documentos PDF empresariales
- Respuestas basadas en información real
- Soporte multilenguaje (español, inglés, portugués)
- Interfaz web tipo chat
- Uso de modelo local (Ollama, sin costos de API)
- Arquitectura RAG completa

---

## 📚 Documentos utilizados

Ubicados en la carpeta `data/`:

- Política de Reembolsos y Devoluciones
- Programa de Afiliados
- Guía de Envíos
- Métodos de Pago
- Manual de Garantía

---

## 🧠 Arquitectura

Flujo del sistema:

PDF → carga → fragmentación → embeddings → FAISS → retrieval → LLM → respuesta

Tecnologías utilizadas:

- Python
- FastAPI
- LangChain
- FAISS
- Ollama (llama3 + embeddings)
- HTML + JavaScript

---

## ⚙️ Instalación

### 1. Clonar repositorio

git clone https://github.com/danielc149/bimbam-buy-ai-agent.git
cd bimbam-buy-ai-agent

### 2. Crear entorno virtual

python -m venv venv

Activar:

source venv/Scripts/activate

### 3. Instalar dependencias

pip install -r requirements.txt

### 4. Instalar Ollama

https://ollama.com

### 5. Descargar modelos

ollama pull llama3
ollama pull nomic-embed-text

### 6. Ejecutar aplicación

python -m uvicorn app:app --reload

### 7. Abrir en navegador

http://127.0.0.1:8000/chat

---

## 💬 Uso

Ejemplos de preguntas:

- ¿Qué hacer si un pago fue rechazado?
- ¿Qué cubre la garantía?
- How many days does a refund take?
- ¿Cómo funciona el programa de afiliados?

---

## ⚠️ Limitaciones

- Algunos documentos no contienen respuestas explícitas
- El sistema puede entregar respuestas interpretativas cuando la información es parcial
- El modelo local puede mostrar variaciones en el idioma de salida
- La precisión depende del wording de la pregunta (limitación natural de RAG)

---

## 🧠 Consideraciones reales

- El sistema es sensible a cómo se formula la pregunta
- Algunos documentos contienen información implícita
- El modelo puede inferir respuestas

---

## ✅ Mejoras implementadas

- Ajuste de fragmentación (chunk_size)
- Uso de MMR en retrieval
- Respuestas interpretativas
- UI sin recarga
- Feedback visual en botón

---

## 🎨 Interfaz

- Input persistente
- Respuestas dinámicas
- Historial local

---

## 🔒 Consideraciones técnicas

- Sin base de datos
- Sin almacenamiento de sesiones
- Optimizado para bajo consumo
- Sin APIs externas

---

## 🏁 Estado del proyecto

Proyecto funcional que demuestra implementación de RAG y manejo de limitaciones reales.

---

## 👨‍💻 Autor

Daniel Cañete
