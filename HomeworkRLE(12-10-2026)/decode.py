def decode(inp :str) -> str:
    out = ""
    for i in range(0, len(inp), 2):
        for _ in range(int(inp[i+1])):
            out += inp[i]
            
    return out
    
a = input("Enter encoded string: ")
print(decode(a))