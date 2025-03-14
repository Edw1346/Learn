import subprocess

"""El módulo subprocess en Python se usa para ejecutar nuevos procesos, interactuar con ellos y obtener su salida. Es útil 
cuando necesitas ejecutar comandos del sistema operativo, como ejecutar scripts o programas desde tu código Python."""
#El módulo subprocess de Python ofrece diversas funciones para ejecutar comandos del sistema y interactuar con procesos. 

#1. subprocess.run(args, *, input=None, capture_output=False, text=False, timeout=None, check=False, cwd=None, env=None, shell=False, executable=None, bufsize=-1, universal_newlines=False, encoding=None, errors=None)
#Ejecuta un comando y espera su finalización. Es la forma más sencilla de ejecutar procesos desde Python. Parámetros: 
#args: Secuencia (lista o cadena) de comandos que se van a ejecutar.
#input: Datos que se enviarán al proceso a través de la entrada estándar.
#capture_output: Si es True, captura la salida estándar y error estándar.
#text: Si es True, las entradas y salidas se manejan como cadenas de texto en lugar de bytes.
#timeout: El tiempo máximo (en segundos) para esperar la terminación del proceso.
#check: Si es True, lanza una excepción si el código de salida es distinto de cero. Ejemplo: 
result = subprocess.run(['ls', '-l'], capture_output=True, text=True) 
print(result.stdout) # Muestra la salida del comando 

#2. subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
#Lanza un proceso y permite interactuar con él de manera más flexible. Proporciona un control detallado sobre la entrada, salida y error del proceso. Parámetros: 
#args: El comando a ejecutar.
#stdin, stdout, stderr: Especifica los flujos de entrada, salida y error.
#bufsize: Tamaño del búfer para los flujos.
#shell: Si es True, ejecuta el comando a través de un shell (como /bin/sh).
#cwd: Establece el directorio de trabajo del proceso. Ejemplo: 
process = subprocess.Popen(['echo', 'Hola'], stdout=subprocess.PIPE, text=True) 
output = process.communicate()[0] 
print(output) # Muestra "Hola" 

#3. subprocess.call(args, *, timeout=None, cwd=None, env=None, shell=False, executable=None)
#Ejecuta un comando y espera a que termine. Devuelve el código de salida del proceso. Parámetros: 
#args: Comando a ejecutar.
#timeout: El tiempo máximo para esperar la finalización. Ejemplo: 
return_code = subprocess.call(['ls', '-l']) 
print(return_code) # Imprime el código de salida, 0 si todo salió bien 

#4. subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, timeout=None, cwd=None, env=None, universal_newlines=False, encoding=None, errors=None)
#Ejecuta un comando y devuelve su salida estándar. Lanza una excepción si el código de salida del comando es distinto de 0. Parámetros: 
#args: Comando a ejecutar.
#stdin, stderr: Redirige las entradas y salidas del comando. Ejemplo: 
output = subprocess.check_output(['echo', 'Hola'], text=True) 
print(output) # Muestra "Hola" 

#5. subprocess.check_call(args, *, timeout=None, cwd=None, env=None, shell=False, executable=None)
#Ejecuta un comando y espera a que termine. Lanza una excepción si el código de salida es distinto de 0. Parámetros: 
#args: Comando a ejecutar.
#timeout: El tiempo máximo para esperar la terminación del proceso. Ejemplo: 
subprocess.check_call(['ls', '-l']) # Lanza una excepción si el comando falla 

#6. subprocess.check_returncode()
#Revisa el código de salida del proceso. Si es distinto de cero, lanza una excepción CalledProcessError. Ejemplo: 
process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE) 
process.communicate() 
process.check_returncode() # Lanza una excepción si el código de salida es distinto de 0 

#7. subprocess.getoutput(cmd)
#Ejecuta un comando en el sistema y devuelve su salida estándar como una cadena. Es un atajo para subprocess.run() con capture_output=True. Ejemplo: 
output = subprocess.getoutput('ls -l') 
print(output) # Muestra la salida del comando 

#8. subprocess.getstatusoutput(cmd)
#Ejecuta un comando y devuelve una tupla (status, output), donde status es el código de salida y output es la salida estándar del comando. Ejemplo: 
status, output = subprocess.getstatusoutput('ls -l') 
print(status, output) # Muestra el código de salida y la salida del comando 

#9. subprocess.run_check(args, *, timeout=None, cwd=None, env=None, shell=False, executable=None)
#Ejecuta un comando y lanza una excepción si el código de salida es distinto de 0 (equivalente a check_call pero más flexible). Ejemplo: 
subprocess.run_check(['ls', '-l']) # Lanza una excepción si el comando falla 

#run: Ejecuta el comando y espera el resultado.
#Popen: Permite un control detallado de los procesos en ejecución.
#call: Ejecuta el comando y espera a que termine, devuelve el código de salida.
#check_output: Ejecuta un comando y devuelve su salida estándar, lanza excepción si falla.
#check_call: Ejecuta un comando y lanza excepción si el código de salida no es 0.
#getoutput: Ejecuta el comando y devuelve su salida.
#getstatusoutput: Ejecuta un comando y devuelve el código de salida junto con la salida.




"""El módulo subprocess no contiene muchas clases, pero hay algunas relevantes para interactuar con los procesos que se ejecutan."""

#1. subprocess.CompletedProcess. Esta clase encapsula el resultado de un comando ejecutado con la función subprocess.run(). El objeto de esta clase contiene información sobre el proceso terminado, como el código de salida, la salida estándar y el error estándar.
#Atributos importantes:
#args: Los argumentos pasados al comando.
#returncode: El código de salida del proceso.
#stdout: La salida estándar del proceso (si fue capturada).
#stderr: El error estándar del proceso (si fue capturado). Ejemplo:
result = subprocess.run(['echo', 'Hola'], capture_output=True, text=True) 
print(result.returncode) # Código de salida 
print(result.stdout) # Salida estándar 
print(result.stderr) # Error estándar (si lo hubiera) 


#2. subprocess.Popen. La clase Popen es una de las clases más importantes del módulo subprocess. Permite interactuar de manera más avanzada con un proceso, ya que da control total sobre el flujo de entrada y salida, y permite ejecutar el proceso de manera asíncrona.
#Métodos importantes:
#communicate(): Interactúa con proceso y obtiene salida. Ideal para procesos que leen o escriben mucho.
#wait(): Espera a que el proceso termine.
#poll(): Verifica si el proceso terminó (devuelve None si sigue ejecutándose).
#Terminate(): Termina el proceso de manera abrupta. Ejemplo:
process = subprocess.Popen(['echo', 'Hola'], stdout=subprocess.PIPE, text=True) 
output = process.communicate()[0] 
print(output) # Muestra "Hola" 

#3. subprocess.Popen.communicate(input=None, timeout=None)
#Este método es parte de la clase Popen. Se usa para enviar datos al proceso a través de su entrada estándar y obtener la salida del proceso. Este método también espera a que el proceso termine. Ejemplo:
process = subprocess.Popen(['grep', 'hola'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) 
output = process.communicate(input="hola mundo\nadiós mundo\n")[0] 
print(output) # Muestra 'hola mundo\n' 

#4. subprocess.Popen.wait() 
#Este método también es parte de la clase Popen. Se utiliza para esperar hasta que el proceso termine y devuelve su código de salida. Ejemplo:
process = subprocess.Popen(['sleep', '2']) 
exit_code = process.wait() # Espera a que termine el proceso 
print(f"El código de salida es {exit_code}") 

#5. subprocess.Popen.poll()
#Este método verifica si el proceso ha terminado. Si el proceso sigue ejecutándose, devuelve None; si terminó, devuelve el código de salida. Ejemplo:
process = subprocess.Popen(['sleep', '2']) 
status = process.poll() # Devuelve None mientras el proceso está en ejecución 
print(status) # None mientras espera 


#CompletedProcess: Representa el resultado de un proceso ejecutado mediante subprocess.run().
#Popen: Permite una mayor flexibilidad para interactuar con procesos en ejecución, permite capturar entrada y salida, controlar el proceso, y más.





"""El módulo subprocess no tiene variables globales o predefinidas que se usen de manera directa en la mayoría de las 
interacciones, sino que su funcionalidad se centra más en las funciones y clases para crear y manejar procesos. 
Sin embargo, existen algunas variables relacionadas con configuraciones y comportamientos dentro de los métodos y 
funciones del módulo"""

#1. subprocess._args_from_interpreter_flags (Interno)
#Es una variable interna que permite obtener los flags del intérprete de Python. Esta variable no suele usarse directamente a menos que estés manipulando el comportamiento interno de la ejecución del proceso de Python.

#2. subprocess._get_default_timeout (Interno)
#Es otra variable interna que establece el valor predeterminado de timeout para las funciones. No está destinada para uso general, pero puede ser relevante cuando se exploran configuraciones avanzadas de procesos.





"""El módulo subprocess incluye varias constantes predefinidas que se utilizan para controlar cómo se interactúa con los 
procesos. Aquí están las más relevantes:"""

#1. subprocess.PIPE
#Se utiliza para crear un canal de comunicación entre tu script y el proceso que estás ejecutando. Permite redirigir la entrada o salida estándar del proceso. Se usa cuando quieres capturar la salida o enviar datos a un proceso. Ejemplo: 
process = subprocess.Popen(['echo', 'Hola'], stdout=subprocess.PIPE) 
output = process.communicate()[0] 
print(output) # Muestra "Hola" 

#2. subprocess.STDOUT
#Permite redirigir la salida de error estándar (stderr) al mismo flujo que la salida estándar (stdout). Esto es útil cuando quieres capturar tanto la salida estándar como los errores en un solo flujo. Se usa cuando rediriges ambos flujos al mismo lugar, por ejemplo, al archivo o a la variable. Ejemplo: 
process = subprocess.Popen(['ls', 'no_existent_file'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
output = process.communicate()[0] 
print(output) # Muestra los errores de 'ls' en la salida estándar 

#3. subprocess.DEVNULL
#Redirige la salida estándar o de error a un lugar nulo, es decir, descarta cualquier salida. Es útil cuando no te importa lo que el proceso está imprimiendo o mostrando. Se usa cuando no deseas que se muestre nada en la consola ni se capture la salida. Ejemplo: 
subprocess.run(['echo', 'Hola'], stdout=subprocess.DEVNULL) # No imprime nada 

#4. subprocess.RUN_TIME
#Esta constante representa el tiempo de ejecución de un proceso, pero no es comúnmente utilizada en los ejemplos. Está relacionada con el seguimiento del tiempo de ejecución de los procesos.

#5. subprocess.TimeoutExpired (Excepción)
#Aunque no es estrictamente una constante, se usa para indicar que el proceso se agotó por el tiempo límite (timeout) que se había establecido.

#subprocess.PIPE: Redirige entradas y salidas del proceso.
#subprocess.STDOUT: Redirige la salida estándar de error al mismo lugar que la salida estándar.
#subprocess.DEVNULL: Descarta cualquier salida del proceso.



"""El módulo subprocess en Python define varias excepciones que se utilizan para manejar errores durante la ejecución de procesos"""

#1. subprocess.SubprocessError
#Es la clase base para todas las excepciones relacionadas con el módulo subprocess. Generalmente, no se utiliza directamente, pero puede servir como punto de captura genérico para todas las excepciones del módulo. Puedes capturar esta excepción si deseas manejar cualquier error relacionado con la ejecución de procesos. Ejemplo: 
try: 
    subprocess.run(['non_existent_command']) 
except subprocess.SubprocessError as e: 
    print(f"Error en el proceso: {e}") 

#2. subprocess.CalledProcessError
#Se lanza cuando un proceso ejecutado con subprocess.run() o subprocess.check_call() devuelve un código de salida distinto de cero (lo que indica un error).
#Atributos importantes: 
#returncode: El código de salida del proceso.
#cmd: El comando que se ejecutó.
#output: La salida estándar capturada.
#stderr: El error estándar capturado.
#Se utiliza para capturar errores cuando un comando falló y necesitas obtener detalles sobre el comando que falló. Ejemplo: 
try: 
    subprocess.run(['ls', 'no_existent_file'], check=True) 
except subprocess.CalledProcessError as e: 
    print(f"El comando falló con código de salida {e.returncode}") 
print(f"Salida: {e.output}") 

#3. subprocess.TimeoutExpired
#Se lanza cuando un proceso supera el tiempo límite especificado mediante el parámetro timeout en funciones como subprocess.run().
#Atributos importantes: 
#cmd: El comando que se ejecutó.
#timeout: El tiempo de espera que se especificó.
#output: La salida estándar capturada (si se especificó capture_output=True).
#stderr: El error estándar capturado (si se especificó capture_output=True).
#Se utiliza cuando un proceso se ejecuta durante más tiempo del que se permitió y se agota el tiempo de espera. Ejemplo: 
try: 
    subprocess.run(['sleep', '10'], timeout=5) 
except subprocess.TimeoutExpired as e: 
    print(f"El proceso tardó demasiado tiempo. Comando: {e.cmd}") 

#4. subprocess.InvalidCommand (Interna)
#Es una excepción interna y no se lanza directamente. Está relacionada con el manejo de comandos incorrectos o mal formateados.

#5. subprocess.NotImplementedError
#Esta excepción puede ser lanzada si se invoca una funcionalidad que no está implementada en la plataforma o entorno en el que se está ejecutando el código.

#Resumen de las Excepciones más Importantes:
#subprocess.SubprocessError: Excepción base para errores en procesos.
#subprocess.CalledProcessError: Se lanza cuando un proceso termina con código de salida diferente de 0.
#subprocess.TimeoutExpired: Se lanza cuando un proceso supera el tiempo de espera.




"""El módulo subprocess no contiene submódulos adicionales. Es un módulo único y completo que se usa para crear y gestionar 
procesos, así como para interactuar con su entrada, salida y errores. Aunque se puede trabajar con varios aspectos del 
proceso utilizando sus funciones, clases y constantes, todo esto se encuentra directamente dentro del propio módulo subprocess."""

