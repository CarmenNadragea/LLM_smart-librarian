"""
app.py
CLI pentru Smart Librarian – AI cu RAG + Tool
"""

import sys
from src.rag_chat import get_full_recommendation
import pyttsx3

def main():
    print("=== Smart Librarian ===")
    print("Scrie o întrebare (ex: Vreau o carte despre prietenie și magie)")
    # Listă simplă de cuvinte nepotrivite (poate fi extinsă)
    bad_words = ["prost", "idiot", "porc", "dracu", "naiba", "fmm", "fmm", "bou", "tampit", "fraier", "nesimtit"]
    tts_engine = pyttsx3.init()
    while True:
        query = input("\nÎntrebare (sau 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            print("La revedere!")
            break
        if any(bad_word in query.lower() for bad_word in bad_words):
            print("\n--- Mesaj ---")
            print("Te rog să folosești un limbaj respectuos. Întrebarea nu va fi procesată.")
            continue
        result = get_full_recommendation(query)
        print("\n--- Recomandare ---")
        print(result["short"])
        print("\n--- Rezumat complet ---")
        print(result["summary"])
        listen = input("\nVrei să asculți recomandarea și rezumatul? (y/n): ").strip().lower()
        if listen == "y":
            tts_engine.say(result["short"])
            tts_engine.say(result["summary"])
            tts_engine.runAndWait()

if __name__ == "__main__":
    main()
