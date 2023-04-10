# Imagenes de Docker para ubuntu18 con Ros y Gazebo 
La(s) imagenes son para el sistema operativo, librerias actualizadas, etc. Cambios en archivos son en Github. 


### Pasos para correrla
* Descargar imagen de https://hub.docker.com/repository/docker/a00829053/ubuntu18_ros/general 
* ```docker pull a00829053/ubuntu18_ros:latest```. Si es en linux, agregar sudo
* ```docker tag a00829053/ubuntu18_ros:latest [Nombre Imagen a la que se guarda]```
* ```docker run -p 6080:80 -v /dev/shm:/dev/shm [NOMBRE IMAGEN]```

### Para guardar cambios en local
Esto es para cambios de archivos locales etc. No para los cambios que se van a empujar al repositorio de Docker


* ```docker ps -a```
* Checar CONTAINER ID de imagen deseada
* ```docker commit [CONTAINER ID] [NOMBRE IMAGEN]:[TAG (OPCIONAL)]```



### Para hacer cambios:
* ```docker run -p 6080:80 -v /dev/shm:/dev/shm a00829053/ubuntu18_ros:v1.x```
* Realizar cambios ahi
* ```docker ps```
* Checar CONTAINER ID de imagen corriendo
* ```docker commit [CONTAINER ID] [NOMBRE IMAGEN]```
* Ir a https://hub.docker.com/repository/docker/a00829053/ubuntu18_ros/general y en tags checar ultima version subida
* ```docker tag [NOMBRE IMAGEN] a00829053/ubuntu18_ros:v1.x``` donde x es la version anterior mas 1
* ```docker push a00829053/ubuntu18_ros:v1.x```
