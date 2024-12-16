import json

file_path = "knowledge_base.json"

def load_knowledge_base():
    """Загрузка базы знаний из файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Возвращаем пустую базу знаний, если файл не найден
        return {"type": "Бытовая техника", "questions": {}}

def save_knowledge_base(knowledge_base):
    """Сохранение базы знаний в файл."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(knowledge_base, f, ensure_ascii=False, indent=4)

def ask_question(node):
    """Рекурсивный поиск ответа в базе знаний."""
    if isinstance(node, str):  # Если это конечный узел
        print(f"Это {node}! (Да/Нет)")
        answer = input().strip().lower()
        if answer == "да":
            print("Отлично!")
            return node
        else:
            print("Сдаюсь")
            newNode = train_knowledge_base(node)
            save_knowledge_base()
    else:  # Если это вопрос
        print(f"{node['question']} (Да/Нет)")
        answer = input().strip().lower()
        if answer in node:
            return ask_question(node[answer])
        else:
            print("Ответ должен быть 'да' или 'нет'")
            return None

def train_knowledge_base(node):
    """Обучение базы знаний."""
    print("Сдаюсь. Подскажите правильный ответ.")
    correct_answer = input().strip()
    print(f"Сформулируйте вопрос, ответ на который поможет отличить '{correct_answer}' от '{node}'.")
    new_question = input().strip()
    print(f"Подскажите вариант правильного ответа для '{correct_answer}': да или нет.")
    answer_for_new_item = input().strip().lower()
    print(node)

    return {
        "question": new_question,
        "да" if answer_for_new_item == "да" else "нет": correct_answer,
        "нет" if answer_for_new_item == "да" else "да": node
    }
    '''else:  # Если это вопрос
        print(f"{node['question']} (Да/Нет)")
        answer = input().strip().lower()
        if answer in node:
            node[answer] = train_knowledge_base(node[answer])
        else:
            print("Ответ не распознан. Попробуйте снова.")
        return node
'''
def print_knowledge_base(node, indent=0):
    """Рекурсивный вывод базы знаний в формате дерева."""
    if isinstance(node, str):
        print(" " * indent + f"→ {node}")
    else:
        print(" " * indent + f"{node['question']}")
        for key in ["да", "нет"]:
            if key in node:
                print(" " * (indent + 4) + f"{key.capitalize()}:")
                print_knowledge_base(node[key], indent + 8)