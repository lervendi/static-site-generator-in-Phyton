import textwrap
import re

def markdown_to_blocks(markdown):
    markdown = textwrap.dedent(markdown)
    lines = markdown.split("\n")

    blocks = []
    current = []
    current_kind = None
    in_code = False

    def line_kind(line: str) -> str:
        s = line.strip()
        if s == "":
            return "blank"
        if s.startswith("```"):
            return "code_fence"
        if re.match(r"^#{1,6} ", s):
            return "heading"
        if s.startswith("> "):
            return "quote"
        if re.match(r"^\d+\. ", s):
            return "ol"
        if s.startswith("- ") or s.startswith("* "):
            return "ul"
        return "other"

    for line in lines:
        kind = line_kind(line)

        # Уже внутри code-блока
        if in_code:
            current.append(line)
            if kind == "code_fence":
                # Закрываем code-блок
                blocks.append("\n".join(current).strip())
                current = []
                in_code = False
                current_kind = None
            continue

        # Начало / конец code-блока
        if kind == "code_fence":
            # Перед кодом закрываем обычный блок
            if current:
                blocks.append("\n".join(current).strip())
                current = []
                current_kind = None
            in_code = True
            current.append(line)
            continue

        # Пустая строка — конец блока
        if kind == "blank":
            if current:
                blocks.append("\n".join(current).strip())
                current = []
                current_kind = None
            continue

        # Обычные строки вне кода
        if current_kind is None:
            # начинаем новый блок
            current = [line]
            current_kind = kind
        else:
            if kind == current_kind:
                # тот же тип блока — продолжаем
                current.append(line)
            else:
                # тип изменился — закрываем блок и начинаем новый
                blocks.append("\n".join(current).strip())
                current = [line]
                current_kind = kind

    # Хвост, если остался
    if current:
        blocks.append("\n".join(current).strip())

    return blocks
