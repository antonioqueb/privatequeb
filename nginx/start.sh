#!/bin/sh

# Espera a que los certificados estén disponibles
while [ ! -f /etc/letsencrypt/live/queb.online/fullchain.pem ] || [ ! -f /etc/letsencrypt/live/queb.online/privkey.pem ]; do
  echo "Esperando a que los certificados SSL estén disponibles..."
  sleep 5
done

echo "Certificados SSL disponibles, iniciando Nginx..."
exec nginx -g "daemon off;"
