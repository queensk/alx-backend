import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

const hashKey = 'HolbertonSchools';
const hashValues = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const [key, value] of Object.entries(hashValues)) {
  client.hset(hashKey, key, value, redis.print);
}

client.hgetall(hashKey, (err, reply) => {
  if (err) throw err;
  console.log(reply);
});
