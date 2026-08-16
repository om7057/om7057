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
| **Merged upstream** | OpenTelemetry (C++ SDK, Go SDK, Go Contrib, Go Compile Instrumentation) · Prometheus · Liquibase · Apicurio Registry · GoFr |
| **CNCF ecosystem** | Prometheus and OpenTelemetry are both CNCF **graduated** projects |
| **Focus** | Metrics cardinality · specification compliance · declarative configuration · TSDB internals · migration tooling |
| **Research** | IEEE ICFT 2025, co-author and presenter on metadata exploration across lakehouse table formats |
| **Experience** | Software Engineer working on backend and distributed systems. Previously SDE Intern at CoinSwitch (Go, gRPC, NATS JetStream) and Engineering Intern at ConnectWise (Go, Kafka, Aurora) |

---

## Recent work

A pattern runs through most of what I contribute upstream: software that fails silently rather
than loudly, and my fixes tend to replace a swallowed error or a discarded configuration value
with a deliberate one.

**Prometheus TSDB** : querier cleanup swallowed `Close()` errors, masking failed blocks as
successful queries; fixed with `errors.Join()`
([#19114](https://github.com/prometheus/prometheus/issues/19114), [#19120](https://github.com/prometheus/prometheus/pull/19120)).
Also fixed IONOS service discovery panicking when the API omitted optional server fields
([#19417](https://github.com/prometheus/prometheus/issues/19417), [#19418](https://github.com/prometheus/prometheus/pull/19418)).

**OpenTelemetry C++ SDK** : normalized `EnvironmentCarrier`'s empty-key handling, a spec violation
([#4190](https://github.com/open-telemetry/opentelemetry-cpp/issues/4190), [#4264](https://github.com/open-telemetry/opentelemetry-cpp/pull/4264));
added configurable per-instrument-type cardinality limits to the Metrics SDK, plus a follow-up fix
for histogram views that silently rejected cardinality-only configs
([#3292](https://github.com/open-telemetry/opentelemetry-cpp/issues/3292), [#4188](https://github.com/open-telemetry/opentelemetry-cpp/pull/4188), [#4314](https://github.com/open-telemetry/opentelemetry-cpp/pull/4314));
closed a config gap where `LoggerConfig` silently ignored severity filtering
([#4130](https://github.com/open-telemetry/opentelemetry-cpp/issues/4130), [#4131](https://github.com/open-telemetry/opentelemetry-cpp/pull/4131)).

**OpenTelemetry Go** : fixed unbounded `network.peer.address` cardinality in `otelmongo`
([#9275](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9275), [#9352](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9352)),
a determinism bug in the X-Ray `IDGenerator`
([#9048](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9048), [#9359](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9359)),
`otelhttp` misreporting HTTP/2 as HTTP/1.1
([#9007](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9007), [#9371](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9371)),
and a dropped aggregate baggage-parse error in the `ot` propagator
([#9047](https://github.com/open-telemetry/opentelemetry-go-contrib/issues/9047), [#9395](https://github.com/open-telemetry/opentelemetry-go-contrib/pull/9395)).
In the core SDK, reenabled the `context-as-argument` linter repo-wide after clearing its last
holdouts ([#3372](https://github.com/open-telemetry/opentelemetry-go/issues/3372), [#8718](https://github.com/open-telemetry/opentelemetry-go/pull/8718)).
In the compile-time instrumentation tool: a runtime enable/disable gate missing from gin's
instrumentation ([#839](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/839), [#840](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/840)),
a dropped final SSE chunk in the OpenAI streaming reader
([#827](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/827), [#828](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/828)),
a blank-receiver method that generated invalid trampoline code
([#798](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/798), [#799](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/799)),
de-duplicated the OpenAI streaming reader across three SDK versions
([#958](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/issues/958), [#990](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/990)),
and a mis-scoped Codecov flag that was blocking unrelated PRs
([#857](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation/pull/857)).

**Liquibase** : fixed a race where a child thread's MDC log entries could be wiped out by a
parent thread's scope `exit()`, by re-scoping ownership to a per-thread map
([#7823](https://github.com/liquibase/liquibase/issues/7823), [#7825](https://github.com/liquibase/liquibase/pull/7825)).
Also fixed a changelog lock released by a command step that never acquired it, by tracking
acquisition separately from existence ([#5438](https://github.com/liquibase/liquibase/issues/5438), [#7886](https://github.com/liquibase/liquibase/pull/7886)).

**Apicurio Registry** : added integration test coverage for contract events that had none
([#8858](https://github.com/Apicurio/apicurio-registry/issues/8858), [#8860](https://github.com/Apicurio/apicurio-registry/pull/8860)).

**GoFr** : added ScyllaDB migration support with a `gomock`-based test harness
([#2085](https://github.com/gofr-dev/gofr/pull/2085)).

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

