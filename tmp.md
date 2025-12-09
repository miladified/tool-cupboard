```
jq '.[].Url' menus.json | grep -v '^""$' | tr -d '"' > uris.txt && cat uris.txt
```