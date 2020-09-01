

# Imprime en consola `Hello World`.

print "Hello World"

# Crea un directorio nuevo llamado `new_dir`.

mkdir new_dir

# Elimina ese directorio.

rm -r new_dir

# Copia el archivo `sed.txt` dentro de la carpeta lorem a la carpeta lorem-copy. 

cp -v ./lorem/sed.txt ./lorem-copy 

# Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante `;`. 

cp -v ./lorem/lorem.txt ./lorem-copy ; ./lorem/at.txt ./lorem-copy

# Muestra el contenido del archivo `sed.txt` dentro de la carpeta lorem.

cat ./lorem/sed.txt    

# Muestra el contenido de los archivos `at.txt` y `lorem.txt` dentro de la carpeta lorem. 

cat ./lorem/at.txt  ./lorem/lorem.txt  

# Visualiza las primeras 3 líneas del archivo `sed.txt` dentro de la carpeta lorem-copy 

cat ./lorem-copy/sed.txt | head -n 3

#  Visualiza las ultimas 3 líneas del archivo `sed.txt` dentro de la carpeta lorem-copy 

cat ./lorem-copy/sed.txt | tail -n 3

# Añade `Homo homini lupus.` al final de archivo `sed.txt` dentro de la carpeta lorem-copy. 

nano ./lorem-copy/sed.txt

# Visualiza las últimas 3 líneas del archivo `sed.txt` dentro de la carpeta lorem-copy. Deberías ver ahora `Homo homini lupus.`. 

cat ./lorem-copy/sed.txt | tail -n 3

# Sustituye todas las apariciones de `et` por `ET` del archivo `at.txt` dentro de la carpeta lorem-copy. Deberás usar `sed`. 

sed -i 's/et/ET/g' ./lorem-copy/at.txt

# Encuentra al usuario activo en el sistema.
whoami

# Encuentra dónde estás en tu sistema de ficheros.

pwd

# Lista los archivos que terminan por `.txt` en la carpeta lorem.

find -f ./lorem/*.txt

# Cuenta el número de líneas que tiene el archivo `sed.txt` dentro de la carpeta lorem. 

wc -l ./lorem/sed.txt

# Cuenta el número de **archivos** que empiezan por `lorem` que están en este directorio y en directorios internos.

find . -name "lorem*" | wc -l 

# Encuentra todas las apariciones de `et` en `at.txt` dentro de la carpeta lorem.

 fgrep et  ./lorem/at.txt

# Cuenta el número de apariciones del string `et` en `at.txt` dentro de la carpeta lorem. 

 fgrep et  ./lorem/at.txt | wc -l  

#  Cuenta el número de apariciones del string `et` en todos los archivos del directorio lorem-copy. 
fgrep -r et ./lorem-copy | wc -l



## Bonus

# Almacena en una variable `name` tu nombre.

name='Jorge'

# Imprime esa variable.

echo $name

# Crea un directorio nuevo que se llame como el contenido de la variable `name`.

mk dir $name

# Elimina ese directorio. 

rm -r $name

# Por cada archivo dentro de la carpeta `lorem` imprime el número de carácteres que tienen sus nombres. 

1. for file in $(ls lorem)
   echo $file

2. for file in $(ls lorem)
   echo $file | wc -m

3. for file in $(ls lorem)
   echo f"lorem has {$file | wc -m} characters long" #ESTÁ MAL 

Intenta primero mostrar los archivos mediante un bucle for 
    1. Imprime los ficheros
    2. Imprime las longitudes de los nombres de los ficheros
    3. Imprime outputs con la siguiente estructura: `lorem has 5 characters lenght`

# Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:
    
    1. top
    2. ps -f     
       
    1. Usando el comando top o htop
    2. Usando el comando ps con argumentos

# Muestra información sobre tu procesador por pantalla

lscpu

# Crea 3 alias y haz que estén disponibles cada vez que inicias sesión

alias mad="cd /home/jorge-alamillos/ironhack/datamad0820/" 
alias apuntes="cd /home/jorge-alamillos/ironhack/apuntes_marc/datamad2008"
alias pull_marc="git pull" 
# Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz

tar -czvf loremcompressed.tar.gz ./lorem*

# Descomprime el archivo lorem-compressed.tar.gz en la carpeta lorem-uncompressed

tar -xzvf loremcompressed.tar.gz -C /lorem-uncompressed

