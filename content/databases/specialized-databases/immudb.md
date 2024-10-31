---
draft: false
title: ImmuDB
content:
  id: immudb
  name: ImmuDB
  logo: /images/databases/specialized-databases/immudb/logo.png
  website: https://codenotary.com/technologies/immudb/
  iframe_website: /website-iframe/databases/specialized-databases/immudb
  dashboardImage: /images/databases/specialized-databases/immudb/screenshot-1.png
  short_description: immutable ledger database based on zero trust, SQL and Key-Value, tamperproof, data change history
  description: immudb is a immutable ledger database that has been developed with performance, scalability and versatility in mind. The user feedback has shown that they love the very high throughput and being able to store hashes as well as data. They see it as a great alternative to using a blockchain or ledger service.
  features:
    - title: Keep track of changes and audit them.
      description: Traditional database transactions and logs are hard to scale and are mutable, so there is no way to know for sure if your data has been compromised. immudb is immutable. You can add new versions of existing records, but never change or delete records. This lets you store critical data without fear of it being changed silently.
    - title: Verify your data without sacrificing performance
      description: Data stored in immudb is cryptographically coherent and verifiable, just like blockchains, but without all the complexity. Unlike blockchains, immudb can handle millions of transactions per second, and can be used both as a lightweight service or embedded in your application as a library.
    - title: Protect yourself from supply-chain attacks
      description: While Cyber Security is an important part of your organization’s business plan, immudb provides another layer of security to ensure data integrity even in the event your perimeter is breached during an attack. Data cannot be deleted or modified once stored into immudb. Additions of new data are logged and auditable, enabling you to view any suspect additions made during the intrusion.
    - title: KEY VALUE AND SQL
      description: immudb can be used as a tamper-proof key value store or SQL database, with audit history capabilities. Within single immudb instance a user can have multiple databases of both types, it is even possible to have KV and SQL withing single database.Key value is a foundation layer for SQL, meaning that SQL is using key value store capabilities underneath.
  screenshots:
    - /images/databases/specialized-databases/immudb/screenshot-1.png
    - /images/databases/specialized-databases/immudb/screenshot-2.jpeg
---