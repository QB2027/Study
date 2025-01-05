from utils.scanner import scan_directory
from utils.json_utils import save_to_json
import os

def main():
    """
    主函数，负责调用模块化功能完成任务。
    """
    # 仓库根目录
    repo_root = os.path.abspath(os.path.dirname(__file__))

    # 输出文件路径
    output_file = os.path.join(repo_root, "files.json")

    # 扫描目录结构
    print("Scanning repository directory structure...")
    data = scan_directory(repo_root)

    # 保存文件树为 JSON
    print(f"Saving JSON file to {output_file}...")
    save_to_json(data, output_file)

if __name__ == "__main__":
    main()
