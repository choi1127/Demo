# 1. pip install rich 가 필요합니다.
# pip install rich

from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

# 2. 변수
name = "Alice"
age = 25
score = 95.5
data = {"name": name, "age": age, "score": score}

# 3. f-string 컬러/스타일 출력 (f-string)
rprint(f"[bold green]Hello[/], {name}! Your score is [cyan]{score:.2f}[/].")

# 4. 패널(박스) 멀티라인 출력
panel_text = f"""
[bold]Student Info[/]
- Name : [yellow]{name}[/]
- Age : [magenta]{age}[/]
- Score: [cyan]{score:.2f}[/]
"""
rprint(Panel(panel_text, title="ProFile", border_style="blue"))

# 5. 테이블 출력 (딕셔너리/리스트 보기 좋게)
table = Table(title="Records")
table.add_column("Key", style="bold")
table.add_column("Value")

for k, v in data.items():
    table.add_row(k, str(v))

rprint(table)

# 6. sep, end 옵션 그대로 활용 (rich.print 동일 동작)
rprint("2025", "09", "23", sep="-", end="🎉\n")