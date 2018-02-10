#######################################
# frontend/Dockerfile - Defines the container used to generate
# the web front-end framework for this todo app.
#######################################

# base image
FROM node

# Set up working directoray
RUN mkdir /usr/src/todo
WORKDIR /usr/src/todo

# Add node modules to path
ENV PATH /usr/src/todo/node_modules/.bin:$PATH

# install and cache dependencies
ADD package.json /usr/src/app/package.json
RUN npm install --silent
RUN npm install react-scripts -g --silent

# start app
CMD ["npm", "start"]
