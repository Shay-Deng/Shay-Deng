<p align="center">
  <img src="assets/banner.svg" width="100%" alt="Howie Deng — agent protocols, agent SDKs and open source. Build with intent. Go deep." />
</p>

<p align="center">
  <a href="#open-source">Open source</a> &nbsp; / &nbsp;
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
<br />
</td></tr>
<tr><td>
<br />
<strong>02 &nbsp; / &nbsp; MERGED UPSTREAM</strong>
<h3>Small, tested fixes in agent SDKs.</h3>
<p><strong>Google ADK</strong>: kept empty signed thinking blocks intact when replaying Claude conversation history, so multi-turn tool calls send the model exactly what it returned.</p>
<p><strong>LangChain4j</strong>: made <code>StreamingModelRouter</code> signal an error, cancel upstream work and terminate exactly once on invalid demand, and kept native async chat delegation when routing.</p>
<p><code>Python</code> &nbsp; <code>Java · Reactive Streams</code> &nbsp; <code>Regression tests</code></p>
<p><a href="https://github.com/google/adk-python/pull/7500"><strong>Google ADK #7500 →</strong></a> &nbsp; · &nbsp; <a href="https://github.com/langchain4j/langchain4j-community/pull/792">LangChain4j #792</a> &nbsp; · &nbsp; <a href="https://github.com/langchain4j/langchain4j-community/pull/794">#794</a></p>
<br />
</td></tr>
</table>

<br />

### Open source

<!-- oss:start -->
**Merged upstream:** [Google ADK](https://github.com/search?q=is%3Apr%20author%3AShay-Deng%20org%3Agoogle&type=pullrequests) · [LangChain4j](https://github.com/search?q=is%3Apr%20author%3AShay-Deng%20org%3Alangchain4j&type=pullrequests)<br />
**In review:** [A2A](https://github.com/search?q=is%3Apr%20author%3AShay-Deng%20org%3Aa2aproject&type=pullrequests) · [Strands Agents](https://github.com/search?q=is%3Apr%20author%3AShay-Deng%20org%3Astrands-agents&type=pullrequests) · [AgentScope](https://github.com/search?q=is%3Apr%20author%3AShay-Deng%20org%3Aagentscope-ai&type=pullrequests) · [LangGraph.js](https://github.com/search?q=is%3Apr%20author%3AShay-Deng%20org%3Alangchain-ai&type=pullrequests) · [Spring AI](https://github.com/search?q=is%3Apr%20author%3AShay-Deng%20org%3Aspring-projects&type=pullrequests)
<!-- oss:end -->

<br />

---

<p align="center">
  <sub>操千曲而后晓声，观千剑而后识器。</sub><br />
  <sub>Read deeply. Build thoughtfully.</sub>
</p>
