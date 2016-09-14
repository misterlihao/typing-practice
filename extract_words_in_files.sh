sed 's/[^a-zA-Z]/\n/g' "$@" | sed -rn 's/^([a-zA-Z]{3,30})$/\1/p' | sort | uniq -iw 4
