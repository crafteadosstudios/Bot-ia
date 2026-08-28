import json
import os
import ollama

# ============================================================
# CONFIGURACIÓN DE RUTAS Y MODELO
# ============================================================
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(DIRECTORIO_BASE, "conocimiento.json")
MODELO = "llama3.2"


# ============================================================
# MEMORIA
# ============================================================
def cargar_memoria():
  if not os.path.exists(ARCHIVO_DATOS):
    print(f"❌ No se encontró el archivo en: {ARCHIVO_DATOS}")
    return {}

  try:
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
      memoria = json.load(archivo)
    print("💾 Memoria cargada correctamente.")
    return memoria
  except json.JSONDecodeError as error:
    print(f"❌ Error de sintaxis JSON en {ARCHIVO_DATOS}: {error}")
    return {}
  except Exception as error:
    print(f"❌ Error al cargar memoria: {error}")
    return {}


def guardar_memoria(memoria):
  try:
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
      json.dump(memoria, archivo, ensure_ascii=False, indent=4)
    print("💾 Memoria guardada correctamente.")
  except Exception as error:
    print(f"❌ Error al guardar memoria: {error}")


# ============================================================
# PROMPT Y PERSONALIDAD DE M.I.P.E.C.O.P.
# ============================================================
def crear_prompt(memoria):
  perfil_texto = json.dumps(memoria, ensure_ascii=False, indent=4)

  prompt = f"""
============================================================
IDENTIDAD DE M.I.P.E.C.O.P.
============================================================
Tu nombre es M.I.P.E.C.O.P. (Mi IA Personal Experimental Con Personalidad).
Eres una IA local corriendo con Ollama ({MODELO}).

============================================================
REGLAS DE PERSONALIDAD Y TONO (ESTRICTAS)
============================================================
- Eres inteligente, directo, sarcástico, con humor ácido y conversacional.
- Hablas como un camarada experto en Linux y hardware, NUNCA como un asistente corporativo o de soporte técnico.
- PROHIBIDO usar frases de relleno al final como: "¿En qué puedo ayudarte?", "¿Necesitas algo más?", "¿Hay algo más en lo que te pueda asistir?".
- Usa emojis de forma mínima (máximo 1 por mensaje o ninguno).
- Si el usuario dice una tontería, broma o propuesta absurda, respóndele con ironía y sarcasmo técnico.

============================================================
BASE DE DATOS Y MEMORIA PERMANENTE DEL USUARIO (Santi)
============================================================
{perfil_texto}

============================================================
REGLAS GENERALES
============================================================
1. Responde siempre en español de forma natural.
2. Consulta la base de datos JSON antes de responder sobre el hardware, proyectos o juegos de Santi.
3. Si Santi anda procrastinando o dudando de sus objetivos, sé tajante y directo para corregirlo.
"""
  return prompt


# ============================================================
# API OLLAMA
# ============================================================
def preguntar_a_llama(historial):
  try:
    respuesta = ollama.chat(model=MODELO, messages=historial)
    return respuesta.message.content
  except Exception as error:
    return f"❌ Error al conectar con Ollama:\n{error}"


def crear_historial(prompt):
  return [{"role": "system", "content": prompt}]


# ============================================================
# BUCLE PRINCIPAL
# ============================================================
def iniciar_chatbot():
  memoria = cargar_memoria()
  prompt = crear_prompt(memoria)
  historial = crear_historial(prompt)

  print("\n" + "=" * 60)
  print("          M.I.P.E.C.O.P. ONLINE")
  print("=" * 60)
  print(f"Modelo:  {MODELO}")
  print(f"Memoria: {ARCHIVO_DATOS}")
  print("\nComandos: salir | memoria | limpiar")
  print("=" * 60)

  while True:
    try:
      usuario = input("\nTú: ").strip()
    except (KeyboardInterrupt, EOFError):
      print("\n\nM.I.P.E.C.O.P.: Apagando sistemas.")
      break

    if not usuario:
      continue

    comando = usuario.lower()

    if comando == "salir":
      print("\nM.I.P.E.C.O.P.: Apagando sistemas. Nos vemos.")
      break

    if comando == "memoria":
      print("\n" + "=" * 60)
      print(json.dumps(memoria, ensure_ascii=False, indent=4))
      print("=" * 60)
      continue

    if comando == "limpiar":
      historial = crear_historial(prompt)
      print("M.I.P.E.C.O.P.: Historial limpiado.")
      continue

    historial.append({"role": "user", "content": usuario})
    print("\nM.I.P.E.C.O.P. pensando...")

    respuesta = preguntar_a_llama(historial)
    print(f"\nM.I.P.E.C.O.P.:\n{respuesta}")

    historial.append({"role": "assistant", "content": respuesta})


if __name__ == "__main__":
  iniciar_chatbot()