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
| **Merged upstream** | 4 contributions across Prometheus, OpenTelemetry C++ SDK, and GoFr |
| **CNCF ecosystem** | Prometheus and OpenTelemetry are both CNCF **graduated** projects |
| **Focus** | TSDB internals · specification compliance · declarative configuration · migration tooling |
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
The fix ([PR #4264](https://github.com/open-telemetry/opentelemetry-cpp/pull/4264)) also
removed a now-unreachable `!empty()` guard, documented why the caching layer is a `string_view`
lifetime and thread-safety *requirement* rather than an optimization, and added two regression
tests verified to fail without the patch.

Same SDK, different gap: `minimum_severity` and `trace_based` were missing from `LoggerConfig`
in the declarative (YAML) configuration path, so file-configured loggers silently ignored
severity filtering. Added both fields to the parser with spec-aligned defaults, plus
integration tests covering default, explicit-severity, and trace-based filtering.
[PR #4131](https://github.com/open-telemetry/opentelemetry-cpp/pull/4131)

In GoFr I added ScyllaDB migration support, extending the framework's schema-migration path
beyond relational backends, with a `gomock`-based harness (`MockScyllaDB`) so migration logic
is testable without a live cluster.
[PR #2085](https://github.com/gofr-dev/gofr/pull/2085)

---

## Contributions

| Project | Contribution | Links |
|---|---|---|
| **Prometheus** | TSDB querier cleanup swallowed `Close()` failures; used `errors.Join()` to surface concurrent errors on multi-block queries | [PR](https://github.com/prometheus/prometheus/pull/19120) · [Issue](https://github.com/prometheus/prometheus/issues/19114) |
| **OpenTelemetry C++** | `EnvironmentCarrier` spec compliance: empty keys silently resolved to the wrong slot in `NormalizeKey()` | [PR](https://github.com/open-telemetry/opentelemetry-cpp/pull/4264) · [Issue](https://github.com/open-telemetry/opentelemetry-cpp/issues/4190) |
| **OpenTelemetry C++** | Added `minimum_severity` and `trace_based` to the declarative YAML config parser for `LoggerConfig` | [PR](https://github.com/open-telemetry/opentelemetry-cpp/pull/4131) · [Issue](https://github.com/open-telemetry/opentelemetry-cpp/issues/4130) |
| **GoFr** | ScyllaDB migration support with `gomock`-based test infrastructure for schema evolution and rollback | [PR](https://github.com/gofr-dev/gofr/pull/2085) |

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
