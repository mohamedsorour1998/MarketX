# Use the official Node.js image as a base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application to the working directory
COPY . .

# Expose the port on which your app will run
EXPOSE 4200

# Start the application
CMD ["npm", "run", "start", "--", "--host", "0.0.0.0", "--disable-host-check"]
