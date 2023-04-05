FROM nginx:1.22.0-alpine

RUN chmod +x /start.sh

# Elimina el archivo de configuración predeterminado
RUN rm /etc/nginx/conf.d/default.conf

# Copia el script de inicio personalizado
COPY start.sh /start.sh

# Cambia los permisos del script de inicio para hacerlo ejecutable
RUN chmod +x /start.sh

# Copia la configuración de Nginx
COPY nginx.conf /etc/nginx/conf.d
