import yaml 

with open ('prueba.yaml','r') as fichero_yaml:
    # Content es un diccionario
    content = yaml.load(fichero_yaml, Loader=yaml.FullLoader)
    print(content)

    # Añadimos contenido al fichero
    content['servers'].append({'name': 'Facebook', 'ips': ['www.facebook.es']})

with open ("modificado.yaml","w") as fichero_yaml:
    yaml.dump(content, fichero_yaml)