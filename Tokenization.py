import tiktoken

enc=tiktoken.get_encoding("cl100k_base")
tokens=enc.encode("Hello World, this is the first GenAI Program")
print(tokens)

result=enc.decode(tokens)
print(result)

#Context Window
#Max Token

