# pull official base image
FROM node:18-alpine

# set working directory
WORKDIR /webapp

# install and cache app dependencies
COPY package.json .
COPY package-lock.json .
RUN npm ci
RUN npm install react-scripts@5.0.1 -g --silent

COPY . /webapp

EXPOSE 3000

# start app
CMD ["npm", "start"]
