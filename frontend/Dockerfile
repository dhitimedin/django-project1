# syntax=docker/dockerfile:1

# Dockerfile for React App
FROM node:18.20.4-alpine

# Set working directory
WORKDIR /frontend

# Install app dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy all source code to container
COPY . .

# Expose environment variable for paths
ENV PATH="./node_modules/.bin:$PATH"

# For production, build the app
RUN npm run build

# Default command for development
CMD [ "npm", "start" ]