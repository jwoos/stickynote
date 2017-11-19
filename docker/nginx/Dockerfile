FROM nginx:mainline-alpine

COPY nginx.conf /opt/
COPY static /opt/static

CMD ["nginx", "-c", "/opt/nginx.conf", "-g", "daemon off;"]
