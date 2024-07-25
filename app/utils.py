import json


def dict_list_to_json(dict_list, filename):
    try:
        json_srt = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_srt)
        return json_srt
    except (ValueError, TypeError, IOError) as e:
        print(
            f"Ошибка при преобразовании списка словарей в JSON или записи в файл: {e}"
        )
        return None


def json_to_dict_list(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            json_str = file.read()
        dict_list = json.loads(json_str)
        return dict_list
    except (ValueError, TypeError, IOError) as e:
        print(f"Ошибка при преобразовании JSON в список словарей: {e}")
        return None
