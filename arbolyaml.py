import yaml

with open('ejemplo.yaml') as f: #tenemos que tener creada el archivo ejemplo 
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

with open('root.yaml') as f: #tenemos que tener creada el archivo root 
    
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:
        
        for k, v in doc.items():
            print(k, "->", v)