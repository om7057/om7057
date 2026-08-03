<h1 align="center">Om Kulkarni</h1>

<p align="center">
Backend and distributed systems &nbsp;·&nbsp; Go, gRPC, event-driven architecture<br/>
Software Engineer &nbsp;·&nbsp; Contributor to CNCF-hosted projects
</p>

<p align="center">
<a href="https://om-kulk.vercel.app/">Portfolio</a> &nbsp;·&nbsp;
<a href="https://www.linkedin.com/in/om7057/">LinkedIn</a> &nbsp;·&nbsp;
<a href="https://medium.com/@om7057">Medium</a> &nbsp;·&nbsp;
<a href="https://x.com/kulkarniom7057">X</a>
</p>

---

|  |  |
|---|---|
| **Merged upstream** | OpenTelemetry (C++ SDK, Go Contrib, Go Compile Instrumentation) · Prometheus · GoFr |
| **CNCF ecosystem** | Prometheus and OpenTelemetry are both CNCF **graduated** projects |
| **Focus** | Metrics cardinality · specification compliance · declarative configuration · TSDB internals · migration tooling |
| **Research** | IEEE ICFT 2025, co-author and presenter on metadata exploration across lakehouse table formats |
| **Experience** | Software Engineer working on backend and distributed systems. Previously SDE Intern at CoinSwitch (Go, gRPC, NATS JetStream) and Engineering Intern at ConnectWise (Go, Kafka, Aurora) |

---

## Recent work

A pattern runs through most of what I contribute upstream: **software that fails silently.**

- **Prometheus TSDB** — querier cleanup discarded errors from `Close()`, masking I/O failures as successful queries. Fixed with `errors.Join()` to surface concurrent failures.
  [Issue #19114](https://github.com/prometheus/prometheus/issues/19114) · [PR #19120](https://github.com/prometheus/prometheus/pull/19120)

- **OTel C++: EnvironmentCarrier** — empty keys silently mapped to the wrong slot instead of erroring, a spec violation. Fixed and documented the `string_view` caching contract.
  [Issue #4190](https://github.com/open-telemetry/opentelemetry-cpp/issues/4190) · [PR #4264](https://github.com/open-telemetry/opentelemetry-cpp/pull/4264)

- **OTel C++: Cardinality Limits** — the Metrics SDK hardcoded a 2000 limit and silently discarded user config. Added per-instrument-type configurable limits end-to-end, from `MetricReader` through the declarative YAML path.
  [Issue #3292](https://github.com/open-telemetry/opentelemetry-cpp/issues/3292) · [PR #4188](https://github.com/open-telemetry/opentelemetry-cpp/pull/4188)

- **OTel C++: LoggerConfig** — `minimum_severity` and `trace_based` were missing from the declarative config parser, so file-configured loggers silently ignored severity filtering. Added both fields with spec-aligned defaults.
  [Issue #4130](https://github.com/open-telemetry/opentelemetry-cpp/issues/4130) · [PR #4131](https://github.com/open-telemetry/opentelemetry-cpp/pull/4131)

- **OTel C++: Histogram View Fix** — a follow-up gap where histogram views setting only a cardinality limit were silently rejected. Fixed, and caught a second regression (degenerate single-bucket histograms) during review.
  [Issue #3292](https://github.com/open-telemetry/opentelemetry-cpp/issues/3292) · [PR #4314](https://github.com/open-telemetry/opentelemetry-cpp/pull/4314)

- **OTel Go Contrib: otelmongo** — pooled connection ID suffixes broke host/port parsing, unbounding `network.peer.address` cardinality. Fixed the parsing and ported the fix to the v1 package too.
  [Issue #9275](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9275) · [PR #9352](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9352)

- **OTel Go Contrib: xray** — a discarded seed-read error could make `IDGenerator` emit identical trace/span IDs across instances. Replaced it with `math/rand/v2`'s runtime-seeded globals, preserving the stable v1 module's API.
  [Issue #9048](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9048) · [PR #9359](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9359)

- **OTel Go Contrib: otelhttp** — `network.protocol.version` was read off the request instead of the negotiated response, misreporting HTTP/2 as HTTP/1.1. Re-sourced it from the response and regenerated all six consumer packages.
  [Issue #9007](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9007) · [PR #9371](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9371)

- **OTel Go: Compile Instrumentation** — `OTEL_GO_DISABLED_INSTRUMENTATIONS=gin` had no effect since gin never checked the runtime enable/disable gate every other instrumentation used. Gave gin its own instrumentation key and hardened it against mid-request env var changes.
  [Issue #839](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/839) · [PR #840](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/840)

- **GoFr** — added ScyllaDB migration support with a `gomock`-based test harness, extending the framework's schema-migration path beyond relational backends.
  [PR #2085](https://github.com/gofr-dev/gofr/pull/2085)

---

## Research

**MetaLens: A Web-Based Tool for Multi-Format Metadata Exploration**
<br/>
IEEE ICFT 2025, Smart Computing track. Co-author and presenter.

A format-agnostic metadata layer for lakehouse systems, unifying schema and snapshot state
across Iceberg, Hudi, Delta, and Parquet into a single view.

[IEEE Xplore](https://ieeexplore.ieee.org/document/11336690) &nbsp;·&nbsp;
[DOI: 10.1109/ICFT66708.2025.11336690](https://doi.org/10.1109/ICFT66708.2025.11336690)

---

## Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=go,cpp,java,py,postgres,redis,cassandra,mongodb&perline=8" height="55" />
</p>
<p align="center">
  <img src="https://skillicons.dev/icons?i=kubernetes,docker,kafka,grafana,prometheus,aws,linux,githubactions&perline=8" height="55" />
</p>

---

## Contribution graph

<p align="center">
  <img src="https://raw.githubusercontent.com/om7057/om7057/output/snake.svg" alt="snake contribution graph" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/om7057/om7057/main/profile-3d-contrib/profile-night-green.svg" alt="3D contribution graph" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=om7057&theme=react-dark&hide_border=true&area=true" alt="commit activity graph" />
</p>
