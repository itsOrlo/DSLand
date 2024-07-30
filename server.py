#Forge 1.20.1
#Playit (Configurar después de inicializar el servidor)

# Configuración


#Librerías py
import requests,os,base64,glob,time,threading
if os.path.exists("servidor.py"):
	os.remove("servidor.py")
if not os.path.exists("./.gitignore"):
	big = "L1B5dGhvbioNCi93b3JrX2FyZWEqDQovc2Vydmlkb3JfbWluZWNyYWZ0DQovbWluZWNyYWZ0X3NlcnZlcg0KL3NlcnZpZG9yX21pbmVjcmFmdF9vbGQNCi90YWlsc2NhbGUtY3MNCi90aGFub3MNCi9zZXJ2ZXJzDQovYmtkaXINCi92ZW5kb3INCmNvbXBvc2VyLioNCmNvbmZpZ3VyYXRpb24uanNvbg0KY29uZmlndXJhY2lvbi5qc29uDQoqLnR4dA0KKi5weWMNCioubXNwDQoqLm91dHB1dA=="
	dec = base64.standard_b64decode(big).decode()
	with open(".gitignore", 'w') as giti:
		giti.write(dec) 
	




#Ping cada 5 minutos para mantener el server
def keep_alive():
    while True:
        try:
            requests.get("https://www.google.com")  # URL de ejemplo
            print("Ping exitoso")
        except:
            print("Error al hacer ping")
        time.sleep(300)  # Ping cada 5 minutos (300 segundos)

# Iniciar el hilo de keep_alive en segundo plano
threading.Thread(target=keep_alive, daemon=True).start()

#Ejecutar chmod por consola a través del ejecutable
def download_latest_release(download_path='.'):
	mirror = "https://elyxdev.github.io/latest"
	pet = requests.get(mirror)
	if pet.status_code == 200:
		data = pet.json()
		url = data.get('latest')
		version = url.split("/")[-1]
		if version in glob.glob("*.msp"):
			return version
		else:
			os.system("rm *.msp")
			print("Actualizando tu versión de MSP...")
			time.sleep(1.5)
		pathto = os.path.join(download_path, version)
		with open(pathto, 'wb') as archivo:
			archivo.write(requests.get(url).content)
		return version
flnm=download_latest_release()
if flnm.split(".")[-1] == "msp":
	os.system(f"chmod +x {flnm} && ./{flnm}")
else:
    os.system(f"python3 {flnm}")