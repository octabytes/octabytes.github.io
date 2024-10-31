---
draft: false
title: Valkey
content:
  id: valkey
  name: Valkey
  logo: /images/databases/nosql/valkey/logo.png
  website: https://valkey.io/
  iframe_website: /website-iframe/databases/nosql/valkey
  dashboardImage: /images/databases/nosql/valkey/screenshot-1.jpg
  short_description: A flexible distributed key-value datastore that supports both caching and beyond caching workloads.
  description: Valkey is an open source (BSD) high-performance key/value datastore that supports a variety of workloads such as caching, and message queues, and can act as a primary database. Valkey can run as a standalone daemon or in a cluster, with options for replication and high availability.  Valkey natively supports a rich collection of data types, including strings, numbers, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, and more.
  features:
    - title: In-memory store
      description: All data in Valkey is stored in RAM, delivering the fastest possible access times to the data for both read and write requests.
    - title: Optimized for speed
      description: "Written in ANSI C, Valkey compiles extremely efficient machine code and requires little overhead. It uses a (mostly) single-threaded event loop model that optimally uses the CPU core it's running on. The data structures used internally are implemented for maximum performance."
    - title: Support for arbitrary data
      description: Data stored in Valkey can be in any form and size. Valkey is binary-safe so it can store any data, from human-readable text to encoded binaries. A single data element in Valkey can range in size from 0 bytes to 0.5GB, allowing it to cache almost any datum.
    - title: Key-based access
      description: Data is stored and fetched from Valkey by key. Keybased access allows for extremely efficient access times, and this model maps naturally to caching. Valkey provides the customary GET and SET semantics for interacting with the data.
  screenshots:
    - /images/databases/nosql/valkey/screenshot-1.jpg
    - /images/databases/nosql/valkey/screenshot-2.jpg
---