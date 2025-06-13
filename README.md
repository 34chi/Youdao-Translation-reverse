# Youdao-Translation-reverse
有道翻译js，py加密解密源码

### RESEARCH.md 技术报告

```markdown
# 有道翻译加密机制技术报告

## 1. 加密流程概述

有道翻译API采用客户端-服务器混合加密方案：
1. **请求签名**：使用MD5生成请求签名
2. **参数传输**：敏感参数通过POST发送
3. **响应加密**：使用AES-CBC加密返回结果

```mermaid
sequenceDiagram
    participant Client
    participant Server
    Client->>Server: POST /webtranslate (签名参数)
    Server-->>Client: AES加密的响应
    Client->>Client: 解密响应
