---
draft: false
title: "Fully managed open-source catalog | OctaByte.io"
layout: "services"

content:
  id: "all-services"
  title: "'All Service'"
  description: Deploy any one of over 350+ supported softwares on a VM in just few minutes. You can relax knowing that we are taking care of installation, configuration, encryption, backups, software & OS updates, live monitoring and more!
  service_categories:
    - name: Databases
      categories:
        - id: all
          name: All
        - id: relational-databases
          name: Relational databases
        - id: nosql
          name: NoSQL
        - id: specialized-databases
          name: Specialized Databases
    - name: Applications
      categories:
        - id: crm-erp
          name: CRM / ERP
        - id: note-taking
          name: Note-taking
        - id: project-management
          name: Project management
        - id: calendar
          name: Calendar
        - id: live-chat
          name: Live chat
        - id: invoicing-and-payments
          name: Invoicing and payments
        - id: documentation
          name: Documentation
        - id: search
          name: Search
        - id: email-marketing
          name: Email marketing
        - id: product-feedback
          name: Product Feedback
        - id: forum-community
          name: Forum / Community
        - id: business-intelligence
          name: Business Intelligence
        - id: password-manager
          name: Password manager
        - id: analytics
          name: Analytics
        - id: e-commerce
          name: E-commerce
        - id: cms
          name: CMS
        - id: customer-support
          name: Customer support
        - id: fediverse
          name: Fediverse
        - id: automation
          name: Automation
        - id: hcm
          name: HCM
        - id: cmms
          name: CMMS
        - id: hrms
          name: HRMS
    - name: Development
      categories:
        - id: identity-and-access-management
          name: Identity and access management
        - id: backend-as-a-service
          name: Backend-as-a-Service
        - id: dev-tools
          name: Dev tools
        - id: network
          name: Network
        - id: dev-ops
          name: devOps
        - id: nocode-lowcode
          name: No-code / Low code

    - name: Hosting and Infrastructure
      categories:
        - id: monitoring
          name: Monitoring
        - id: email
          name: Email
        - id: storage
          name: Storage
        - id: containers
          name: Containers
        - id: infrastructure
          name: Infrastructure

  services:
    - id: postgresql
      title: PostgreSQL
      image: /images/databases/relational-databases/postgresql/logo.png
      url: /databases/relational-databases/postgresql
      category: relational-databases
      description: PostgreSQL is a powerful, open-source object-relational database system, known for reliability, data integrity and performance.
    - id: mysql
      title: MySQL
      image: /images/databases/relational-databases/mysql/logo.png
      url: /databases/relational-databases/mysql
      category: relational-databases
      description: MySQL is an Oracle-backed open-source RDBMS that runs on almost all platforms.
    - id: mariadb
      title: MariaDB
      image: /images/databases/relational-databases/mariadb/logo.png
      url: /databases/relational-databases/mariadb
      category: relational-databases
      description: The open source relational database
    - id: columnstore
      title: ColumnStore
      image: /images/databases/relational-databases/columnstore/logo.png
      url: /databases/relational-databases/columnstore
      category: relational-databases
      description: MariaDB ColumnStore is a GPLv2 open-source columnar database built on MariaDB Server.
    - id: timescaledb
      title: TimescaleDB
      image: /images/databases/relational-databases/timescaledb/logo.png
      url: /databases/relational-databases/timescaledb
      category: relational-databases specialized-databases
      description: TimescaleDB is the leading open-source relational database with support for time-series data.
    - id: clickhouse
      title: ClickHouse
      image: /images/databases/relational-databases/clickhouse/logo.png
      url: /databases/relational-databases/clickhouse
      category: relational-databases specialized-databases
      description: ClickHouse is an open-source, column-oriented DBMS for online analytical processing.
    - id: clickhouses3
      title: ClickHouseS3
      image: /images/databases/relational-databases/clickhouses3/logo.png
      url: /databases/relational-databases/clickhouses3
      category: relational-databases specialized-databases
      description: ClickHouse + S3  is an open-source, column-oriented DBMS for online analytical processing.
    - id: mssql
      title: MSSQL
      image: /images/databases/relational-databases/mssql/logo.png
      url: /databases/relational-databases/mssql
      category: relational-databases
      description: SQL Server 2019 is a modern data platform designed to tackle the challenges of today's data professional.
    - id: hydra
      title: Hydra
      image: /images/databases/relational-databases/hydra/logo.png
      url: /databases/relational-databases/hydra
      category: relational-databases specialized-databases
      description: Hydra is an open-source alternative to enterprise data warehouses and it's simple, fast, and adaptable to your needs.
    - id: valkey
      title: Valkey
      image: /images/databases/nosql/valkey/logo.png
      url: /databases/nosql/valkey
      category: nosql specialized-databases
      description: A flexible distributed key-value datastore that supports both caching and beyond caching workloads.
    - id: redis
      title: Redis
      image: /images/databases/nosql/redis/logo.png
      url: /databases/nosql/redis
      category: nosql specialized-databases
      description: Redis is an open-source, in-memory database, cache and message broker.
    - id: scylladb
      title: ScyllaDB
      image: /images/databases/nosql/scylladb/logo.png
      url: /databases/nosql/scylladb
      category: nosql
      description: ScyllaDB is a true NoSQL database for the most demanding applications.
    - id: opensearch
      title: OpenSearch
      image: /images/databases/nosql/opensearch/logo.png
      url: /databases/nosql/opensearch
      category: nosql specialized-databases
      description: Open source distributed and RESTful search engine.
    - id: cassandra
      title: Cassandra
      image: /images/databases/nosql/cassandra/logo.png
      url: /databases/nosql/cassandra
      category: nosql
      description: Open Source NoSQL Database
    - id: ferretdb
      title: FerretDB
      image: /images/databases/nosql/ferretdb/logo.png
      url: /databases/nosql/ferretdb
      category: nosql
      description: Documents DB, built on Postgres. FerretDB allows you to use MongoDB drivers seamlessly with PostgreSQL as the database backend. Use all tools, drivers, UIs, and the same query language and stay open-source.
    - id: keydb
      title: KeyDB
      image: /images/databases/specialized-databases/keydb/logo.png
      url: /databases/specialized-databases/keydb
      category: specialized-databases
      description: KeyDB is both your cache and database, for cloud-optimized solutions.
    - id: influxdb
      title: InfluxDB
      image: /images/databases/specialized-databases/influxdb/logo.png
      url: /databases/specialized-databases/influxdb
      category: specialized-databases
      description: InfluxDB is a scalable datastore that empowers developers to build IoT, analytics and monitoring software.
    - id: surrealdb
      title: SurrealDB
      image: /images/databases/specialized-databases/surrealdb/logo.png
      url: /databases/specialized-databases/surrealdb
      category: specialized-databases
      description: A scalable, distributed, collaborative, document-graph database, for the realtime web.
    - id: chromadb
      title: Chromadb
      image: /images/databases/specialized-databases/chromadb/logo.png
      url: /databases/specialized-databases/chromadb
      category: specialized-databases
      description: The AI-native open-source embedding database
    - id: milvus
      title: Milvus
      image: /images/databases/specialized-databases/milvus/logo.png
      url: /databases/specialized-databases/milvus
      category: specialized-databases
      description: The High-Performance Vector Database Built for Scale
    - id: neo4j
      title: Neo4j
      image: /images/databases/specialized-databases/neo4j/logo.png
      url: /databases/specialized-databases/neo4j
      category: specialized-databases
      description: Neo4j is the world’s leading Graph Database
    - id: kafka
      title: Kafka
      image: /images/databases/specialized-databases/kafka/logo.png
      url: /databases/specialized-databases/kafka
      category: specialized-databases
      description: Apache Kafka is an open-source platform for high-performance data pipelines, streaming analytics, data integration and mission-critical applications.
    - id: m3db
      title: M3DB
      image: /images/databases/specialized-databases/m3db/logo.png
      url: /databases/specialized-databases/m3db
      category: specialized-databases
      description: M3 is a Prometheus compatible, easy to adopt metrics engine
    - id: immudb
      title: ImmuDB
      image: /images/databases/specialized-databases/immudb/logo.png
      url: /databases/specialized-databases/immudb
      category: specialized-databases
      description: immutable ledger database based on zero trust, SQL and Key-Value, tamperproof, data change history
    - id: weaviate
      title: Weaviate
      image: /images/databases/specialized-databases/weaviate/logo.png
      url: /databases/specialized-databases/weaviate
      category: specialized-databases
      description: Weaviate is an open-source vector database. It allows you to store data objects and vector embeddings from your favorite ML models, and scale seamlessly into billions of data objects.
    - id: cryptpad
      title: CryptPad
      image: /images/applications/crm-erp/cryptpad/logo.png
      url: /applications/crm-erp/cryptpad
      category: crm-erp
      description: CryptPad is a collaboration suite, encrypted and open-source.
    - id: dolibarr
      title: Dolibarr
      image: /images/applications/crm-erp/dolibarr/logo.png
      url: /applications/crm-erp/dolibarr
      category: crm-erp
      description: Dolibarr ERP CRM is a modern software package to manage your company or foundation's activity
    - id: attendize
      title: Attendize
      image: /images/applications/crm-erp/attendize/logo.png
      url: /applications/crm-erp/attendize
      category: crm-erp
      description: Attendize is a ticket-selling and event management platform.
    - id: pretix
      title: Pretix
      image: /images/applications/crm-erp/pretix/logo.png
      url: /applications/crm-erp/pretix
      category: crm-erp
      description: Ticket shop application for conferences, festivals, concerts, tech events, shows, exhibitions, workshops, bar camps, etc.
    - id: humhub
      title: HumHub
      image: /images/applications/crm-erp/humhub/logo.png
      url: /applications/crm-erp/humhub
      category: crm-erp forum-community
      description: HumHub to communicate and collaborate, share information, interact with all people in your organization, and personalize the software to fit your individual needs.
    - id: odoo
      title: Odoo ERP & CRM
      image: /images/applications/crm-erp/odoo/logo.png
      url: /applications/crm-erp/odoo
      category: crm-erp
      description: Odoo is a suite of web-based, open-source business apps.
    - id: erpnext
      title: ErpNext
      image: /images/applications/crm-erp/erpnext/logo.png
      url: /applications/crm-erp/erpnext
      category: crm-erp
      description: ERPNext is the leading open-source enterprise resource planning (ERP) software.
    - id: invoiceninja
      title: InvoiceNinja
      image: /images/applications/crm-erp/invoiceninja/logo.png
      url: /applications/crm-erp/invoiceninja
      category: crm-erp invoicing-and-payments
      description: Invoice Ninja is the leading free, open-source online invoicing app for freelancers and businesses.
    - id: suitecrm
      title: SuiteCRM
      image: /images/applications/crm-erp/suitecrm/logo.png
      url: /applications/crm-erp/suitecrm
      category: crm-erp
      description: SuiteCRM is an open source Customer Relationship Management (CRM) software solution that provides a 360-degree view of your customers and business.
    - id: chiefonboarding
      title: ChiefOnboarding
      image: /images/applications/crm-erp/chiefonboarding/logo.png
      url: /applications/crm-erp/chiefonboarding
      category: crm-erp
      description: Create entire blueprints of what your new hire will go through within minutes. Simply drag and drop items into the timeline.
    - id: espocrm
      title: EspoCRM
      image: /images/applications/crm-erp/espocrm/logo.png
      url: /applications/crm-erp/espocrm
      category: crm-erp
      description: EspoCRM is a web application that allows users to see, enter and evaluate all your company relationships regardless of the type.
    - id: twenty
      title: Twenty
      image: /images/applications/crm-erp/twenty/logo.png
      url: /applications/crm-erp/twenty
      category: crm-erp
      description: Open-source CRM, Building a modern alternative to Salesforce, powered by the community.
    - id: frappehr
      title: FrappeHR
      image: /images/applications/crm-erp/frappehr/logo.png
      url: /applications/crm-erp/frappehr
      category: crm-erp hrms
      description: Frappe HR (ERPNext HRMS) is a user-friendly solution designed to streamline HR and payroll operations, driving excellence within your team.
    - id: joplin
      title: Joplin
      image: /images/applications/note-taking/joplin/logo.png
      url: /applications/note-taking/joplin
      category: note-taking
      description: Joplin - an open source note taking and to-do application with synchronization capabilities for Windows, macOS, Linux, Android and iOS
    - id: vikunja
      title: Vikunja
      image: /images/applications/note-taking/vikunja/logo.png
      url: /applications/note-taking/vikunja
      category: note-taking
      description: The open-source to-do app. Organize everything, on all platforms.
    - id: cryptgeon
      title: Cryptgeon
      image: /images/applications/note-taking/cryptgeon/logo.png
      url: /applications/note-taking/cryptgeon
      category: note-taking
      description: Cryptgeon is a secure, open-source note / file-sharing service inspired by PrivNote written in rust & svelte.
    - id: docmost
      title: Docmost
      image: /images/applications/note-taking/docmost/logo.png
      url: /applications/note-taking/docmost
      category: note-taking
      description: Docmost is a collaborative wiki and documentation software. It is an open-source alternative to Confluence and Notion.
    - id: hedgedoc
      title: HedgeDoc
      image: /images/applications/note-taking/hedgedoc/logo.png
      url: /applications/note-taking/hedgedoc
      category: note-taking
      description: HedgeDoc is an open-source, web-based, self-hosted, collaborative markdown editor
    - id: etherpad
      title: Etherpad
      image: /images/applications/note-taking/etherpad/logo.png
      url: /applications/note-taking/etherpad
      category: note-taking
      description: Etherpad is a highly customizable open source online editor providing collaborative editing in really real-time.
    - id: trilium
      title: Trilium
      image: /images/applications/note-taking/trilium/logo.png
      url: /applications/note-taking/trilium
      category: note-taking
      description: Trilium Notes is a hierarchical note taking application with focus on building large personal knowledge bases.
    - id: affine
      title: Affine
      image: /images/applications/note-taking/affine/logo.png
      url: /applications/note-taking/affine
      category: note-taking
      description: More than Notion and Miro's next-generation knowledge base, AFFiNE unifies planning, sorting, and creation.
    - id: memos
      title: Memos
      image: /images/applications/note-taking/memos/logo.png
      url: /applications/note-taking/memos
      category: note-taking
      description: A lightweight, self-hosted memo hub. Open Source and Free forever.
    - id: flatnotes
      title: Flatnotes
      image: /images/applications/note-taking/flatnotes/logo.png
      url: /applications/note-taking/flatnotes
      category: note-taking
      description: A self-hosted, database-less note-taking web app that utilizes a flat folder of markdown files for storage.
    - id: huly
      title: Huly
      image: /images/applications/note-taking/huly/logo.png
      url: /applications/note-taking/huly
      category: note-taking project-management
      description: All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion)
    - id: plane
      title: Plane
      image: /images/applications/project-management/plane/logo.png
      url: /applications/project-management/plane
      category: project-management
      description: An open-source software development tool to manage issues, sprints, and product roadmaps with peace of mind
    - id: leantime
      title: Leantime
      image: /images/applications/project-management/leantime/logo.png
      url: /applications/project-management/leantime
      category: project-management
      description: Leantime is a strategic project management system for non-project managers.
    - id: openproject
      title: OpenProject
      image: /images/applications/project-management/openproject/logo.png
      url: /applications/project-management/openproject
      category: project-management
      description: OpenProject is a web-based project management system for location-independent team collaboration.
    - id: taiga
      title: Taiga
      image: /images/applications/project-management/taiga/logo.png
      url: /applications/project-management/taiga
      category: project-management
      description: Your Agile, Free and Open Source Project Management Tool
    - id: focalboard
      title: FocalBoard
      image: /images/applications/project-management/focalboard/logo.png
      url: /applications/project-management/focalboard
      category: project-management
      description: Project & Task Management for Software Development Teams
    - id: wekan
      title: Wekan
      image: /images/applications/project-management/wekan/logo.png
      url: /applications/project-management/wekan
      category: project-management
      description: Experience efficient task management with WeKan - the Open-Source, customizable, and privacy-focused Kanban.
    - id: siglens
      title: SigLens
      image: /images/applications/project-management/siglens/logo.png
      url: /applications/project-management/siglens
      category: project-management
      description: 100x Efficient Log Management than Splunk 🚀 Reduce your observability cost by 90%
    - id: kanboard
      title: Kanboard
      image: /images/applications/project-management/kanboard/logo.png
      url: /applications/project-management/kanboard
      category: project-management
      description: Kanban project management software
    - id: easyappointments
      title: EasyAppointments
      image: /images/applications/calendar/easyappointments/logo.png
      url: /applications/calendar/easyappointments
      category: calendar
      description: Open Source Appointment Scheduler that allows customers to book appointments with you
    - id: rallly
      title: Rallly
      image: /images/applications/calendar/rallly/logo.png
      url: /applications/calendar/rallly
      category: calendar
      description: Rallly is the Doodle alternative scheduling and collaboration tool designed to make organizing events and meetings easier.
    - id: cal
      title: Cal
      image: /images/applications/calendar/cal/logo.png
      url: /applications/calendar/cal
      category: calendar
      description: Calendly alternative Cal.com, is the event-juggling scheduler for everyone. Focus on meetings, not making meetings. Free for individuals.
    - id: lobechat
      title: LobeChat
      image: /images/applications/live-chat/lobechat/logo.png
      url: /applications/live-chat/lobechat
      category: live-chat
      description: An open-source, high-performance chatbot framework. Support one-click free deployment of your private ChatGPT/Gemini/LLM application.
    - id: chatwoot
      title: Chatwoot
      image: /images/applications/live-chat/chatwoot/logo.png
      url: /applications/live-chat/chatwoot
      category: live-chat
      description: Chatwoot is an open-source, alternative customer engagement suite.
    - id: mattermost
      title: Mattermost Team Edition
      image: /images/applications/live-chat/mattermost/logo.png
      url: /applications/live-chat/mattermost
      category: live-chat
      description: Mattermost is an open-source platform for secure collaboration across the entire software development lifecycle.
    - id: rocket.chat
      title: Rocket.Chat
      image: /images/applications/live-chat/rocket.chat/logo.png
      url: /applications/live-chat/rocket.chat
      category: live-chat
      description: Rocket.Chat is an open-source communications platform for organizations with high standards of data protection.
    - id: papercups
      title: Papercups
      image: /images/applications/live-chat/papercups/logo.png
      url: /applications/live-chat/papercups
      category: live-chat customer-support
      description: Papercups is a open-source live customer chat
    - id: revolt
      title: Revolt
      image: /images/applications/live-chat/revolt/logo.png
      url: /applications/live-chat/revolt
      category: live-chat
      description: The Open Source Discord Alternative. Find your community, connect with the world
    - id: jitsi
      title: Jitsi
      image: /images/applications/live-chat/jitsi/logo.png
      url: /applications/live-chat/jitsi
      category: live-chat
      description: Jitsi is a set of open-source projects that allows you to easily build and deploy secure video conferencing solutions.
    - id: zulip
      title: Zulip
      image: /images/applications/live-chat/zulip/logo.png
      url: /applications/live-chat/zulip
      category: live-chat
      description: Zulip is a team collaboration tool with unique topic-based threading that combines the best of email and chat to make remote work productive and delightful.
    - id: typebot
      title: Typebot
      image: /images/applications/live-chat/typebot/logo.png
      url: /applications/live-chat/typebot
      category: live-chat customer-support
      description: Typebot gives you powerful blocks to create unique chat experiences. Embed them anywhere on your web/mobile apps and start collecting results like magic
    - id: mirotalk
      title: MiroTalk
      image: /images/applications/live-chat/mirotalk/logo.png
      url: /applications/live-chat/mirotalk
      category: live-chat
      description: WebRTC - P2P - Simple, Secure, Fast Real-Time Video Conferences Up to 4k and 60fps, compatible with all browsers and platforms.
    - id: botpress
      title: Botpress
      image: /images/applications/live-chat/botpress/logo.png
      url: /applications/live-chat/botpress
      category: live-chat customer-support
      description: The first next-generation chatbot builder powered by OpenAI. Build ChatGPT-like bots for your project or business to get things done.
    - id: bigcapital
      title: Bigcapital
      image: /images/applications/invoicing-and-payments/bigcapital/logo.png
      url: /applications/invoicing-and-payments/bigcapital
      category: invoicing-and-payments
      description: Bigcapital is financial accounting with intelligent reporting for faster decision-making, an open-source alternative to Quickbooks, Xero, etc.
    - id: lago
      title: Lago
      image: /images/applications/invoicing-and-payments/lago/logo.png
      url: /applications/invoicing-and-payments/lago
      category: invoicing-and-payments
      description: Open-source alternative to Stripe Billing and Chargebee it offers a modular architecture for metering and usage-based billing, at every stage of your company.
    - id: crater
      title: Crater
      image: /images/applications/invoicing-and-payments/crater/logo.png
      url: /applications/invoicing-and-payments/crater
      category: invoicing-and-payments
      description: Crater helps you track expenses, and payments & create professional invoices & estimates.
    - id: btcpay
      title: BTCPay
      image: /images/applications/invoicing-and-payments/btcpay/logo.png
      url: /applications/invoicing-and-payments/btcpay
      category: invoicing-and-payments e-commerce
      description: Start Accepting Bitcoin Payments With 0% Fees & No Third-party
    - id: hyperswitch
      title: Hyperswitch
      image: /images/applications/invoicing-and-payments/hyperswitch/logo.png
      url: /applications/invoicing-and-payments/hyperswitch
      category: invoicing-and-payments
      description: An open-source payments switch written in Rust to make payments fast, reliable, and affordable.
    - id: cells
      title: Cells
      image: /images/applications/documentation/cells/logo.png
      url: /applications/documentation/cells
      category: documentation cms
      description: Pydio Cells is the Document Sharing, Management, and Collaboration platform.
    - id: papermerge
      title: Papermerge
      image: /images/applications/documentation/papermerge/logo.png
      url: /applications/documentation/papermerge
      category: documentation
      description: Open Source Document Management System for Digital Archives (Scanned Documents)
    - id: wikijs
      title: Wikijs
      image: /images/applications/documentation/wikijs/logo.png
      url: /applications/documentation/wikijs
      category: documentation
      description: Wikijs is a powerful open-source wiki app built on Node.js, Git and Markdown.
    - id: outline
      title: Outline
      image: /images/applications/documentation/outline/logo.png
      url: /applications/documentation/outline
      category: documentation
      description: Outline is a fast wiki and knowledge base for growing teams - an alternative to Google Docs.
    - id: bookstack
      title: BookStack
      image: /images/applications/documentation/bookstack/logo.png
      url: /applications/documentation/bookstack
      category: documentation
      description: BookStack is a platform to create documentation/wiki content built with PHP & Laravel.
    - id: documize
      title: Documize
      image: /images/applications/documentation/documize/logo.png
      url: /applications/documentation/documize
      category: documentation
      description: Free Knowledge Management Software
    - id: docuseal
      title: DocuSeal
      image: /images/applications/documentation/docuseal/logo.png
      url: /applications/documentation/docuseal
      category: documentation
      description: Open source, tool to streamline document filling and signing. Create custom PDF forms to complete and sign with an easy-to-use online tool.
    - id: documenso
      title: Documenso
      image: /images/applications/documentation/documenso/logo.png
      url: /applications/documentation/documenso
      category: documentation
      description: The Open Source DocuSign Alternative, Document signing.
    - id: answer
      title: Answer
      image: /images/applications/documentation/answer/logo.png
      url: /applications/documentation/answer
      category: documentation forum-community
      description: An open-source knowledge-based community software. You can use it quickly to build Q&A community for your products, customers, teams, and more.
    - id: ollama
      title: Ollama
      image: /images/applications/search/ollama/logo.png
      url: /applications/search/ollama
      category: search
      description: ChatGPT-Style Open Web UI Client for LLMs (Formerly Ollama WebUI) to Get up and running with Llama 2, Mistral, and other large language models.
    - id: searxng
      title: SearXNG
      image: /images/applications/search/searxng/logo.png
      url: /applications/search/searxng
      category: search
      description: SearXNG is a free internet metasearch engine which aggregates results from various search services and databases. Users are neither tracked nor profiled.
    - id: serpbear
      title: SerpBear
      image: /images/applications/search/serpbear/logo.png
      url: /applications/search/serpbear
      category: search
      description: SerpBear is an Open Source Search Engine Position Tracking App. It allows you to track your website's keyword positions in Google and get notified of their positions.
    - id: meilisearch
      title: Meilisearch
      image: /images/applications/search/meilisearch/logo.png
      url: /applications/search/meilisearch
      category: search
      description: Meilisearch is a next-generation search API.
    - id: typesense
      title: Typesense
      image: /images/applications/search/typesense/logo.png
      url: /applications/search/typesense
      category: search
      description: Typesense is a fast, typo-tolerant, fuzzy search engine for building great search experiences.
    - id: solr
      title: Solr
      image: /images/applications/search/solr/logo.png
      url: /applications/search/solr
      category: search
      description: Apache Solr is the popular, blazing fast open source search platform for all your enterprise, e-commerce, and analytics needs, built on Apache Lucene.
    - id: manticoresearch
      title: ManticoreSearch
      image: /images/applications/search/manticoresearch/logo.png
      url: /applications/search/manticoresearch
      category: search
      description: Manticore Search is an easy to use open source fast database for search. Modern, fast, light-weight, outstanding full-text search capabilities.
    - id: zincsearch
      title: ZincSearch
      image: /images/applications/search/zincsearch/logo.png
      url: /applications/search/zincsearch
      category: search
      description: ZincSearch is a search engine that does full text indexing. It is a lightweight alternative to Elasticsearch and runs using a fraction of the resources.
    - id: mautic
      title: Mautic
      image: /images/applications/email-marketing/mautic/logo.png
      url: /applications/email-marketing/mautic
      category: email-marketing automation
      description: Mautic is a open source marketing automation software.
    - id: listmonk
      title: Listmonk
      image: /images/applications/email-marketing/listmonk/logo.png
      url: /applications/email-marketing/listmonk
      category: email-marketing
      description: Listmonk is a self-hosted, high performance mailing list and newsletter manager
    - id: limesurvey
      title: LimeSurvey
      image: /images/applications/product-feedback/limesurvey/logo.png
      url: /applications/product-feedback/limesurvey
      category: product-feedback
      description: LimeSurvey is the most popular FOSS online survey tool on the web.
    - id: fider
      title: Fider
      image: /images/applications/product-feedback/fider/logo.png
      url: /applications/product-feedback/fider
      category: product-feedback customer-support
      description: Customer Feedback Made Easy
    - id: nodebb
      title: NodeBB
      image: /images/applications/forum-community/nodebb/logo.png
      url: /applications/forum-community/nodebb
      category: forum-community
      description: NodeBB is next-generation forum software - powerful, mobile-ready and easy to use.
    - id: discourse
      title: Discourse
      image: /images/applications/forum-community/discourse/logo.png
      url: /applications/forum-community/discourse
      category: forum-community
      description: Discourse is an open-source discussion platform built for the next decade of the Internet.
    - id: photon
      title: Photon
      image: /images/applications/forum-community/photon/logo.png
      url: /applications/forum-community/photon
      category: forum-community fediverse
      description: A replacement for Lemmy-ui with more features, a better design, and more customizability. It includes Photon UI + Lemmy
    - id: azuracast
      title: AzuraCast
      image: /images/applications/forum-community/azuracast/logo.png
      url: /applications/forum-community/azuracast
      category: forum-community
      description: A self-hosted web radio management suite
    - id: mastodon
      title: Mastodon
      image: /images/applications/forum-community/mastodon/logo.png
      url: /applications/forum-community/mastodon
      category: forum-community fediverse
      description: Mastodon is a free fediverse, open-source social network server with OpenSearch for indexing.
    - id: flarum
      title: Flarum
      image: /images/applications/forum-community/flarum/logo.png
      url: /applications/forum-community/flarum
      category: forum-community
      description: Flarum is a delightfully simple discussion platform for your website
    - id: element
      title: Element
      image: /images/applications/forum-community/element/logo.png
      url: /applications/forum-community/element
      category: forum-community fediverse
      description: Create your community based on Matrix protocol
    - id: owncast
      title: Owncast
      image: /images/applications/forum-community/owncast/logo.png
      url: /applications/forum-community/owncast
      category: forum-community fediverse
      description: Owncast is a free and open source live video and web chat server for use with existing popular broadcasting software.
    - id: picoshare
      title: Picoshare
      image: /images/applications/forum-community/picoshare/logo.png
      url: /applications/forum-community/picoshare
      category: forum-community
      description: PicoShare is a service for sharing images, videos, and other files.
    - id: friendica
      title: Friendica
      image: /images/applications/forum-community/friendica/logo.png
      url: /applications/forum-community/friendica
      category: forum-community fediverse
      description: A Decentralized Social Network, you can use to host your own social media server that forms one part of the fediverse, an interconnected and decentralized network of independently operated servers
    - id: lemmy
      title: Lemmy
      image: /images/applications/forum-community/lemmy/logo.png
      url: /applications/forum-community/lemmy
      category: forum-community fediverse
      description: Open-source Reddit alternative. Create your own discussion platform with Lemmy
    - id: kbin
      title: KBIN
      image: /images/applications/forum-community/kbin/logo.png
      url: /applications/forum-community/kbin
      category: forum-community fediverse
      description: A reddit-like content aggregator and micro-blogging platform for the fediverse.
    - id: lobsters
      title: Lobsters
      image: /images/applications/forum-community/lobsters/logo.png
      url: /applications/forum-community/lobsters
      category: forum-community
      description: Lobsters is a community dedicated to computing, where members gather to share links and engage in discussions.
    - id: phpbb
      title: PhpBB
      image: /images/applications/forum-community/phpbb/logo.png
      url: /applications/forum-community/phpbb
      category: forum-community
      description: phpBB is a free flat-forum bulletin board software solution that can be used to stay in touch with a group of people or can power your entire website.
    - id: countly
      title: Countly
      image: /images/applications/business-intelligence/countly/logo.png
      url: /applications/business-intelligence/countly
      category: business-intelligence
      description: Countly is a product analytics platform that helps teams track, analyze, and act on their user actions and behavior on mobile, web, and desktop applications.
    - id: metabase
      title: Metabase
      image: /images/applications/business-intelligence/metabase/logo.png
      url: /applications/business-intelligence/metabase
      category: business-intelligence
      description: Metabase is an open-source tool that simply and quickly gathers business intelligence and analytics for your company.
    - id: metabasepostgres
      title: MetabasePostgres
      image: /images/applications/business-intelligence/metabasepostgres/logo.png
      url: /applications/business-intelligence/metabasepostgres
      category: business-intelligence
      description: Metabase is an open-source tool that simply and quickly gathers business intelligence and analytics for your company.
    - id: lightdash
      title: Lightdash
      image: /images/applications/business-intelligence/lightdash/logo.png
      url: /applications/business-intelligence/lightdash
      category: business-intelligence
      description: Lighdash an open source alternative to Looker built using dbt.
    - id: superset
      title: Superset
      image: /images/applications/business-intelligence/superset/logo.png
      url: /applications/business-intelligence/superset
      category: business-intelligence
      description: Apache Superset is a data visualization and data exploration platform.
    - id: vaultwarden
      title: Vaultwarden
      image: /images/applications/password-manager/vaultwarden/logo.png
      url: /applications/password-manager/vaultwarden
      category: password-manager
      description: Vaultwarden is an open-source password management application that can be self-hosted and run on your infrastructure.
    - id: password
      title: Password Pusher
      image: /images/applications/password-manager/password/logo.png
      url: /applications/password-manager/password
      category: password-manager
      description: An application to communicate passwords over the web. Links to passwords expire after a certain number of views and/or time has passed.
    - id: passit
      title: Passit
      image: /images/applications/password-manager/passit/logo.png
      url: /applications/password-manager/passit
      category: password-manager
      description: Password manager to use on any device with a web browser to secure your digital life.
    - id: keeweb
      title: KeeWeb
      image: /images/applications/password-manager/keeweb/logo.png
      url: /applications/password-manager/keeweb
      category: password-manager
      description: KeeWeb is a free, open-source password manager, available as a web version and as a desktop app.
    - id: yopass
      title: Yopass
      image: /images/applications/password-manager/yopass/logo.png
      url: /applications/password-manager/yopass
      category: password-manager
      description: Yopass encryption mechanisms are built on open-source software meaning full transparency with the possibility to audit and submit features.
    - id: infisical
      title: Infisical
      image: /images/applications/password-manager/infisical/logo.png
      url: /applications/password-manager/infisical
      category: password-manager
      description: "Infisical is an open-source, end-to-end encrypted platform for secret management: sync secrets across your team/infrastructure and prevents secret leaks."
    - id: vault
      title: Vault
      image: /images/applications/password-manager/vault/logo.png
      url: /applications/password-manager/vault
      category: password-manager
      description: Vault is a tool for secrets management, encryption as a service, and privileged access management
    - id: umami
      title: Umami
      image: /images/applications/analytics/umami/logo.png
      url: /applications/analytics/umami
      category: analytics
      description: Umami is a simple, fast, website analytics alternative to Google Analytics.
    - id: matomo
      title: Matomo
      image: /images/applications/analytics/matomo/logo.png
      url: /applications/analytics/matomo
      category: analytics
      description: Matomo is a full-featured PHP MySQL software program that you download and install on your own webserver
    - id: fugu
      title: Fugu
      image: /images/applications/analytics/fugu/logo.png
      url: /applications/analytics/fugu
      category: analytics
      description: Fugu is a product analytics software with a strong focus on simplicity and privacy-friendliness.
    - id: posthog
      title: PostHog
      image: /images/applications/analytics/posthog/logo.png
      url: /applications/analytics/posthog
      category: analytics
      description: PostHog provides open-source product analytics, session recording, feature flagging and a/b testing that you can self-host.
    - id: dremio
      title: Dremio
      image: /images/applications/analytics/dremio/logo.png
      url: /applications/analytics/dremio
      category: analytics
      description: The Easy and Open Data Lakehouse Self-service analytics with data warehouse functionality and data lake flexibility across all your data.
    - id: tika
      title: Tika
      image: /images/applications/analytics/tika/logo.png
      url: /applications/analytics/tika
      category: analytics
      description: Apache Tika a content analysis toolkit detects and extracts metadata and text from over a thousand different file types (such as PPT, XLS, and PDF).
    - id: knime
      title: Knime
      image: /images/applications/analytics/knime/logo.png
      url: /applications/analytics/knime
      category: analytics
      description: KNIME Analytics Platform
    - id: quickwit
      title: Quickwit
      image: /images/applications/analytics/quickwit/logo.png
      url: /applications/analytics/quickwit
      category: analytics
      description: Cloud-native search engine for observability. An open-source alternative to Datadog, Elasticsearch, Loki, and Tempo.
    - id: ackee
      title: Ackee
      image: /images/applications/analytics/ackee/logo.png
      url: /applications/analytics/ackee
      category: analytics
      description: Ackee is a self-hosted, Node.js-based analytics tool for ensuring privacy.
    - id: prestashop
      title: Prestashop
      image: /images/applications/e-commerce/prestashop/logo.png
      url: /applications/e-commerce/prestashop
      category: e-commerce
      description: The PrestaShop project is a universal open-source software platform to build your e-commerce solution.
    - id: magento
      title: Magento
      image: /images/applications/e-commerce/magento/logo.png
      url: /applications/e-commerce/magento
      category: e-commerce
      description: Magento open-source software delivers basic e-commerce capabilities that allow you to build a unique online store from the ground up.
    - id: nopcommerce
      title: nopCommerce
      image: /images/applications/e-commerce/nopcommerce/logo.png
      url: /applications/e-commerce/nopcommerce
      category: e-commerce
      description: nopCommerce is the most popular ASP.NET shopping cart in the world based on Microsoft technologies. Free and open-source eCommerce platform.
    - id: shopware
      title: Shopware
      image: /images/applications/e-commerce/shopware/logo.png
      url: /applications/e-commerce/shopware
      category: e-commerce
      description: Shopware is a modern eCommerce platform connecting enterprise-level capabilities with flexibility
    - id: woocommerce
      title: WooCommerce
      image: /images/applications/e-commerce/woocommerce/logo.png
      url: /applications/e-commerce/woocommerce
      category: e-commerce
      description: WooCommerce is a customizable, open-source eCommerce platform built on WordPress.
    - id: wordpress-multisites
      title: Wordpress-Multisites
      image: /images/applications/cms/wordpress-multisites/logo.png
      url: /applications/cms/wordpress-multisites
      category: cms
      description: WordPress Multisite is a version of WordPress that allows you to run multiple sites off a single installation of WordPress.
    - id: wordpress
      title: Wordpress
      image: /images/applications/cms/wordpress/logo.png
      url: /applications/cms/wordpress
      category: cms
      description: WordPress is open-source software you can use to create a beautiful website, blog or app.
    - id: ghost
      title: Ghost
      image: /images/applications/cms/ghost/logo.png
      url: /applications/cms/ghost
      category: cms
      description: Ghost is a powerful app for new-media creators to publish, share, and grow a business around their content.
    - id: drupal
      title: Drupal
      image: /images/applications/cms/drupal/logo.png
      url: /applications/cms/drupal
      category: cms
      description: Drupal is an open-source content management platform that supports a wide variety of websites.
    - id: joomla
      title: Joomla
      image: /images/applications/cms/joomla/logo.png
      url: /applications/cms/joomla
      category: cms
      description: Joomla is an award-winning content management system for building websites and powerful online applications.
    - id: firefish
      title: Firefish
      image: /images/applications/cms/firefish/logo.png
      url: /applications/cms/firefish
      category: cms
      description: Firefish is based off of Misskey, a powerful microblogging social media platform in the fediverse.
    - id: mediacms
      title: MediaCMS
      image: /images/applications/cms/mediacms/logo.png
      url: /applications/cms/mediacms
      category: cms
      description: MediaCMS is a fully featured open-source video and media CMS.
    - id: agencyos
      title: AgencyOS
      image: /images/applications/cms/agencyos/logo.png
      url: /applications/cms/agencyos
      category: cms
      description: Open source operating system for digital agencies. Built with Directus and Nuxt.
    - id: directus
      title: Directus
      image: /images/applications/cms/directus/logo.png
      url: /applications/cms/directus
      category: cms
      description: Directus is an Open Data Platform for managing the content of any SQL database.
    - id: strapi
      title: Strapi
      image: /images/applications/cms/strapi/logo.png
      url: /applications/cms/strapi
      category: cms
      description: Strapi enables easy building of self-hosted, customizable, performant content API.
    - id: freescout
      title: FreeScout
      image: /images/applications/customer-support/freescout/logo.png
      url: /applications/customer-support/freescout
      category: customer-support
      description: FreeScout is a free self-hosted help desk & shared mailbox.
    - id: formbricks
      title: Formbricks
      image: /images/applications/customer-support/formbricks/logo.png
      url: /applications/customer-support/formbricks
      category: customer-support
      description: Formbricks is your go-to solution for in-product micro-surveys that will supercharge your product experience.
    - id: dittofeed
      title: Dittofeed
      image: /images/applications/customer-support/dittofeed/logo.png
      url: /applications/customer-support/dittofeed
      category: customer-support
      description: Automate communications with customers. Give data control to your growth engineers.
    - id: glpi
      title: GLPI
      image: /images/applications/customer-support/glpi/logo.png
      url: /applications/customer-support/glpi
      category: customer-support
      description: GLPI is a Free Asset and IT Management Software package, Data center management, ITIL Service Desk, licenses tracking and software auditing.
    - id: zammad
      title: Zammad
      image: /images/applications/customer-support/zammad/logo.png
      url: /applications/customer-support/zammad
      category: customer-support
      description: Zammad is a web-based, open-source helpdesk/customer support system.
    - id: trudesk
      title: Trudesk
      image: /images/applications/customer-support/trudesk/logo.png
      url: /applications/customer-support/trudesk
      category: customer-support
      description: Trudesk is an open-source help desk/ticketing solution.
    - id: mantisbt
      title: MantisBT
      image: /images/applications/customer-support/mantisbt/logo.png
      url: /applications/customer-support/mantisbt
      category: customer-support
      description: MantisBT makes collaboration with team members & clients easy, fast, and professional
    - id: tracardi
      title: Tracardi
      image: /images/applications/customer-support/tracardi/logo.png
      url: /applications/customer-support/tracardi
      category: customer-support
      description: TRACARDI is a new HOME for your customer data. TRACARDI is an API-first solution, a low-code / no-code platform aimed at any e-commerce business that wants to start using user data for marketing purposes.
    - id: pixelfed
      title: Pixelfed
      image: /images/applications/fediverse/pixelfed/logo.png
      url: /applications/fediverse/pixelfed
      category: fediverse
      description: Pixelfed is a fediverse decentralized social network for image sharing. Unlike other platforms with features similar to those of the social network Instagram.
    - id: pleroma
      title: Pleroma
      image: /images/applications/fediverse/pleroma/logo.png
      url: /applications/fediverse/pleroma
      category: fediverse
      description: A microblogging server software that can federate other servers that support ActivityPub. it will federate with all servers like Friendica, GNU Social, Hubzilla, Mastodon, Misskey, Peertube, and Pixelfed.
    - id: misskey
      title: Misskey
      image: /images/applications/fediverse/misskey/logo.png
      url: /applications/fediverse/misskey
      category: fediverse
      description: Misskey is an open-source microblogging, federated social media platform that's free forever!
    - id: sharkey
      title: Sharkey
      image: /images/applications/fediverse/sharkey/logo.png
      url: /applications/fediverse/sharkey
      category: fediverse
      description: Sharkey is an open source, decentralized social media platform that's free forever!
    - id: peertube
      title: PeerTube
      image: /images/applications/fediverse/peertube/logo.png
      url: /applications/fediverse/peertube
      category: fediverse
      description: Free software to take back control of your videos for the Fediverse
    - id: castopod
      title: Castopod
      image: /images/applications/fediverse/castopod/logo.png
      url: /applications/fediverse/castopod
      category: fediverse
      description: Self-host your podcasts with ease, keep control over what you create, and talk to your audience without any middleman. Your podcast and your audience belong to you and you only.
    - id: activepieces
      title: Activepieces
      image: /images/applications/automation/activepieces/logo.png
      url: /applications/automation/activepieces
      category: automation
      description: Activepieces is an open source alternative to Zapier, Make.com and Tray.io. Automate your work with our builder and connectors - host it on your machine.
    - id: automatisch
      title: Automatisch
      image: /images/applications/automation/automatisch/logo.png
      url: /applications/automation/automatisch
      category: automation
      description: Automatisch helps you to automate your business processes without coding. Use our affordable cloud solution or self-host on your own servers.
    - id: node-red
      title: Node-red
      image: /images/applications/automation/node-red/logo.png
      url: /applications/automation/node-red
      category: automation
      description: Node-RED is a low-code programming environment for event-driven applications.
    - id: apachenifi
      title: ApacheNiFi
      image: /images/applications/automation/apachenifi/logo.png
      url: /applications/automation/apachenifi
      category: automation
      description: Apache NiFi automates the movement of data between disparate data sources and systems, making data ingestion fast, easy, and secure.
    - id: n8n
      title: N8N
      image: /images/applications/automation/n8n/logo.png
      url: /applications/automation/n8n
      category: automation
      description: n8n is a free, self-hosted workflow automation tool that integrates with other apps to automate processes between them.
    - id: huginn
      title: Huginn
      image: /images/applications/automation/huginn/logo.png
      url: /applications/automation/huginn
      category: automation
      description: Huginn is a tool in the Web Service Automation category of a tech stack.
    - id: airflow
      title: Airflow
      image: /images/applications/automation/airflow/logo.png
      url: /applications/automation/airflow
      category: automation
      description: Apache Airflow is a platform created by the community to programmatically author, schedule and monitor workflows.
    - id: airflow-worker
      title: Airflow-worker
      image: /images/applications/automation/airflow-worker/logo.png
      url: /applications/automation/airflow-worker
      category: automation
      description: Apache Airflow is a platform created by the community to programmatically author, schedule and monitor workflows.
    - id: minthcm
      title: MintHCM
      image: /images/applications/hcm/minthcm/logo.png
      url: /applications/hcm/minthcm
      category: hcm
      description: Human Capital Management system (HCM) that you can start using today to manage your HR departments and businesses in different branches.
    - id: logto
      title: Logto
      image: /images/development/identity-and-access-management/logto/logo.png
      url: /development/identity-and-access-management/logto
      category: identity-and-access-management
      description: Logto is an Auth0 alternative for building modern customer identity infrastructure with minimal effort, for both your customers and their organizations.
    - id: lightldap
      title: LightLDAP
      image: /images/development/identity-and-access-management/lightldap/logo.png
      url: /development/identity-and-access-management/lightldap
      category: identity-and-access-management
      description: A Lightweight authentication server that provides an opinionated, simplified LDAP interface for authentication. It integrates with many backends, from KeyCloak to Authelia to Nextcloud and more!
    - id: authelia
      title: Authelia
      image: /images/development/identity-and-access-management/authelia/logo.png
      url: /development/identity-and-access-management/authelia
      category: identity-and-access-management
      description: Authelia is an authentication and authorization server and portal fulfilling the identity and access management (IAM) role of information security in providing multi-factor authentication and single sign-on (SSO) for your applications via a web portal. It
    - id: keycloak
      title: Keycloak
      image: /images/development/identity-and-access-management/keycloak/logo.png
      url: /development/identity-and-access-management/keycloak
      category: identity-and-access-management
      description: Keycloak is an open-source identity and access management solution aimed at modern applications and services.
    - id: authentik
      title: Authentik
      image: /images/development/identity-and-access-management/authentik/logo.png
      url: /development/identity-and-access-management/authentik
      category: identity-and-access-management
      description: authentik is a flexible, versatile open-source identity provider.
    - id: zitadel
      title: Zitadel
      image: /images/development/identity-and-access-management/zitadel/logo.png
      url: /development/identity-and-access-management/zitadel
      category: identity-and-access-management
      description: Zitadel is a cloud-native Identity & Access Management platform built for the cloud era.
    - id: agencyos
      title: AgencyOS
      image: /images/development/backend-as-a-service/agencyos/logo.png
      url: /development/backend-as-a-service/agencyos
      category: backend-as-a-service nocode-lowcode
      description: Open source operating system for digital agencies. Built with Directus and Nuxt.
    - id: directus
      title: Directus
      image: /images/development/backend-as-a-service/directus/logo.png
      url: /development/backend-as-a-service/directus
      category: backend-as-a-service nocode-lowcode
      description: Directus is an Open Data Platform for managing the content of any SQL database.
    - id: strapi
      title: Strapi
      image: /images/development/backend-as-a-service/strapi/logo.png
      url: /development/backend-as-a-service/strapi
      category: backend-as-a-service
      description: Strapi enables easy building of self-hosted, customizable, performant content API.
    - id: appwrite
      title: Appwrite
      image: /images/development/backend-as-a-service/appwrite/logo.png
      url: /development/backend-as-a-service/appwrite
      category: backend-as-a-service nocode-lowcode
      description: Appwrite provides developers with a set of REST APIs to manage their core backend needs.
    - id: parse
      title: Parse
      image: /images/development/backend-as-a-service/parse/logo.png
      url: /development/backend-as-a-service/parse
      category: backend-as-a-service
      description: Parse Server is an open-source backend that can be deployed to any infrastructure that can run Node.js.
    - id: supabase
      title: Supabase
      image: /images/development/backend-as-a-service/supabase/logo.png
      url: /development/backend-as-a-service/supabase
      category: backend-as-a-service
      description: Supabase is an open source alternative to Firebase.
    - id: pocketbase
      title: PocketBase
      image: /images/development/backend-as-a-service/pocketbase/logo.png
      url: /development/backend-as-a-service/pocketbase
      category: backend-as-a-service
      description: Open Source backend for your next SaaS and Mobile app in 1 file
    - id: jellyfin
      title: Jellyfin
      image: /images/development/dev-tools/jellyfin/logo.png
      url: /development/dev-tools/jellyfin
      category: dev-tools
      description: Free Software Media System that puts you in control of managing and streaming your media alternative to the proprietary Emby and Plex.
    - id: opnform
      title: OpnForm
      image: /images/development/dev-tools/opnform/logo.png
      url: /development/dev-tools/opnform
      category: dev-tools
      description: Form Builder, Create beautiful forms and share them anywhere. It is super fast, you don't need to know how to code. It's an alternative to products like Typeform, JotForm, Tally, etc
    - id: corteza
      title: Corteza
      image: /images/development/dev-tools/corteza/logo.png
      url: /development/dev-tools/corteza
      category: dev-tools
      description: A low-code platform alternative to Salesforce lets you build and iterate CRM, business processes and other structured data apps fast, create intelligent business process workflows, and connect with almost any data source.
    - id: kroki
      title: Kroki
      image: /images/development/dev-tools/kroki/logo.png
      url: /development/dev-tools/kroki
      category: dev-tools
      description: Creates diagrams from textual descriptions!
    - id: gophish
      title: Gophish
      image: /images/development/dev-tools/gophish/logo.png
      url: /development/dev-tools/gophish
      category: dev-tools
      description: A powerful phishing framework that makes it easy to test your organization's exposure to phishing.
    - id: emqx
      title: EMQX
      image: /images/development/dev-tools/emqx/logo.png
      url: /development/dev-tools/emqx
      category: dev-tools
      description: MQTT broker for IoT, IIoT, and connected vehicles. it supports multiple open standard protocols like MQTT, HTTP, QUIC, and WebSocket.
    - id: draw
      title: draw
      image: /images/development/dev-tools/draw/logo.png
      url: /development/dev-tools/draw
      category: dev-tools
      description: draw.io is a JavaScript, client-side editor for general diagramming.
    - id: stirling-pdf
      title: Stirling-PDF
      image: /images/development/dev-tools/stirling-pdf/logo.png
      url: /development/dev-tools/stirling-pdf
      category: dev-tools
      description: Web application that allows you to perform various operations on PDF files.
    - id: infisical
      title: Infisical
      image: /images/development/dev-tools/infisical/logo.png
      url: /development/dev-tools/infisical
      category: dev-tools
      description: "Infisical is an open-source, end-to-end encrypted platform for secret management: sync secrets across your team/infrastructure and prevents secret leaks."
    - id: quickchart
      title: QuickChart
      image: /images/development/dev-tools/quickchart/logo.png
      url: /development/dev-tools/quickchart
      category: dev-tools
      description: QuickChart allows you to generates chart images of charts from a URL.
    - id: gitlab
      title: Gitlab
      image: /images/development/dev-tools/gitlab/logo.png
      url: /development/dev-tools/gitlab
      category: dev-tools dev-ops
      description: GitLab enables you to deliver software faster with better security and collaboration in a single platform.
    - id: growthbook
      title: GrowthBook
      image: /images/development/dev-tools/growthbook/logo.png
      url: /development/dev-tools/growthbook
      category: dev-tools
      description: GrowthBook is an open-source platform for feature flags and A/B tests that helps teams deploy code efficiently and analyze experiments
    - id: gitness
      title: Gitness
      image: /images/development/dev-tools/gitness/logo.png
      url: /development/dev-tools/gitness
      category: dev-tools
      description: Gitness is an Open Source developer platform with Source Control Management, Continuous Integration, and Continuous Delivery.
    - id: devlake
      title: DevLake
      image: /images/development/dev-tools/devlake/logo.png
      url: /development/dev-tools/devlake
      category: dev-tools
      description: A dev data platform that ingests, analyzes, and visualizes the fragmented data from DevOps tools to extract insights for engineering excellence, developer experience, and community growth
    - id: onedev
      title: Onedev
      image: /images/development/dev-tools/onedev/logo.png
      url: /development/dev-tools/onedev
      category: dev-tools
      description: OneDev is an open-source all-in-one DevOps platform.
    - id: gogs
      title: Gogs
      image: /images/development/dev-tools/gogs/logo.png
      url: /development/dev-tools/gogs
      category: dev-tools
      description: Gogs is a lightweight self-hosted Git server that can be run on just about anything.
    - id: gitea
      title: Gitea
      image: /images/development/dev-tools/gitea/logo.png
      url: /development/dev-tools/gitea
      category: dev-tools
      description: Gitea is a painless self-hosted Git service. It is similar to GitHub, Bitbucket, and GitLab
    - id: gerrit
      title: Gerrit
      image: /images/development/dev-tools/gerrit/logo.png
      url: /development/dev-tools/gerrit
      category: dev-tools
      description: Gerrit is a code review and project management tool for Git based projects.
    - id: rstudio
      title: Rstudio
      image: /images/development/dev-tools/rstudio/logo.png
      url: /development/dev-tools/rstudio
      category: dev-tools
      description: Publish your R and Python content with RStudio Connect
    - id: gotenberg
      title: Gotenberg
      image: /images/development/dev-tools/gotenberg/logo.png
      url: /development/dev-tools/gotenberg
      category: dev-tools
      description: A Docker-powered stateless API for PDF files
    - id: bytebase
      title: Bytebase
      image: /images/development/dev-tools/bytebase/logo.png
      url: /development/dev-tools/bytebase
      category: dev-tools
      description: Bytebase is an open-source database CI/CD tool for developers and DBAs.
    - id: flagsmith
      title: Flagsmith
      image: /images/development/dev-tools/flagsmith/logo.png
      url: /development/dev-tools/flagsmith
      category: dev-tools
      description: Flagsmith is an, fully featured, Feature Flag and Remote Config service.
    - id: pritunl
      title: Pritunl
      image: /images/development/network/pritunl/logo.png
      url: /development/network/pritunl
      category: network
      description: Best open-source alternative to proprietary commercial VPN products such as Aviatrix and Pulse Secure.
    - id: rustdeskserver
      title: RustdeskServer
      image: /images/development/network/rustdeskserver/logo.png
      url: /development/network/rustdeskserver
      category: network
      description: Open source virtual / remote desktop infrastructure for everyone!
    - id: browserless
      title: Browserless
      image: /images/development/network/browserless/logo.png
      url: /development/network/browserless
      category: network nocode-lowcode
      description: Browserless provides fast, scalable, reliable web browser automation.
    - id: apachenifi
      title: ApacheNiFi
      image: /images/development/network/apachenifi/logo.png
      url: /development/network/apachenifi
      category: network
      description: Apache NiFi automates the movement of data between disparate data sources and systems, making data ingestion fast, easy, and secure.
    - id: gotify
      title: Gotify
      image: /images/development/network/gotify/logo.png
      url: /development/network/gotify
      category: network
      description: Gotify is a free and simple server for sending and receiving messages.
    - id: centrifugo
      title: Centrifugo
      image: /images/development/network/centrifugo/logo.png
      url: /development/network/centrifugo
      category: network dev-ops
      description: Centrifugo is a scalable real-time, language-agnostic messaging server.
    - id: wg-easy
      title: WG-Easy
      image: /images/development/network/wg-easy/logo.png
      url: /development/network/wg-easy
      category: network dev-ops
      description: WireGuard is a simple, fast general-purpose VPN for running on embedded interfaces and super computers alike.
    - id: nebula
      title: Nebula
      image: /images/development/network/nebula/logo.png
      url: /development/network/nebula
      category: network dev-ops
      description: Nebula is a scalable overlay networking tool with a focus on performance, simplicity and security
    - id: meshcentral
      title: MeshCentral
      image: /images/development/network/meshcentral/logo.png
      url: /development/network/meshcentral
      category: network
      description: MeshCentral is a full computer management web site
    - id: ubuntu-desktop
      title: Ubuntu-Desktop
      image: /images/development/dev-ops/ubuntu-desktop/logo.png
      url: /development/dev-ops/ubuntu-desktop
      category: dev-ops
      description: Ubuntu Virtual Desktop experience in your browser
    - id: gitlab-runner
      title: Gitlab-runner
      image: /images/development/dev-ops/gitlab-runner/logo.png
      url: /development/dev-ops/gitlab-runner
      category: dev-ops
      description: GitLab Runner is an application that works with GitLab CI/CD to run jobs in a pipeline.
    - id: dbgate
      title: DbGate
      image: /images/development/dev-ops/dbgate/logo.png
      url: /development/dev-ops/dbgate
      category: dev-ops
      description: Database manager for MySQL, PostgreSQL, SQL Server, MongoDB, SQLite, and others. Runs under Windows, Linux, Mac, or as a web application
    - id: imagor
      title: Imagor
      image: /images/development/dev-ops/imagor/logo.png
      url: /development/dev-ops/imagor
      category: dev-ops
      description: Imagor is a fast, Docker-ready image processing server.
    - id: sonarqube
      title: SonarQube
      image: /images/development/dev-ops/sonarqube/logo.png
      url: /development/dev-ops/sonarqube
      category: dev-ops
      description: SonarQube is an open-source platform that reveals the health of an application and highlights new issues.
    - id: jenkins
      title: Jenkins
      image: /images/development/dev-ops/jenkins/logo.png
      url: /development/dev-ops/jenkins
      category: dev-ops
      description: Jenkins is the leading open-source automation server.
    - id: airflow
      title: Airflow
      image: /images/development/dev-ops/airflow/logo.png
      url: /development/dev-ops/airflow
      category: dev-ops
      description: Apache Airflow is a platform created by the community to programmatically author, schedule and monitor workflows.
    - id: couchbase
      title: Couchbase
      image: /images/development/dev-ops/couchbase/logo.png
      url: /development/dev-ops/couchbase
      category: dev-ops
      description: Couchbase Server is a modern cloud-native, distributed database that fuses the strengths of relational databases such as SQL and ACID transactions with JSON flexibility and scale that defines NoSQL
    - id: airflow-worker
      title: Airflow-worker
      image: /images/development/dev-ops/airflow-worker/logo.png
      url: /development/dev-ops/airflow-worker
      category: dev-ops
      description: Apache Airflow is a platform created by the community to programmatically author, schedule and monitor workflows.
    - id: mage
      title: Mage AI
      image: /images/development/dev-ops/mage/logo.png
      url: /development/dev-ops/mage
      category: dev-ops
      description: The modern replacement for Airflow. Build, run, and manage data pipelines for integrating and transforming data.
    - id: powerdns
      title: PowerDNS
      image: /images/development/dev-ops/powerdns/logo.png
      url: /development/dev-ops/powerdns
      category: dev-ops
      description: PowerDNS is a premier supplier of open-source DNS software, services and support.
    - id: nomad
      title: Nomad
      image: /images/development/dev-ops/nomad/logo.png
      url: /development/dev-ops/nomad
      category: dev-ops
      description: Nomad is a scheduler and workload orchestrator.
    - id: minio
      title: MinIO
      image: /images/development/dev-ops/minio/logo.png
      url: /development/dev-ops/minio
      category: dev-ops
      description: MinIO is a leader in hybrid cloud and multi-cloud object storage.
    - id: kellnr
      title: Kellnr
      image: /images/development/dev-ops/kellnr/logo.png
      url: /development/dev-ops/kellnr
      category: dev-ops
      description: Kellnr allows you to host private Rust crates on your hardware. You can also keep full control of your code at any time.
    - id: portainer
      title: Portainer
      image: /images/development/dev-ops/portainer/logo.png
      url: /development/dev-ops/portainer
      category: dev-ops
      description: Portainer is a centralized service delivery platform for containerized apps.
    - id: cronicle
      title: Cronicle
      image: /images/development/dev-ops/cronicle/logo.png
      url: /development/dev-ops/cronicle
      category: dev-ops
      description: Cronicle is a simple, distributed task scheduler and runner with a web based UI.
    - id: haproxy
      title: HAProxy
      image: /images/development/dev-ops/haproxy/logo.png
      url: /development/dev-ops/haproxy
      category: dev-ops
      description: The Reliable, High Performance TCP/HTTP Load Balancer
    - id: openresty
      title: OpenResty
      image: /images/development/dev-ops/openresty/logo.png
      url: /development/dev-ops/openresty
      category: dev-ops
      description: A Fast and Scalable Web Platform by Extending NGINX with LuaJIT
    - id: kestra
      title: Kestra
      image: /images/development/dev-ops/kestra/logo.png
      url: /development/dev-ops/kestra
      category: dev-ops
      description: The open source data orchestration and scheduling platform.
    - id: dockerregistry
      title: DockerRegistry
      image: /images/development/dev-ops/dockerregistry/logo.png
      url: /development/dev-ops/dockerregistry
      category: dev-ops
      description: Docker Registry is a stateless, highly scalable server side application that stores and lets you distribute Docker images. The Registry is open-source, under the permissive Apache license.
    - id: mailcow
      title: MailCow
      image: /images/development/dev-ops/mailcow/logo.png
      url: /development/dev-ops/mailcow
      category: dev-ops
      description: Mailcow is a mail server suite with an elegant web interface for managing domains, mailboxes, etc.
    - id: postal
      title: Postal
      image: /images/development/dev-ops/postal/logo.png
      url: /development/dev-ops/postal
      category: dev-ops
      description: Postal is a fully featured open-source mail delivery platform for incoming and outgoing email.
    - id: healthchecks
      title: Healthchecks
      image: /images/development/dev-ops/healthchecks/logo.png
      url: /development/dev-ops/healthchecks
      category: dev-ops
      description: Healthchecks is an online service for monitoring regularly running tasks such as cron jobs.
    - id: guacamole
      title: Guacamole
      image: /images/development/dev-ops/guacamole/logo.png
      url: /development/dev-ops/guacamole
      category: dev-ops
      description: Apache Guacamole is a clientless remote desktop gateway.
    - id: k3s
      title: K3S
      image: /images/development/dev-ops/k3s/logo.png
      url: /development/dev-ops/k3s
      category: dev-ops
      description: K3s is a fully compliant Kubernetes distribution
    - id: microk8s
      title: Microk8s
      image: /images/development/dev-ops/microk8s/logo.png
      url: /development/dev-ops/microk8s
      category: dev-ops
      description: MicroK8s is a small, fast, single-package Kubernetes for developers, IoT and edge
    - id: vault
      title: Vault
      image: /images/development/dev-ops/vault/logo.png
      url: /development/dev-ops/vault
      category: dev-ops
      description: Vault is a tool for secrets management, encryption as a service, and privileged access management
    - id: k0s
      title: k0s
      image: /images/development/dev-ops/k0s/logo.png
      url: /development/dev-ops/k0s
      category: dev-ops
      description: The Simple, Solid & Certified Kubernetes Distribution. Deploy and run Kubernetes workloads at any scale on any infrastructure. All batteries included. 100% open source & free.
    - id: openldap
      title: OpenLDAP
      image: /images/development/dev-ops/openldap/logo.png
      url: /development/dev-ops/openldap
      category: dev-ops
      description: OpenLDAP is a free, open-source implementation of the Lightweight Directory Access Protocol (LDAP)
    - id: nexus3
      title: Nexus3
      image: /images/development/dev-ops/nexus3/logo.png
      url: /development/dev-ops/nexus3
      category: dev-ops
      description: The free artifact repository with universal format support.
    - id: hop
      title: Hop
      image: /images/development/nocode-lowcode/hop/logo.png
      url: /development/nocode-lowcode/hop
      category: nocode-lowcode
      description: Apache Hop is a data orchestration and data engineering platform that aims to facilitate all aspects of data and metadata orchestration
    - id: automatisch
      title: Automatisch
      image: /images/development/nocode-lowcode/automatisch/logo.png
      url: /development/nocode-lowcode/automatisch
      category: nocode-lowcode
      description: Automatisch helps you to automate your business processes without coding. Use our affordable cloud solution or self-host on your own servers.
    - id: illa
      title: ILLA
      image: /images/development/nocode-lowcode/illa/logo.png
      url: /development/nocode-lowcode/illa
      category: nocode-lowcode
      description: ILLA Cloud is a low-code platform. Anyone can build internal tools with ILLA Cloud in minutes.
    - id: totaljsflow
      title: TotaljsFlow
      image: /images/development/nocode-lowcode/totaljsflow/logo.png
      url: /development/nocode-lowcode/totaljsflow
      category: nocode-lowcode
      description: It's a friendly, modern, straightforward Visual Programming Interface for Low-code Development accessible through a web browser. The tool integrates, processes, and transforms various events and data in real-time.
    - id: node-red
      title: Node-red
      image: /images/development/nocode-lowcode/node-red/logo.png
      url: /development/nocode-lowcode/node-red
      category: nocode-lowcode
      description: Node-RED is a low-code programming environment for event-driven applications.
    - id: budibase
      title: Budibase
      image: /images/development/nocode-lowcode/budibase/logo.png
      url: /development/nocode-lowcode/budibase
      category: nocode-lowcode
      description: Budibase is a quick way to build business apps that empower teams and improve productivity.
    - id: apitable
      title: APITable
      image: /images/development/nocode-lowcode/apitable/logo.png
      url: /development/nocode-lowcode/apitable
      category: nocode-lowcode
      description: APITable is an API-oriented low-code platform for building collaborative apps and is better than all other Airtable open-source alternatives.
    - id: lowcoder
      title: Lowcoder
      image: /images/development/nocode-lowcode/lowcoder/logo.png
      url: /development/nocode-lowcode/lowcoder
      category: nocode-lowcode
      description: Create software applications for your Company and your Customers with minimal coding experience. Lowcoder is the best Retool, Appsmith, or Tooljet Alternative.
    - id: dify
      title: Dify
      image: /images/development/nocode-lowcode/dify/logo.png
      url: /development/nocode-lowcode/dify
      category: nocode-lowcode
      description: LLM app development platform. Dify's intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features, and more, letting you quickly go from prototype to production.
    - id: n8n
      title: N8N
      image: /images/development/nocode-lowcode/n8n/logo.png
      url: /development/nocode-lowcode/n8n
      category: nocode-lowcode
      description: n8n is a free, self-hosted workflow automation tool that integrates with other apps to automate processes between them.
    - id: baserow
      title: Baserow
      image: /images/development/nocode-lowcode/baserow/logo.png
      url: /development/nocode-lowcode/baserow
      category: nocode-lowcode
      description: Baserow is an open source no-code database tool and Airtable alternative.
    - id: nocodb
      title: NocoDB
      image: /images/development/nocode-lowcode/nocodb/logo.png
      url: /development/nocode-lowcode/nocodb
      category: nocode-lowcode
      description: NocoDB is an open-source #NoCode platform that turns any database into a smart spreadsheet.
    - id: appsmith
      title: Appsmith
      image: /images/development/nocode-lowcode/appsmith/logo.png
      url: /development/nocode-lowcode/appsmith
      category: nocode-lowcode
      description: Appsmith is a powerful open-source framework to build internal tools.
    - id: tooljet
      title: ToolJet
      image: /images/development/nocode-lowcode/tooljet/logo.png
      url: /development/nocode-lowcode/tooljet
      category: nocode-lowcode
      description: ToolJet is an open-source low-code framework to build and deploy custom internal tools
    - id: nocobase
      title: NocoBase
      image: /images/development/nocode-lowcode/nocobase/logo.png
      url: /development/nocode-lowcode/nocobase
      category: nocode-lowcode
      description: Scalability-first open-source no-code platform. No programming required, build your own collaboration platform, management system with NocoBase in minutes.
    - id: hasura
      title: Hasura
      image: /images/development/nocode-lowcode/hasura/logo.png
      url: /development/nocode-lowcode/hasura
      category: nocode-lowcode
      description: Hasura GraphQL Engine is an open-source product that connects to your databases & services and gives you a realtime GraphQL API, instantly.
    - id: openblocks
      title: OpenBlocks
      image: /images/development/nocode-lowcode/openblocks/logo.png
      url: /development/nocode-lowcode/openblocks
      category: nocode-lowcode
      description: Openblocks is a retool Alternative developer-friendly open-source low-code platform to build internal apps within minutes.
    - id: changedetection
      title: ChangeDetection
      image: /images/hosting-and-infrastructure/monitoring/changedetection/logo.png
      url: /hosting-and-infrastructure/monitoring/changedetection
      category: monitoring
      description: Changedetection.io is an open source web page monitoring, notification and change detection.
    - id: coroot
      title: Coroot
      image: /images/hosting-and-infrastructure/monitoring/coroot/logo.png
      url: /hosting-and-infrastructure/monitoring/coroot
      category: monitoring
      description: Coroot is an APM & Observability tool, a DataDog and NewRelic alternative
    - id: grafana
      title: Grafana
      image: /images/hosting-and-infrastructure/monitoring/grafana/logo.png
      url: /hosting-and-infrastructure/monitoring/grafana
      category: monitoring
      description: Grafana is a multi-platform, open-source analytics and interactive visualization web application.
    - id: loki
      title: Loki
      image: /images/hosting-and-infrastructure/monitoring/loki/logo.png
      url: /hosting-and-infrastructure/monitoring/loki
      category: monitoring
      description: Loki is a log aggregation system designed to store and query logs from all your applications and infrastructure.
    - id: glitchtip
      title: GlitchTip
      image: /images/hosting-and-infrastructure/monitoring/glitchtip/logo.png
      url: /hosting-and-infrastructure/monitoring/glitchtip
      category: monitoring
      description: Reimplementation of the Sentry error tracking platform, Track errors, uptime, and performance.
    - id: sensu
      title: Sensu
      image: /images/hosting-and-infrastructure/monitoring/sensu/logo.png
      url: /hosting-and-infrastructure/monitoring/sensu
      category: monitoring
      description: Sensu is an open source monitoring tool for ephemeral infrastructure and distributed applications.
    - id: signoz
      title: SigNoz
      image: /images/hosting-and-infrastructure/monitoring/signoz/logo.png
      url: /hosting-and-infrastructure/monitoring/signoz
      category: monitoring
      description: SigNoz is an open-source APM solution for understanding issues in your applications and solving them quickly
    - id: uptime-kuma
      title: Uptime-kuma
      image: /images/hosting-and-infrastructure/monitoring/uptime-kuma/logo.png
      url: /hosting-and-infrastructure/monitoring/uptime-kuma
      category: monitoring
      description: Uptime Kuma is a self-hosted monitoring tool like Uptime Robot.
    - id: healthchecks
      title: Healthchecks
      image: /images/hosting-and-infrastructure/monitoring/healthchecks/logo.png
      url: /hosting-and-infrastructure/monitoring/healthchecks
      category: monitoring
      description: Healthchecks is an online service for monitoring regularly running tasks such as cron jobs.
    - id: victoriametrics
      title: VictoriaMetrics
      image: /images/hosting-and-infrastructure/monitoring/victoriametrics/logo.png
      url: /hosting-and-infrastructure/monitoring/victoriametrics
      category: monitoring
      description: VictoriaMetrics is a fast, cost-effective monitoring solution and time series database
    - id: jitsu
      title: Jitsu
      image: /images/hosting-and-infrastructure/monitoring/jitsu/logo.png
      url: /hosting-and-infrastructure/monitoring/jitsu
      category: monitoring
      description: Jitsu is an open-source web and app-event collection platform.
    - id: zabbix
      title: Zabbix
      image: /images/hosting-and-infrastructure/monitoring/zabbix/logo.png
      url: /hosting-and-infrastructure/monitoring/zabbix
      category: monitoring
      description: Zabbix is an enterprise-class open source distributed monitoring solution.
    - id: prometheus
      title: Prometheus
      image: /images/hosting-and-infrastructure/monitoring/prometheus/logo.png
      url: /hosting-and-infrastructure/monitoring/prometheus
      category: monitoring
      description: Power your metrics and alerting with the leading open-source monitoring solution
    - id: nagios
      title: Nagios
      image: /images/hosting-and-infrastructure/monitoring/nagios/logo.png
      url: /hosting-and-infrastructure/monitoring/nagios
      category: monitoring infrastructure
      description: The Industry Standard In IT Infrastructure Monitoring
    - id: canopsis
      title: Canopsis
      image: /images/hosting-and-infrastructure/monitoring/canopsis/logo.png
      url: /hosting-and-infrastructure/monitoring/canopsis
      category: monitoring
      description: The first open-source hypervision solution
    - id: mailcow
      title: MailCow
      image: /images/hosting-and-infrastructure/email/mailcow/logo.png
      url: /hosting-and-infrastructure/email/mailcow
      category: email
      description: Mailcow is a mail server suite with an elegant web interface for managing domains, mailboxes, etc.
    - id: postal
      title: Postal
      image: /images/hosting-and-infrastructure/email/postal/logo.png
      url: /hosting-and-infrastructure/email/postal
      category: email
      description: Postal is a fully featured open-source mail delivery platform for incoming and outgoing email.
    - id: mailu
      title: Mailu
      image: /images/hosting-and-infrastructure/email/mailu/logo.png
      url: /hosting-and-infrastructure/email/mailu
      category: email
      description: Mailu is an insular email distribution - mail server as Docker images
    - id: nextcloud
      title: Nextcloud
      image: /images/hosting-and-infrastructure/storage/nextcloud/logo.png
      url: /hosting-and-infrastructure/storage/nextcloud
      category: storage
      description: Nextcloud provides an industry-leading, on-premises content collaboration platform.
    - id: photoprism
      title: PhotoPrism
      image: /images/hosting-and-infrastructure/storage/photoprism/logo.png
      url: /hosting-and-infrastructure/storage/photoprism
      category: storage
      description: PhotoPrism is an AI-powered app for browsing, organizing & sharing your photo collection
    - id: syncthing
      title: Syncthing
      image: /images/hosting-and-infrastructure/storage/syncthing/logo.png
      url: /hosting-and-infrastructure/storage/syncthing
      category: storage
      description: Syncthing is a free, continuous, multiple-device file synchronization program.
    - id: filestash
      title: Filestash
      image: /images/hosting-and-infrastructure/storage/filestash/logo.png
      url: /hosting-and-infrastructure/storage/filestash
      category: storage
      description: Filestash is a Dropbox-like file manager that lets you manage your data anywhere it is located.
    - id: owncloud
      title: ownCloud
      image: /images/hosting-and-infrastructure/storage/owncloud/logo.png
      url: /hosting-and-infrastructure/storage/owncloud
      category: storage
      description: ownCloud is a suite of client-server software for creating and using file hosting services.
    - id: paperless-ngx
      title: Paperless-ngx
      image: /images/hosting-and-infrastructure/storage/paperless-ngx/logo.png
      url: /hosting-and-infrastructure/storage/paperless-ngx
      category: storage
      description: Paperless-ngx is a document management system that transforms your physical documents into a searchable online archive so you can keep, well, less paper.
    - id: archivebox
      title: ArchiveBox
      image: /images/hosting-and-infrastructure/storage/archivebox/logo.png
      url: /hosting-and-infrastructure/storage/archivebox
      category: storage
      description: ArchiveBox is a powerful, self-hosted internet archiving solution to collect, save, and view sites you want to preserve offline.
    - id: docspell
      title: Docspell
      image: /images/hosting-and-infrastructure/storage/docspell/logo.png
      url: /hosting-and-infrastructure/storage/docspell
      category: storage
      description: Simple document organizer
    - id: immich
      title: Immich
      image: /images/hosting-and-infrastructure/storage/immich/logo.png
      url: /hosting-and-infrastructure/storage/immich
      category: storage
      description: Self-hosted photo and video backup solution directly from your mobile phone.
    - id: picoshare
      title: Picoshare
      image: /images/hosting-and-infrastructure/storage/picoshare/logo.png
      url: /hosting-and-infrastructure/storage/picoshare
      category: storage
      description: PicoShare is a service for sharing images, videos, and other files.
    - id: minio
      title: MinIO
      image: /images/hosting-and-infrastructure/storage/minio/logo.png
      url: /hosting-and-infrastructure/storage/minio
      category: storage
      description: MinIO is a leader in hybrid cloud and multi-cloud object storage.
    - id: sftpgo
      title: SFTPGo
      image: /images/hosting-and-infrastructure/storage/sftpgo/logo.png
      url: /hosting-and-infrastructure/storage/sftpgo
      category: storage
      description: Fully featured and highly configurable SFTP server with optional HTTP/S, FTP/S and WebDAV support
    - id: nomad
      title: Nomad
      image: /images/hosting-and-infrastructure/containers/nomad/logo.png
      url: /hosting-and-infrastructure/containers/nomad
      category: containers
      description: Nomad is a scheduler and workload orchestrator.
    - id: portainer
      title: Portainer
      image: /images/hosting-and-infrastructure/containers/portainer/logo.png
      url: /hosting-and-infrastructure/containers/portainer
      category: containers
      description: Portainer is a centralized service delivery platform for containerized apps.
    - id: dockerregistry
      title: DockerRegistry
      image: /images/hosting-and-infrastructure/containers/dockerregistry/logo.png
      url: /hosting-and-infrastructure/containers/dockerregistry
      category: containers
      description: Docker Registry is a stateless, highly scalable server side application that stores and lets you distribute Docker images. The Registry is open-source, under the permissive Apache license.
    - id: k3s
      title: K3S
      image: /images/hosting-and-infrastructure/containers/k3s/logo.png
      url: /hosting-and-infrastructure/containers/k3s
      category: containers
      description: K3s is a fully compliant Kubernetes distribution
    - id: microk8s
      title: Microk8s
      image: /images/hosting-and-infrastructure/containers/microk8s/logo.png
      url: /hosting-and-infrastructure/containers/microk8s
      category: containers
      description: MicroK8s is a small, fast, single-package Kubernetes for developers, IoT and edge
    - id: k0s
      title: k0s
      image: /images/hosting-and-infrastructure/containers/k0s/logo.png
      url: /hosting-and-infrastructure/containers/k0s
      category: containers
      description: The Simple, Solid & Certified Kubernetes Distribution. Deploy and run Kubernetes workloads at any scale on any infrastructure. All batteries included. 100% open source & free.
    - id: nexus3
      title: Nexus3
      image: /images/hosting-and-infrastructure/containers/nexus3/logo.png
      url: /hosting-and-infrastructure/containers/nexus3
      category: containers
      description: The free artifact repository with universal format support.
    - id: itop
      title: iTop
      image: /images/hosting-and-infrastructure/infrastructure/itop/logo.png
      url: /hosting-and-infrastructure/infrastructure/itop
      category: infrastructure
      description: iTop adapts to the needs of digital businesses to manage multiple customers, contracts and SLAs
    - id: centrifugo
      title: Centrifugo
      image: /images/hosting-and-infrastructure/infrastructure/centrifugo/logo.png
      url: /hosting-and-infrastructure/infrastructure/centrifugo
      category: infrastructure
      description: Centrifugo is a scalable real-time, language-agnostic messaging server.
    - id: powerdns
      title: PowerDNS
      image: /images/hosting-and-infrastructure/infrastructure/powerdns/logo.png
      url: /hosting-and-infrastructure/infrastructure/powerdns
      category: infrastructure
      description: PowerDNS is a premier supplier of open-source DNS software, services and support.
    - id: rabbitmq
      title: RabbitMQ
      image: /images/hosting-and-infrastructure/infrastructure/rabbitmq/logo.png
      url: /hosting-and-infrastructure/infrastructure/rabbitmq
      category: infrastructure
      description: RabbitMQ is the most widely deployed open source message broker
    - id: haproxy
      title: HAProxy
      image: /images/hosting-and-infrastructure/infrastructure/haproxy/logo.png
      url: /hosting-and-infrastructure/infrastructure/haproxy
      category: infrastructure
      description: The Reliable, High Performance TCP/HTTP Load Balancer
    - id: openresty
      title: OpenResty
      image: /images/hosting-and-infrastructure/infrastructure/openresty/logo.png
      url: /hosting-and-infrastructure/infrastructure/openresty
      category: infrastructure
      description: A Fast and Scalable Web Platform by Extending NGINX with LuaJIT
    - id: squid
      title: Squid
      image: /images/hosting-and-infrastructure/infrastructure/squid/logo.png
      url: /hosting-and-infrastructure/infrastructure/squid
      category: infrastructure
      description: Fast & powerful proxy server
    - id: localstack
      title: LocalStack
      image: /images/hosting-and-infrastructure/infrastructure/localstack/logo.png
      url: /hosting-and-infrastructure/infrastructure/localstack
      category: infrastructure
      description: A fully functional local cloud stack. Develop and test your cloud and serverless apps offline!
---
