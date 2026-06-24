# Imagen base de Nginx
FROM nginx:alpine

# Copiar el archivo HTML al directorio de Nginx
COPY index.html /usr/share/nginx/html/

# Copiar configuración personalizada de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponer puerto 80
EXPOSE 80

# Nginx se ejecuta automáticamente con la imagen