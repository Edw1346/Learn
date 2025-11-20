import json

"""El módulo json se utiliza para trabajar con datos en formato JSON (JavaScript Object Notation). 
Permite convertir entre objetos de Python (diccionarios y listas) y cadenas de texto en formato JSON"""

#json.dumps(obj, *, indent=None, separators=None). Convierte un objeto de Python en una cadena JSON:
json_str = json.dumps({"nombre": "Juan", "edad": 30}) #json.dums({'Nombre':'Layer'})
print(json_str) 

#json.loads(s, *, object_hook=None, **kw). Convierte una cadena JSON en un objeto Python:
data = json.loads('{"nombre": "Pedros", "edad": 40}') #json.loads({'Nombre':'Luis'})
print(data) 

#json.dump(obj, fp, *, separators=None,). Convierte un objeto de Python y lo escribe en un archivo JSON:
with open('data.json', 'w') as f:
    json.dump({"nombre": "Carlos", "edad": 50}, f) 

#json.load(fp, *, object_hook=None, **kw). Lee un archivo JSON y lo convierte en un objeto Python:
with open('data.json', 'r') as f: 
    data = json.load(f) 
    print(data) 

#json.JSONDecoder.decode(s).Decodifica cadena JSON en objeto Python. Mas directa que json.loads():
decoder = json.JSONDecoder() 
data = decoder.decode('{"nombre": "Josue", "edad": 10}') 
print(data) 

#json.JSONEncoder.encode(obj). Convierte objeto Python en cadena JSON. Mas directa de json.dumps():
encoder = json.JSONEncoder() 
json_str = encoder.encode({"nombre": "Edwin", "edad": 22}) 
print(json_str) 

#json.JSONDecoder.object_pairs_hook. Devuelvan como una lista de tuplas en lugar de un diccionario:
json_str = '{"nombre": "Douglas", "edad": 28}' 
obj = json.loads(json_str, object_pairs_hook=lambda d: [(k, v) for k, v in d.items()]) 
print(obj) # [('nombre', 'Juan'), ('edad', 30)] 

#json.JSONEncoder.default(obj). Permite personalizar cómo se codifican los objetos en JSON, y cuando el objeto no es directamente serializable:
def custom_encoder(obj): 
    if isinstance(obj, set): return list(obj) 

raise TypeError(f"Type {type(obj)} not serializable") 
json_str = json.dumps({1, 2, 3}, default=custom_encoder) 
print(json_str) # [1, 2, 3] 

#json.JSONDecoder.scan_once(string, idx=0). Escanea una cadena JSON una vez y devuelve el objeto y la posición final:
decoder = json.JSONDecoder() 
obj, idx = decoder.scan_once('{"nombre": "Juan"}', 0) 
print(obj) # {'nombre': 'Juan'} 
