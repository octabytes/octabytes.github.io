---
draft: false
title: Redis
content:
  id: redis
  name: Redis
  logo: /images/databases/nosql/redis/logo.png
  website: https://redis.io/
  iframe_website: /website-iframe/databases/nosql/redis
  dashboardImage: /images/databases/nosql/redis/screenshot-1.jpg
  short_description: Redis is an open-source, in-memory database, cache and message broker.
  description: Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperlogs, geospatial indexes, and streams. It has built-in replication, Lua scripting, LRU eviction, transactions, etc. Different processes can query and modify the same data structures in a shared way. Redis delivers sub-millisecond response times, enabling millions of requests per second for real-time applications.
  features:
    - title: In-memory store
      description: All data in Redis is stored in RAM, delivering the fastest possible access times to the data for both read and write requests.
    - title: Optimized for speed
      description: Written in ANSI C, Redis compiles into extremely efficient machine code and requires little overhead. It uses a (mostly) singlethreaded event loop model that optimally uses the CPU core it's running on. The data structures used internally are implemented for maximum performance.
    - title: Support for arbitrary data
      description: Data stored in Redis can be in any form and size. Redis is binary-safe so it can store any data, from human readable text to encoded binaries. A single data element in Redis can range in size from 0 bytes to 0.5GB, allowing it to cache almost any datum.
    - title: Key-based access
      description: Data is stored and fetched from Redis by key. Keybased access allows for extremely efficient access times, and this model maps naturally to caching. Redis provides the customary GET and SET semantics for interacting with the data.
  screenshots:
    - /images/databases/nosql/redis/screenshot-1.jpg
    - /images/databases/nosql/redis/screenshot-2.jpg
---