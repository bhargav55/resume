#!/usr/bin/env bash
# Track job applications. Usage:
#   ./scripts/apply-tracker.sh add "Ethena Labs" "Smart Contract Engineer" "https://..." "Applied"
#   ./scripts/apply-tracker.sh list
#   ./scripts/apply-tracker.sh status "Ethena Labs"

TRACKER_FILE="applications.csv"

if [[ ! -f "$TRACKER_FILE" ]]; then
  echo "Date,Company,Role,Link,Status,Notes" > "$TRACKER_FILE"
fi

case "$1" in
  add)
    DATE=$(date +%Y-%m-%d)
    echo "$DATE,\"$2\",\"$3\",\"$4\",\"${5:-Applied}\",\"${6:-}\"" >> "$TRACKER_FILE"
    echo "Logged: $2 — $3"
    ;;
  list)
    column -t -s',' "$TRACKER_FILE"
    ;;
  status)
    grep -i "$2" "$TRACKER_FILE" | column -t -s','
    ;;
  *)
    echo "Usage:"
    echo "  $0 add <company> <role> <link> <status> [notes]"
    echo "  $0 list"
    echo "  $0 status <company>"
    ;;
esac
