import json

def save_to_json(data, output_file):
    """
    保存数据到 JSON 文件。
    :param data: 要保存的数据
    :param output_file: 输出 JSON 文件路径
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"JSON file successfully generated at: {output_file}")
    except Exception as e:
        print(f"Error writing to JSON file: {e}")
