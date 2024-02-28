
cut -f 4 -d ',' $1 | tr -s '\n' | grep -v "Time of Day"

