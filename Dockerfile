FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY esporte-fantoken-mcp-ia.pdf /usr/share/nginx/html/esporte-fantoken-mcp-ia.pdf
