import redis

def main():
    client = redis.Redis(host='47.106.174.119', port='19940', password='dyl1994')
    if client.ping():
        print(client.keys('*'))
        print(client.get('user').decode('utf-8'))
        print(client.get('name').decode('utf-8'))
        print(list(map(lambda x: x.decode('utf-8'), client.zrange('fuck', start=0, end=-1))))


if __name__ == '__main__':
    main()