#official Node.js image as base
From node:16-alpine as builder

#set working directory
WORKDIR /web_app

# install app dependencies
COPY package*.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

#START APP 
RUN npm install

#add app
COPY . .

#Build the react app
RUN npm run builder

#use nginx
FROM nginx:alpine

#Copy the built React app from the previous stage to the nginx web server
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Command to start the nginx server
CMD ["nginx", "-g", "daemon off;"]





