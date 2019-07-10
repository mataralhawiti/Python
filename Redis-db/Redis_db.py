"how to Python with Redis DB (https://realpython.com/python-redis/?__s=6hywyxj2chop56vawdog)"

""" ### Notes ###
Redis (pronounced RED-iss, or maybe REE-diss or Red-DEES, depending on who you ask), which is a lightning fast in-memory key-value store that can be used for anything from A to Z.

Redis has a client-server architecture and uses a request-response model. This means that you (the client) connect to a Redis server through TCP connection, on port 6379 by default. 
You request some action (like some form of reading, writing, getting, setting, or updating), and the server serves you back a response.

redis-cli vs. redis-server (127.0.0.1:6379)

$ pgrep redis-server


Redis as a Python Dictionary
    * Redis stands for Remote Dictionary Service.
    * “You mean, like a Python dictionary?” you may ask.
    * Yes. Broadly speaking, there are many parallels you can draw between a Python dictionary (or generic hash table) and what Redis is and does:
    * A Redis database holds key:value pairs and supports commands such as GET, SET, and DEL, as well as several hundred additional commands.
    * Redis keys are always strings.
    * Redis values may be a number of different data types. string, list, hashes, geospatial items. the new stream type, etc
    * Many Redis commands operate in constant O(1) time, just like retrieving a value from a Python dict or any hash table.

    * Redis creator Salvatore Sanfilippo calls the project a “data structure server” (rather than a key-value store, such as memcached) because, to its credit, Redis supports 
      storing additional types of key:value data types besides string:string.
"""


""" ### example via redis-cli ###
* Ex 1 :
    127.0.0.1:6379> SET Bahamas Nassau
    OK
    127.0.0.1:6379> SET Croatia Zagreb
    OK
    127.0.0.1:6379> GET Croatia
    "Zagreb"
    127.0.0.1:6379> GET Japan
    (nil)

    -> equivalent in python :
        >>> capitals = {}
        >>> capitals["Bahamas"] = "Nassau"
        >>> capitals["Croatia"] = "Zagreb"
        >>> capitals.get("Croatia")
        'Zagreb'
        >>> capitals.get("Japan")  # None

* Ex 2 :
    127.0.0.1:6379> MSET Lebanon Beirut Norway Oslo France Paris
    OK
    127.0.0.1:6379> MGET Lebanon Norway Bahamas
    1) "Beirut"
    2) "Oslo"
    3) "Nassau"

    -> equivalent in python :
        >>> capitals.update({
        ...     "Lebanon": "Beirut",
        ...     "Norway": "Oslo",
        ...     "France": "Paris",
        ... })
        >>> [capitals.get(k) for k in ("Lebanon", "Norway", "Bahamas")]
        ['Beirut', 'Oslo', 'Nassau']

* Ex 3 [A hash is a mapping of string:string, called field-value pairs, that sits under one top-level key] :
    127.0.0.1:6379> HSET realpython url "https://realpython.com/"
    (integer) 1
    127.0.0.1:6379> HSET realpython github realpython
    (integer) 1
    127.0.0.1:6379> HSET realpython fullname "Real Python"
    (integer) 1

    -> equivalent in python :
    data = {
        "realpython": {
            "url": "https://realpython.com/",
            "github": "realpython",
            "fullname": "Real Python",}}
    ** A Redis hash is roughly analogous to a Python dict that is nested one level deep

    -> HMSET for hashes to set multiple pairs within the hash value object
    127.0.0.1:6379> HMSET pypa url "https://www.pypa.io/" github pypa fullname "Python Packaging Authority"
    OK
    127.0.0.1:6379> HGETALL pypa
    1) "url"
    2) "https://www.pypa.io/"
    3) "github"
    4) "pypa"
    5) "fullname"
    6) "Python Packaging Authority"


-> Note
    * Hashes, lists, and sets each have some commands that are particular to that given data type, which are in some cases denoted by their initial letter:
        * Hashes: Commands to operate on hashes begin with an H, such as HSET, HGET, or HMSET.
        * Sets: Commands to operate on sets begin with an S, such as SCARD, which gets the number of elements at the set value corresponding to a given key.
        * Lists: Commands to operate on lists begin with an L or R. Examples include LPOP and RPUSH. The L or R refers to which side of the list is operated on. 
            * A few list commands are also prefaced with a B, which means blocking. A blocking operation doesn’t let other operations interrupt it while it’s executing. 
              For instance, BLPOP executes a blocking left-pop on a list structure.

    * One noteworthy feature of Redis’ list type is that it is a linked list rather than an array. This means that appending is O(1) while indexing at an arbitrary index number is O(N).

    -> 
    127.0.0.1:6379> FLUSHDB
    OK
    127.0.0.1:6379> QUIT
"""


""" ### Python Redis client library -> redis-py ###
    * It encapsulates an actual TCP connection to a Redis server and sends raw commands, as bytes serialized using the REdis Serialization Protocol (RESP), to the server. 
    * It then takes the raw reply and parses it back into a Python object such as bytes, int, or even datetime.datetime.
"""


import redis
r = redis.Redis()
# r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
# r.get("Bahamas") # return : b'Nassau' -> Python’s bytes type,not str.
# r.get("Bahamas").decode("utf-8") # str


import datetime
today = datetime.date.today() 
visitors = {"dan", "jon", "alex"}
#r.sadd(today, *visitors) # Not acceptable as Redis key must be str 
stoday = today.isoformat()
r.sadd(stoday, *visitors) # sadd: set-add

print(r.smembers(stoday))
print(r.scard(today.isoformat()))
