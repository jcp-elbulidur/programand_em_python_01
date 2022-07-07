tipo_texto = 'TEsTO'  # 0001 <= texto



# COLECOES

# MUTAVEL OU NAO
# retornando ou nao

# LISTAS 

tipo_lista = [1,2,2,3,4,"5","5",[34,56,99]]

print("Original", tipo_lista)

# METODO APPEND
tipo_lista.append(6)

print("Original", tipo_lista)

# METODO POP
md_pop = tipo_lista.pop(1)
print("md_pop", md_pop)

print("Original", tipo_lista)

# REMOVE 
md_remove = tipo_lista.remove("5")
print('md_remove', md_remove)

print("Original", tipo_lista)

print("Original", tipo_lista)

#  TUPLAS 

tipo_tupla = ('Seg', 'Ter', 'Qua', 'Seg')

pessoas = [1,2,3,4]

rel_1 = (1,4,4,2,4,3)

# METODO COUNT
md_count = rel_1.count(4)
print('md_count', md_count)


# METODO
md_index = tipo_tupla.index('Seg')
print("md_index", md_index)


# DICIONARIO

print('*'*10, 'DICIONARIO')

tipo_dict = {'CHAVE': 'VALOR'}

pessoa = {'Nome': "Julio", "Time": "Sao Paulo"}

md_keys = pessoa.keys()
md_values = pessoa.values()
md_items = pessoa.items()

print("md_keys", md_keys)
print("md_values", md_values)
print("md_items", md_items)

print(pessoa.get("Julio"))
print(pessoa["Nome"])







