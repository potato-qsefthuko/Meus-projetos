from google import genai
import os

caminho_api = os.path.join(os.path.dirname(__file__), "api.txt")

with open(caminho_api, "r") as f:
    API_KEY = f.read().strip()
# Inicializa o cliente simples
client = genai.Client(api_key=API_KEY)

def gemini_search(query: str):
    try:
        # O modelo que FINALMENTE funcionou!
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=query
        )
        
        if response.text:
            return response.text
        return "O Gemini não retornou texto."

    except Exception as e:
        print(f"\n[ERRO]: {e}\n")
        return f"Erro ao consultar o Gemini: {e}"

if __name__ == "__main__":
    print("Testando o modelo que funcionou...")
    print(f"Resultado: {gemini_search('Oi, teste final!')}")