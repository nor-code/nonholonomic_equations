import redis
import pickle

client = redis.Redis(host='localhost', port=6379, db=0)
client.set('test-key', 'test-value')

# get a value
value = client.get('test-key')
print(value)