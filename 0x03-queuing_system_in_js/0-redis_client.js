// Import the redis library
import redis from 'redis';

// Create a new client
const client = redis.createClient();

// Handle the connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});
