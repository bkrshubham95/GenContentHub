FROM node:18.13.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install -g npm@9.6.4
RUN npm install --silent

# add app
COPY . ./

# start app
CMD ["npm", "start"]