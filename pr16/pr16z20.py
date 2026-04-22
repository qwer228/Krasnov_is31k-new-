import re
logs = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""
error_lines = [line for line in logs.splitlines() if re.search(r'\bERROR\b', line)]
dates = [re.match(r'^(\d{4}-\d{2}-\d{2})', line).group(1) for line in error_lines]
counts = {}
for d in dates:
    counts[d] = counts.get(d, 0) + 1
print({'error_lines': error_lines, 'dates': dates, 'count_by_date': counts})