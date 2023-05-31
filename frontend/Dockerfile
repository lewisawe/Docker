# Use the official Node.js base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install the npm dependencies
RUN npm install

# Copy the React application code
COPY . .

# Build the React application
RUN npm run build

# Expose the React application port
EXPOSE 3000

# Run the React application server
CMD ["npm", "start"]
