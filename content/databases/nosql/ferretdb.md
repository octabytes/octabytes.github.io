---
draft: false
title: FerretDB
content:
  id: ferretdb
  name: FerretDB
  logo: /images/databases/nosql/ferretdb/logo.png
  website: https://www.ferretdb.com/
  iframe_website: /website/databases/nosql/ferretdb
  dashboardImage: /images/databases/nosql/ferretdb/screenshot-1.png
  short_description: Documents DB, built on Postgres. FerretDB allows you to use MongoDB drivers seamlessly with PostgreSQL as the database backend. Use all tools, drivers, UIs, and the same query language and stay open-source.
  description: Documents DB built on Postgres. FerretDB allows you to use MongoDB drivers seamlessly with PostgreSQL as the database backend. Use all tools, drivers, UIs, and the same query language and stay open-source.
  features:
    - title: Solution
      description: The core of our solution is a stateless proxy, which converts MongoDB protocol queries to SQL, and uses PostgreSQL as a database engine. This will be compatible with MongoDB drivers and should work as a drop-in replacement to MongoDB in many cases.
    - title: CRUD operations
      description: CRUD (Create, Read, Update, and Delete) operations in FerretDB use the same protocol and drivers as MongoDB.
    - title: Operators
      description: It supports a complete list of operators, including query operators, update operators, aggregation operators, etc.
    - title: Query pushdown
      description: Initially, FerretDB retrieved all data related to queried collection, and applied filters on its own, making it possible to implement complex logic safely and quickly. and it minimizes the amount of incoming data, by applying the WHERE clause on SQL queries.
  screenshots:
    - /images/databases/nosql/ferretdb/screenshot-1.png
    - /images/databases/nosql/ferretdb/screenshot-2.png
---
