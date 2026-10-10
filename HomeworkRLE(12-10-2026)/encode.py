def encode(inp: str) -> str:
    out :str = ""
    curr :str = inp[0]
    count :int = 1
    for i in range(1, len(inp)):
       if not curr == inp[i]:
          out = out+curr+str(count)
          curr = inp[i]
          count = 1
       else:
           count += 1

    out = out + curr + str(count)
    return out


a = input("Enter string: ")
print(encode(a))