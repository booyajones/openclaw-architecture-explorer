# OpenClaw Scaling & Hardware Guide

Hardware matters for OpenClaw, but **not in the way people first assume**.

## The Real Bottlenecks (in order)

1. **LLM/API rate limits**
2. **Gateway concurrency model**
3. **Browser/tool execution**
4. **Memory/context buildup**
5. **External systems latency**
6. **Only then raw CPU/RAM**

The gateway is more like **air traffic control** than the airplane engine. A bigger EC2 box helps, but it doesn't magically turn 2 stable jobs into 200 stable jobs unless the rest of the architecture changes.

## Hardware Recommendations by Scale

### 2 Simultaneous Jobs
One decent Windows EC2 instance is fine:
- 2–4 vCPU
- 8–16 GB RAM

### 20 Jobs
You want queueing, per-job isolation, logging, and retry rules:
- 4–8 vCPU
- 16–32 GB RAM

### 200 Jobs
Do **not** run this as "one OpenClaw gateway with 200 things happening." Instead, separate concerns:

```
OpenClaw gateway = control plane
Workers = execution plane
Queue = traffic manager
LLM provider = rate-limited external dependency
```

## Architecture for 200+ Jobs

```
Requests / schedules
        ↓
Queue: SQS / Redis / Temporal / BullMQ
        ↓
Worker pool
        ↓
OpenClaw sessions / agents / tools
        ↓
LLM APIs, browser automation, files, email, SaaS APIs
```

## Memory Estimation Rules of Thumb

| Job Type | RAM per Job |
|----------|-------------|
| Light text/API job | 100–300 MB |
| Browser job | 500 MB–2 GB |
| Heavy coding/repo job | 1–4 GB |
| Local model inference | GPU/RAM bound (different game) |

**Example:** 200 browser-heavy jobs could require **100–300+ GB RAM** if truly simultaneous. But 200 queued jobs with 10–25 active at a time is very manageable.

## The Right Mental Model

```
Capability = model quality + tool access + permissions + workflows
Throughput = queueing + concurrency + rate limits + hardware
Reliability = isolation + retries + logging + watchdogs
```

**Practical recommendation:** Cap active jobs at a sane number (5–15 concurrent), then scale horizontally with worker instances once you know the job profile.

## Production Architecture Pattern

For enterprise use cases:

- **1 gateway per environment**
- **Multiple worker nodes**
- **Strict job queue**
- **Per-agent concurrency limits**
- **Browser jobs separated from API-only jobs**
- **Central logs**
- **Dead-letter queue**
- **Automatic restart/watchdog**
- **Rate-limit aware LLM router**

## Key Insight

**Hardware affects throughput much more than intelligence.**

A stronger box doesn't make the agent smarter. It lets more sessions, tools, browsers, and file operations run without choking.

For 200 jobs: **Don't buy one monster server first.** Build the queue/worker architecture, then scale workers horizontally.
