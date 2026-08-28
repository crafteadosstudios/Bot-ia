```markdown
# 🤖 M.I.P.E.C.O.P.

> **Mi IA Personal Experimental Con Personalidad**  
> *Un asistente conversacional local, sarcástico y técnico impulsado por Llama 3.2.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Llama_3.2-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
[![Linux](https://img.shields.io/badge/Fedora_Linux-FCC624?style=for-the-badge&logo=fedora&logoColor=black)](https://getfedora.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

---

## 📌 Descripción

**M.I.P.E.C.O.P.** es un bot de inteligencia artificial diseñado para ejecutarse **100% de manera local** utilizando el motor de **Ollama** y el modelo **Llama 3.2**. A diferencia de los asistentes comerciales estandarizados, M.I.P.E.C.O.P. implementa un motor de personalidad directa, sarcástica y con un tono técnico enfocado en Linux y hardware, eliminando muletillas corporativas y respuestas genéricas de soporte técnico.

El sistema utiliza persistencia de memoria mediante lectura y escritura en archivos JSON locales, permitiendo que la IA recuerde el contexto, especificaciones y proyectos del usuario entre sesiones.

---

## ✨ Características Principales

* 🔒 **Privacidad Total (100% Local):** No requiere conexión a APIs externas ni suscripciones en la nube.
* 🧠 **Memoria Persistente JSON:** Lee y actualiza la información del usuario desde `conocimiento.json`.
* ⚡ **Arquitectura Ligera:** Optimizado para correr con consumo mínimo de recursos en entornos de escritorio Linux.
* 🛠️ **Comandos Integrados en CLI:** Gestión de estado directamente en la sesión interactiva (`memoria`, `limpiar`, `salir`).
* 🎯 **Prompt de Sistema Estricto:** Configuración rígida para mantener coherencia en el tono, ironía técnica y brevedad de respuestas.

---

## 🛠️ Requisitos del Sistema

* **Sistema Operativo:** Linux (Probado y optimizado en Fedora Linux) / macOS / Windows.
* **Lenguaje:** Python 3.10 o superior.
* **Motor de IA:** [Ollama](https://ollama.com/) instalado y activo.
* **Modelo:** `llama3.2` descargado en Ollama.

---

## 🚀 Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone [https://github.com/crafteadosstudios/Bot-ia.git](https://github.com/crafteadosstudios/Bot-ia.git)
cd Bot-ia

```

### 2. Configurar el Entorno de Python

Instala la librería oficial de Ollama para Python:

```bash
pip install ollama

```

### 3. Preparar el Motor Ollama

Asegúrate de que el servicio de Ollama esté en ejecución y descarga el modelo requerido:

```bash
ollama serve
ollama pull llama3.2

```

---

## 💻 Módulos y Uso

Ejecuta el asistente desde tu terminal o desde el entorno integrado de VS Code:

```bash
python3 bot.py

```

### ⌨️ Comandos Interactivos de Consola

| Comando | Descripción |
| --- | --- |
| `memoria` | Despliega en pantalla el estado actual del archivo `conocimiento.json`. |
| `limpiar` | Reinicia el historial activo de la conversación manteniendo el *system prompt*. |
| `salir` | Cierra la sesión de la IA y finaliza la ejecución del script. |

---

## 📁 Estructura del Proyecto

```text
Bot-ia/
├── bot.py              # Script principal: CLI, gestión de Ollama y lógica de estado
├── conocimiento.json   # Base de conocimiento persistente y contexto del usuario
└── README.md           # Documentación oficial del proyecto

```

---

## 📝 Ejemplo de Estructura `conocimiento.json`

```json
{
    "usuario": "Santi",
    "sistema_operativo": "Fedora Linux",
    "proyectos": ["Bot-ia", "Servidores Locales"],
    "preferencias": "Respuestas técnicas, directas y sin rodeos"
}

```

---

## 🤝 Contribuciones y Desarrollo

Las contribuciones, reportes de errores y sugerencias son bienvenidas. Si deseas agregar nuevas funcionalidades a la gestión de memoria o modificar los parámetros del *system prompt*, puedes abrir un *Issue* o enviar un *Pull Request*.

---

## 👤 Autor

Desarrollado por **[Crafteados Studios](https://www.google.com/search?q=https://github.com/crafteadosstudios)**.

```

Para actualizar la documentación en GitHub, ejecuta lo siguiente en tu terminal dentro de la carpeta del proyecto:

```bash
git add README.md
git commit -m "docs: add complete and professional README"
git push

```
