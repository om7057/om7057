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

In the Prometheus TSDB, querier cleanup discarded the error from `Close()`. On multi-block
queries a failing block would surface as a successful query with missing data: no error, no
log line, nothing for an operator to page on. I used `errors.Join()` to preserve concurrent
cleanup failures alongside the primary error, so the failure reaches the caller instead of
vanishing.
[Issue #19114](https://github.com/prometheus/prometheus/issues/19114) ·
[PR #19120](https://github.com/prometheus/prometheus/pull/19120)

The same shape appeared in the OpenTelemetry C++ SDK. `EnvironmentCarrier::NormalizeKey()`
did not normalize the empty key, so `Get("")` and `Set("")` quietly operated on the wrong
slot rather than erroring, a spec violation against
[opentelemetry-specification#5163](https://github.com/open-telemetry/opentelemetry-specification/issues/5163).
The fix also removed a now-unreachable `!empty()` guard, documented why the caching layer is a
`string_view` lifetime and thread-safety *requirement* rather than an optimization, and added
two regression tests verified to fail without the patch.
[Issue #4190](https://github.com/open-telemetry/opentelemetry-cpp/issues/4190) ·
[PR #4264](https://github.com/open-telemetry/opentelemetry-cpp/pull/4264)

The Metrics SDK had the same problem one layer up: cardinality limits were hardcoded to 2000,
and configuration supplied by the user was logged as unsupported and thrown away. I added a
`CardinalityLimits` struct with per-instrument-type fields, exposed
`GetCardinalityLimit(InstrumentType)` on `MetricReader` and as a pure virtual on the
`CollectorHandle` interface, and resolved the declarative YAML path through a zero-as-unset
sentinel so an explicit `2000` counts as a real override rather than an absent one. The same
change fixed undefined behaviour from uninitialized configuration members, and the default
stayed a namespace-level `constexpr` to avoid the out-of-class definition C++14 would demand
of an ODR-used static member.
[Issue #3292](https://github.com/open-telemetry/opentelemetry-cpp/issues/3292) ·
[PR #4188](https://github.com/open-telemetry/opentelemetry-cpp/pull/4188)

Same SDK, different gap: `minimum_severity` and `trace_based` were missing from `LoggerConfig`
in the declarative (YAML) configuration path, so file-configured loggers silently ignored
severity filtering. Added both fields to the parser with spec-aligned defaults, plus
integration tests covering default, explicit-severity, and trace-based filtering.
[Issue #4130](https://github.com/open-telemetry/opentelemetry-cpp/issues/4130) ·
[PR #4131](https://github.com/open-telemetry/opentelemetry-cpp/pull/4131)

The cardinality-limits work had a follow-up gap: a histogram view that set only a cardinality
limit, with no explicit aggregation block, was silently rejected, since the code always built
a plain `AggregationConfig` instead of the `HistogramAggregationConfig` the view registry
requires. Fixing it surfaced a second, subtler bug: a freshly-built config has empty
boundaries, which the aggregation constructors read as "use zero buckets" rather than "use
SDK defaults." Fixed both, and deduplicated the boundary list that three call sites had each
been carrying their own copy of.
[Issue #3292](https://github.com/open-telemetry/opentelemetry-cpp/issues/3292) ·
[PR #4314](https://github.com/open-telemetry/opentelemetry-cpp/pull/4314)

The same class of bug showed up across `opentelemetry-go-contrib`. In `otelmongo`, pooled
connection IDs from the v2 Mongo driver carry a `[-<n>]` suffix that broke host/port parsing,
so the fallback path used the whole per-connection string as the hostname, unbounding
`network.peer.address` cardinality on every long-running process.
[Issue #9275](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9275) ·
[PR #9352](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9352)

In `propagators/aws/xray`, a discarded error from the `crypto/rand` seed read meant every
`IDGenerator` fell back to seed `0` whenever entropy wasn't available, so restricted or
sandboxed environments could emit identical trace and span IDs across instances. Replaced the
manually-seeded generator with `math/rand/v2`'s runtime-seeded globals, while keeping the
now-unused `sync.Mutex` in place to preserve the stable v1 module's public API.
[Issue #9048](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9048) ·
[PR #9359](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9359)

And in `otelhttp`, `network.protocol.version` was read off the outgoing request, which the
standard library always stamps `HTTP/1.1`, so client spans and metrics misreported HTTP/2
connections negotiated over ALPN. Re-sourced it from the response instead, once the true
wire protocol is known, and regenerated all six consumer packages from the shared template.
[Issue #9007](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9007) ·
[PR #9371](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9371)

Outside of contrib, `opentelemetry-go-compile-instrumentation`'s gin package never checked the
runtime enable/disable gate every other instrumentation package used, so
`OTEL_GO_DISABLED_INSTRUMENTATIONS=gin` silently had no effect. Gave gin its own
instrumentation key, since it only enriches an existing HTTP span rather than creating one,
and hardened the before/after hook pair against the env var changing mid-request.
[Issue #839](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/839) ·
[PR #840](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/840)

In GoFr I added ScyllaDB migration support, extending the framework's schema-migration path
beyond relational backends, with a `gomock`-based harness (`MockScyllaDB`) so migration logic
is testable without a live cluster.
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
  <img src="https://raw.githubusercontent.com/om7057/om7057/main/profile-3d-contrib/profile-night-rainbow.svg" alt="3D contribution graph" />
</p>
