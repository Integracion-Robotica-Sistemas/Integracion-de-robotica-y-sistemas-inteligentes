# Integracion-de-robotica-y-sistemas-inteligentes
Clase de Integración de robótica y sistemas inteligentes

### SSH Key
Para poder hacer push requests, es necesario tener permiso, y realizar la creacion de SSH keys:
* Ir a: https://github.com/settings/keys, y hacer click en new ssh key 
![image](https://user-images.githubusercontent.com/66874216/229581393-e734521d-3882-443d-ac24-ce128ff3aebe.png)

* Escribir en terminal para generar una nueva ssh key: `ssh-keygen -t ed25519 -C "your_email@example.com"`
* Presionar ENTER para las siguientes tres preguntas
* Guardar el nombre del archivo de la primera pregunta `Enter file in which to save the key (/home/ubuntu/.ssh/id_ed11111)`, se guarda `id_ed11111`
* Escribir en terminal `cat ~/.ssh/id_ed25519.pub` para visualizar la nueva key
* Nombrar la key cualquier cosa en la seccion de title en Github, Copiar la key y pegarla en la seccion de key en github
![image](https://user-images.githubusercontent.com/66874216/229585434-8a1c26c9-e0cc-4114-a52f-2069b02d631d.png)

* Escribir en terminal `eval "$(ssh-agent -s)"` para inicializar el agente
* Escribir en terminal `ssh-add ~/.ssh/id_ed25519` para agregar la key al agente

Se pueden ayudar de las siguientes referencias:
* https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
* https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

