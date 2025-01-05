import os

# 需要跳过的目录或文件
EXCLUDE_DIRS = {'.git', '.github'}
EXCLUDE_FILES = {'README.md', 'LICENSE', 'git_sync.bat', 'git_sync.sh'}

def scan_directory(base_path, current_path=""):
    """
    递归扫描 base_path 下的文件和目录，返回树状结构的列表。
    :param base_path: 要扫描的实际操作系统路径
    :param current_path: 从仓库根目录开始的相对路径，用于前端显示或下载
    :return: 一个列表，每个元素是 {name, type, path, children?}
    """
    entries = []
    try:
        for entry in os.scandir(base_path):
            if entry.is_dir():
                if entry.name in EXCLUDE_DIRS:
                    continue
                entries.append({
                    "name": entry.name,
                    "type": "directory",
                    "path": os.path.join(current_path, entry.name).replace("\\", "/"),
                    "children": scan_directory(
                        os.path.join(base_path, entry.name),
                        os.path.join(current_path, entry.name)
                    )
                })
            else:
                if entry.name in EXCLUDE_FILES:
                    continue
                entries.append({
                    "name": entry.name,
                    "type": "file",
                    "path": os.path.join(current_path, entry.name).replace("\\", "/")
                })
    except PermissionError as e:
        print(f"PermissionError: Unable to access {base_path} - {e}")
    except Exception as e:
        print(f"Error scanning {base_path}: {e}")
    return entries
