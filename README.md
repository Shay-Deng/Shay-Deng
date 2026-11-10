<p align="center">
  <img src="assets/banner.svg" width="100%" alt="Howie Deng — agent protocols, agent SDKs and open source. Build with intent. Go deep." />
</p>

<p align="center">
  <a href="#open-source-contributions">Open-source contributions</a> &nbsp; / &nbsp;
  <a href="https://github.com/Shay-Deng?tab=repositories">Repositories</a> &nbsp; / &nbsp;
  <a href="https://twitter.com/ShayDeng">Connect on X</a>
</p>

<br />

### Agent protocols & SDKs

I work on the plumbing that lets AI agents talk to each other: protocol conformance for **Agent2Agent (A2A)**, and fixes in the agent SDKs people build on. I write in **Java**, **Python** and **TypeScript**, and I like small, well-tested changes that are easy to review.

<p>
  <img alt="Java" src="https://img.shields.io/badge/Java-171b30?style=for-the-badge&amp;logo=openjdk&amp;logoColor=c4b5fd" />
  <img alt="Python" src="https://img.shields.io/badge/Python-171b30?style=for-the-badge&amp;logo=python&amp;logoColor=67e8f9" />
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-171b30?style=for-the-badge&amp;logo=typescript&amp;logoColor=c4b5fd" />
  <img alt="A2A Protocol" src="https://img.shields.io/badge/A2A_Protocol-171b30?style=for-the-badge&amp;logoColor=67e8f9" />
  <img alt="MCP" src="https://img.shields.io/badge/MCP-171b30?style=for-the-badge&amp;logo=modelcontextprotocol&amp;logoColor=c4b5fd" />
  <img alt="Spring AI" src="https://img.shields.io/badge/Spring_AI-171b30?style=for-the-badge&amp;logo=spring&amp;logoColor=67e8f9" />
  <img alt="LangChain4j" src="https://img.shields.io/badge/LangChain4j-171b30?style=for-the-badge&amp;logoColor=c4b5fd" />
  <img alt="pytest" src="https://img.shields.io/badge/pytest-171b30?style=for-the-badge&amp;logo=pytest&amp;logoColor=67e8f9" />
  <img alt="JUnit 5" src="https://img.shields.io/badge/JUnit_5-171b30?style=for-the-badge&amp;logo=junit5&amp;logoColor=c4b5fd" />
</p>

<br />

### Featured work

<table>
<tr><td>
<br />
<strong>01 &nbsp; / &nbsp; A2A PROTOCOL CONFORMANCE</strong>
<h3>Testing agents against the spec, then fixing what the tests find.</h3>
<p>Contributing to the A2A Technology Compatibility Kit (<code>a2a-tck</code>) and running it against the reference Python SDK. One run showed that HTTP+JSON error responses were not served with the A2A media type the spec asks for; I traced it to the shared error handler and fixed it in <code>a2a-python</code>.</p>
<p><code>Protocol specs</code> &nbsp; <code>JSON-RPC · HTTP+JSON · gRPC</code> &nbsp; <code>pytest</code></p>
<p><a href="https://github.com/a2aproject/a2a-python/pull/1446"><strong>a2a-python #1446 →</strong></a> &nbsp; · &nbsp; <a href="https://github.com/a2aproject/a2a-tck/pull/268">a2a-tck #268</a> &nbsp; · &nbsp; <a href="https://github.com/a2aproject/a2a-tck/pull/269">a2a-tck #269</a></p>
<sub>Review status is kept current in the list below.</sub>
<br /><br />
</td></tr>
<tr><td>
<br />
<strong>02 &nbsp; / &nbsp; LANGCHAIN4J COMMUNITY</strong>
<h3>Making streaming failure handling predictable.</h3>
<p>Fixed <code>StreamingModelRouter</code> so that invalid demand signals an error, cancels upstream work and terminates exactly once, then kept native async chat delegation when routing.</p>
<p><code>Reactive Streams</code> &nbsp; <code>Concurrency</code> &nbsp; <code>Regression tests</code></p>
<p><a href="https://github.com/langchain4j/langchain4j-community/pull/792"><strong>#792 →</strong></a> &nbsp; · &nbsp; <a href="https://github.com/langchain4j/langchain4j-community/pull/794">#794</a> &nbsp; · &nbsp; <a href="https://github.com/langchain4j/langchain4j-community/issues/791">Issue #791</a></p>
<sub>Both merged.</sub>
<br /><br />
</td></tr>
</table>

<br />

### Open-source contributions

<!-- oss:start -->
<sub>2 merged &nbsp;·&nbsp; 9 in review &nbsp;·&nbsp; 7 projects &nbsp;·&nbsp; updated daily by <code>scripts/update_readme.py</code></sub>

**Merged**

| Project | Pull request | Merged |
| :-- | :-- | :-- |
| [langchain4j/langchain4j-community](https://github.com/langchain4j/langchain4j-community) | [#794](https://github.com/langchain4j/langchain4j-community/pull/794) feat(model-router): preserve native async chat delegation | 2026&#8209;09&#8209;30 |
| [langchain4j/langchain4j-community](https://github.com/langchain4j/langchain4j-community) | [#792](https://github.com/langchain4j/langchain4j-community/pull/792) fix: terminate streaming router subscriptions on invalid demand | 2026&#8209;09&#8209;16 |

**In review**

| Project | Pull request | Opened |
| :-- | :-- | :-- |
| [a2aproject/a2a-python](https://github.com/a2aproject/a2a-python) | [#1446](https://github.com/a2aproject/a2a-python/pull/1446) fix(rest): serve HTTP+JSON error responses as application/a2a+json | 2026&#8209;11&#8209;10 |
| [a2aproject/a2a-tck](https://github.com/a2aproject/a2a-tck) | [#269](https://github.com/a2aproject/a2a-tck/pull/269) fix(jsonrpc): send camelCase params for push config and ListTasks | 2026&#8209;11&#8209;10 |
| [a2aproject/a2a-tck](https://github.com/a2aproject/a2a-tck) | [#268](https://github.com/a2aproject/a2a-tck/pull/268) fix: give every sent message its own messageId | 2026&#8209;11&#8209;09 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | [#5963](https://github.com/strands-agents/harness-sdk/pull/5963) fix(models)!: reject a pre-built client combined with apiKey or clientConfig in TypeScript | 2026&#8209;11&#8209;09 |
| [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | [#4033](https://github.com/agentscope-ai/agentscope-java/pull/4033) fix(controlplane): let failed managed turns be cancelled to release the session | 2026&#8209;11&#8209;06 |
| [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs) | [#2998](https://github.com/langchain-ai/langgraphjs/pull/2998) fix(sdk): isolate reads using custom fetch implementations | 2026&#8209;10&#8209;10 |
| [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs) | [#2997](https://github.com/langchain-ai/langgraphjs/pull/2997) fix(sdk): avoid stale subagent namespace mappings on hydration | 2026&#8209;10&#8209;10 |
| [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) | [#3413](https://github.com/agentscope-ai/agentscope-java/pull/3413) feat(sandbox): retain E2B sandboxes between calls | 2026&#8209;10&#8209;03 |
| [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) | [#6991](https://github.com/spring-projects/spring-ai/pull/6991) Add opt-in in-index filtering to `Neo4jVectorStore` | 2026&#8209;09&#8209;14 |

<!-- oss:end -->

<br />

### What I'm exploring

| Agent protocols | Agent SDKs | Engineering practice |
| :--- | :--- | :--- |
| A2A conformance & interoperability | Google ADK · Strands Agents · AgentScope | Spec-driven tests |
| MCP integration | LangChain4j · Spring AI | Focused fixes & regression tests |

<br />

---

<p align="center">
  <sub>操千曲而后晓声，观千剑而后识器。</sub><br />
  <sub>Read deeply. Build thoughtfully.</sub>
</p>
