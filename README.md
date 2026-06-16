<h1 align="center">Hey Om here👋 What's Up?</h1>

<h3 align="center">
Backend & Distributed Systems | Event-Driven Systems • DevOps | Open Source Enthusiast
</h3>

<p align="center">
  Fun fact: I make systems scalable so I can sleep peacefully 😄
</p>

---

## 💻 Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=go,cpp,java,js,py,postgres,mongodb,mysql,redis,cassandra&perline=10" height="60" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=docker,kubernetes,kafka,aws,linux,git,gitlab,githubactions,postman,vscode&perline=10" height="60" />
</p>

---

## ⚙️ What I've Built

**Microservices & Event-Driven Systems**
- Production Go microservices with REST and gRPC APIs; real-time streaming over NATS JetStream (at-least-once) and Kafka-based event pipelines.
- Concurrent-safe subscription management (`sync.Map`) with reconnect-and-replay for fault-tolerant stream recovery.
- Hystrix-inspired circuit breaker with tuned thresholds and fallback strategies for graceful degradation.

**Observability & Distributed Tracing**
- gRPC distributed tracing via interceptor chains, propagating trace IDs through HTTP/2 metadata for full request lifecycle correlation.
- Structured logging across REST, gRPC, and async CGo layers with correlation IDs feeding into ELK/Loki pipelines.
- REST middleware with pre/post hooks, latency tracking, and INFO/WARN/ERROR classification for SLI/SLO alerting.
- Trace-aware logging across Go↔C++ FFI boundary, maintaining correlation through async SDK responses.

**Infrastructure, Secrets & Configuration**
- 12-factor multi-environment config with runtime selection via entrypoint scripts, eliminating cross-environment bleed.
- Secrets pipeline using runtime injection and file materialization with strict Unix permissions (0600/0700) for zero-code rotation.
- Multi-stage Docker builds with environment-driven config binding at container startup.

**Databases & Scalability**
- PostgreSQL (Aurora) sharding with partner-based shard mapping and cache-first reads for horizontal scalability.
- Shard-aware data routing with entitlement validation and controlled ingestion/retention pipelines.

**Concurrency & Systems**
- Fail-fast singleton init via `sync.Once` with strict dependency ordering, preventing nil-pointer crashes under load.
- PID 1 signal handling, file descriptor lifecycle, TCP keepalive tuning, and cooperative cancellation via `context.Context`.

---

## 🚀 Open Source Contributions

### OpenTelemetry C++ SDK | C++17, YAML, CMake, Google Test | Jun 2026
- Added `minimum_severity` and `trace_based` fields to `LoggerConfig`, updating the YAML parser with correct defaults and resolving CI failures across clang-format, markdownlint, and IWYU for all three build presets.
- Added integration tests in `yaml_logs_test.cc` covering default values, explicit severity levels, and trace-based filtering scenarios.

### GoFr Framework — ScyllaDB Migration Support | Go, ScyllaDB, gomock | Jul – Aug 2025
- Contributed ScyllaDB migration support to GoFr (14K+ stars), enabling schema migration workflows for distributed NoSQL systems.
- Built `gomock`-based testing infra (`MockScyllaDB`) and a sample migration pipeline covering table versioning, schema evolution, and rollback edge cases.

Merged PR: https://github.com/gofr-dev/gofr/pull/2085

---

## 📊 Stats
<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=om7057&theme=github_dark" height="150" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=om7057&theme=github_dark" height="150" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=om7057&theme=github_dark&utcOffset=5.5" height="150" />
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=om7057&theme=github_dark" width="800" />
</p>

---

## 💡 Contribution Graph
<p align="center">
  <img
    src="https://raw.githubusercontent.com/om7057/om7057/output/snake.svg"
    alt="snake contribution graph"
  />
</p>

---

## 🌐 Connect with me
<p align="center">
  <a href="https://www.linkedin.com/in/om7057/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&color=0077B5&logoColor=white&style=for-the-badge" height="28" />
  </a>
  <a href="https://x.com/kulkarniom7057" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Twitter&logo=x&color=000000&logoColor=white&style=for-the-badge" height="28" />
  </a>
</p>
