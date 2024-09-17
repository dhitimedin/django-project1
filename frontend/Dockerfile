FROM node:18.20.4-alpine
WORKDIR /frontend
ENV PATH="./node_module/.bin:$PATH"
COPY . .
RUN npm run build
CMD [ "npm", "start" ]