FROM node:16-alpine
WORKDIR /app/
COPY package.json package-lock.json ./
# commented out for development otherwise docker-compose.yml volume 
# overwrites node_modules on cleanStart
RUN npm install
