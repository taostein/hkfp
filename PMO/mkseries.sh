
cut -f 2 -d ',' $1 | tr -s '\n' | grep -v "Date" | sort | uniq -c | awk '{print $2,",",$1}' | sed -e "s/ //g"

