import re
log = "2026-04-01 ERROR Failed to connect"
match = re.match(r'^(\d{4}-\d{2}-\d{2})\s+(INFO|ERROR|WARNING|DEBUG)\s+(.+)$', log)
if match:
    print({'date': match.group(1), 'level': match.group(2), 'message': match.group(3)})