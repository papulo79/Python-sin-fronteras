from camelcase import CamelCase

c = CamelCase()
text = "texto sin camelcase"

print(c.hump(text))
