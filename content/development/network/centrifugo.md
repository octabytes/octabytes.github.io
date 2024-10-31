---
draft: false
title: Centrifugo
content:
  id: centrifugo
  name: Centrifugo
  logo: /images/development/network/centrifugo/logo.png
  website: https://centrifugal.dev/
  iframe_website: /website-iframe/development/network/centrifugo
  dashboardImage: /images/development/network/centrifugo/screenshot-1.jpg
  short_description: Centrifugo is a scalable real-time, language-agnostic messaging server.
  description: Centrifugo, a scalable real-time messaging server, works in conjunction with whatever programming language your application uses on frontend or backend sides. Centrifugo broadcasts the event to all connected clients subscribed to the event channel. In brief, Centrifugo is a user-facing PUB/SUB server.
  features:
    - title: Integrates with everything
      description: "Centrifugo, a self-hosted service, can handle connections over a variety of real-time transports and provides a simple publish API. It integrates well with any application. There's no need to change an application architecture to introduce real-time features; you just let Centrifugo deal with persistent connections."
    - title: Great performance
      description: Centrifugo, built in Go language, has some smart optimizations inside. It performs very well; a test stand, with 1m WebSocket connections, showed that about 30m messages per minute (500k messages per second) would be delivered to connected clients and latency would not be greater than 200ms in 99 percentile.
    - title: Feature-rich
      description: "Centrifugo's many built-in features can help you to build an attractive real-time application in a short time. Centrifugo provides different types of subscriptions, hot channel history, instant presence and RPC calls. There is also the option to proxy connection events to the application backend over HTTP or GRPC."
    - title: Out-of-the-box scalability
      description: "Built-in Redis, KeyDB, Tarantool engines or Nats broker make it possible to scale connections over different machines. With consistent sharding of Redis, KeyDB and Tarantool, it's possible to handle millions of active connections with reasonable hardware requirements."
  screenshots:
    - /images/development/network/centrifugo/screenshot-1.jpg
    - /images/development/network/centrifugo/screenshot-2.jpg
---