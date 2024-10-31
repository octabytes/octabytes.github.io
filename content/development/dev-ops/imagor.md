---
draft: false
title: Imagor
content:
  id: imagor
  name: Imagor
  logo: /images/development/dev-ops/imagor/logo.png
  website: https://github.com/cshum/imagor
  iframe_website: /website-iframe/development/dev-ops/imagor
  dashboardImage: /images/development/dev-ops/imagor/screenshot-1.jpg
  short_description: Imagor is a fast, Docker-ready image processing server.
  description: Imagor is a Go application that is highly optimized for concurrent requests. It is ready to be installed and used in any Unix environment, and ready to be containerized using Docker.Imagor adopts the Thumbor URL syntax and covers most of the web image processing use cases. If these fit your requirements, Imagor would be a lightweight, high performance drop-in replacement.
  features:
    - title: Loader
      description: Loader loads image. Enable Loader where you wish to load images from, but without modifying it e.g. static directory.
    - title: Storage
      description: Storage loads and saves image. This allows subsequent requests for the same image loads directly from the storage, instead of HTTP source.
    - title: Result Storage
      description: Result Storage loads and saves the processed image. This allows subsequent request of the same parameters loads from the result storage, saving processing resources.
    - title: HTTP Loader
      description: Imagor provides built-in adaptors that support HTTP, proxy, file system and AWS S3. By default, HTTP Loader is used as fallback.
  screenshots:
    - /images/development/dev-ops/imagor/screenshot-1.jpg
    - /images/development/dev-ops/imagor/screenshot-2.png
---