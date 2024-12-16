from utils import load_knowledge_base, ask_question

def main():
    knowledge_base = load_knowledge_base()
    print(f"Добро пожаловать в игру 'Угадай предмет'! Тема: {knowledge_base['type']}.")
    print("Режим поиска ответа.\n")
    ask_question(knowledge_base["questions"])
    
if __name__ == "__main__":
    main()