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
| **Merged upstream** | OpenTelemetry (C++ SDK, Go Contrib, Go Compile Instrumentation) · Prometheus · Liquibase · GoFr |
| **CNCF ecosystem** | Prometheus and OpenTelemetry are both CNCF **graduated** projects |
| **Focus** | Metrics cardinality · specification compliance · declarative configuration · TSDB internals · migration tooling |
| **Research** | IEEE ICFT 2025, co-author and presenter on metadata exploration across lakehouse table formats |
| **Experience** | Software Engineer working on backend and distributed systems. Previously SDE Intern at CoinSwitch (Go, gRPC, NATS JetStream) and Engineering Intern at ConnectWise (Go, Kafka, Aurora) |

---

## Recent work

A pattern runs through most of what I contribute upstream: software that fails silently rather
than loudly, and my fixes tend to replace a swallowed error or a discarded configuration value
with a deliberate one.

In the **Prometheus TSDB**, querier cleanup was discarding errors returned by `Close()`, so a
failing block surfaced as a successful query with missing data. I introduced `errors.Join()` to
preserve concurrent cleanup failures alongside the primary error ([#19114](https://github.com/prometheus/prometheus/issues/19114),
[#19120](https://github.com/prometheus/prometheus/pull/19120)).

Most of my recent work has been in the **OpenTelemetry C++ SDK**. `EnvironmentCarrier` didn't
normalize empty keys, so `Get("")`/`Set("")` silently touched the wrong slot instead of erroring :
a spec violation I fixed alongside the caching contract's documentation
([#4190](https://github.com/open-telemetry/opentelemetry-cpp/issues/4190), [#4264](https://github.com/open-telemetry/opentelemetry-cpp/pull/4264)).
I also implemented configurable, per-instrument-type cardinality limits for the Metrics SDK,
which previously hardcoded a limit of 2000 and silently discarded any user-supplied override
([#3292](https://github.com/open-telemetry/opentelemetry-cpp/issues/3292), [#4188](https://github.com/open-telemetry/opentelemetry-cpp/pull/4188)) :
along with a follow-up fix for histogram views that set only a cardinality limit, which were
being silently rejected ([#4314](https://github.com/open-telemetry/opentelemetry-cpp/pull/4314)).
Separately, I closed a declarative-configuration gap where `minimum_severity` and `trace_based`
were missing from `LoggerConfig`, causing file-configured loggers to silently ignore severity
filtering ([#4130](https://github.com/open-telemetry/opentelemetry-cpp/issues/4130), [#4131](https://github.com/open-telemetry/opentelemetry-cpp/pull/4131)).

I've since extended the same pattern to the **Go side of OpenTelemetry**. In `opentelemetry-go-contrib`,
I fixed unbounded `network.peer.address` cardinality in `otelmongo` caused by unparsed pooled
connection ID suffixes ([#9275](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9275),
[#9352](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9352)); a determinism bug in the
AWS X-Ray `IDGenerator` where a silently-discarded seed-read error could produce identical trace and
span IDs across instances ([#9048](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9048),
[#9359](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9359)); and a case in `otelhttp`
where `network.protocol.version` was read from the outgoing request rather than the negotiated
response, misreporting HTTP/2 connections as HTTP/1.1 ([#9007](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9007),
[#9371](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9371)). In `opentelemetry-go-compile-instrumentation`,
I fixed the gin package silently ignoring `OTEL_GO_DISABLED_INSTRUMENTATIONS=gin`, since it never
checked the runtime enable/disable gate every other instrumentation package relied on
([#839](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/839),
[#840](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/840)).

In **Liquibase**, a child thread that inherited its parent's `Scope` (via `InheritableThreadLocal`)
could have its MDC log entries wiped out by the parent's `exit()`, since entries were tracked in a
single static map keyed only by scope ID with no notion of which thread owned them. I re-scoped
ownership to a `ThreadLocal<Map<...>>` so each thread only ever cleans up entries it registered
itself, and rewrote my first regression test after review pointed out it never actually exercised
the shared-scope-ID collision the bug depended on
([#7823](https://github.com/liquibase/liquibase/issues/7823), [#7825](https://github.com/liquibase/liquibase/pull/7825)).

In **GoFr**, I added ScyllaDB migration support with a `gomock`-based test harness, extending the
framework's schema-migration path beyond relational backends ([#2085](https://github.com/gofr-dev/gofr/pull/2085)).

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
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=om7057&theme=react-dark&hide_border=true&area=true" alt="commit activity graph" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/om7057/om7057/main/profile-3d-contrib/profile-night-green.svg" alt="3D contribution graph" />
</p>

