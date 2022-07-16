
# items() method is used to return the list with all dictionary keys with values.
d1={101:"gfg",103:"practice",102:"ide"}
d2={v:k for(k,v) in d1.items()}

print(d2)