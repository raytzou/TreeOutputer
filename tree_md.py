import os

def tree(path, prefix='', level=2, output_lines=None):
    if level < 0 or not os.path.isdir(path):
        return

    entries = [e for e in os.listdir(path) if not e.startswith('.')]
    entries.sort(key=lambda e: (not os.path.isdir(os.path.join(path, e)), e.lower()))

    for index, name in enumerate(entries):
        full_path = os.path.join(path, name)
        connector = '└── ' if index == len(entries) - 1 else '├── '
        output_lines.append(prefix + connector + name)
        if os.path.isdir(full_path):
            extension = '    ' if index == len(entries) - 1 else '│   '
            tree(full_path, prefix + extension, level - 1, output_lines)

def main():
    target_path = input("請輸入完整資料夾路徑：").strip('"')
    if not os.path.isdir(target_path):
        print("錯誤：找不到該路徑或不是資料夾。")
        return

    while True:
        try:
            max_level = int(input("請輸入查詢深度 (0=只顯示當前層, 1=包含子資料夾, 以此類推)："))
            if max_level < 0:
                print("深度不能為負數，請重新輸入。")
                continue
            break
        except ValueError:
            print("請輸入有效的數字。")
    output_lines = ["```", f".  # 來自 {target_path}"]
    tree(target_path, level=max_level, output_lines=output_lines)
    output_lines.append("```")

    output_file = os.path.join(os.path.dirname(__file__), "tree.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    print(f"樹狀結構已儲存到：{output_file}")

if __name__ == '__main__':
    main()
