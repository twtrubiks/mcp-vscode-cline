# 用 Cline 在 VSCode 玩轉 Model Context Protocol (MCP)  🚀

* [Youtube Tutorial - 用 Cline 在 VSCode 玩轉 Model Context Protocol (MCP)(等待新增)]()

## MCP 到底是什麼？ 🤔

MCP 的全名是 Model Context Protocol。簡單說，它就像是 AI 界的 USB Type-C 🔌 ✨

想想看以前，手機、電腦、平板，每種都要不同的充電線和插頭，超麻煩對吧 😩

USB Type-C 出來後，一條線搞定很多事.

MCP 也是類似的概念，它想給 AI 一個通用的溝通方式，讓 AI 可以很方便地去發現、搞懂、然後使用外部的工具或服務。

這樣有啥好處？ 💡

開發者就不用再為了接不同的 AI 或工具，一直去研究那些 API 參數。

而且，AI 自己也能更聰明，看情況決定要用哪個工具來幫忙.

## MCP 跟 Function Calling 有啥不同？

你可能聽過 Function Calling( N8N 的 AI Agent 比較類似這個)，那也能讓 AI 去叫外面的功能。

但 MCP 又更靈活一點！

Function Calling 通常是你得先告訴 AI 有哪些功能可以用，像個菜單一樣。

但 MCP 更像是讓 AI 自己主動去看看周圍 (Context) 有哪些工具可以用，然後自己決定要怎麼用。

## 流程圖

下面這張圖，大約就是你在 VSCode 用 Cline 跟 AI 聊天時，背後 MCP 在忙什麼：

```mermaid
graph LR
    A[使用者在 VSCode 中 <br> 透過 Cline 輸入指令] --> B[大型語言模型<br>接收指令]
    B --> C{AI 需要外部工具<br>或資訊？}
    C -- 是 --> D["AI 透過 MCP<br>找可用的工具"]
    D --> E[AI 選擇合適的工具<br>並透過 MCP 呼叫]
    E --> F[外部工具/伺服器<br>執行任務]
    F --> G[AI 接收工具<br>回傳的結果]
    C -- 否 --> G
    G --> H[AI 整合資訊<br>產生最終回覆]
    H --> I[結果顯示在<br>VSCode Cline 介面中]
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#f9d,stroke:#333,stroke-width:2px,shape:diamond
    style D fill:#9cf,stroke:#333,stroke-width:2px
    style E fill:#9cf,stroke:#333,stroke-width:2px
    style F fill:#9cf,stroke:#333,stroke-width:2px
```

## Cline

透過 [Cline](https://github.com/cline/cline), 其實就是一個 VSCode 的擴充功能

目前已經很非常多 [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

很多 MCP 的工具或伺服器都是用 Python或 Node.js 寫的, 所以建議大家可以先安裝.

[下載 Node.js](https://nodejs.org/zh-tw/download)

```cmd
# 下載並安裝 nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# 下載並安裝 Node.js:
nvm install 22

# 核對 Node.js 版本:
node -v # 應會印出 "v22.14.0"。
nvm current # 應會印出 "v22.14.0"。

# 核對 npm 版本：
npm -v # 應會印出 "10.9.2"。
```

![alt tag](https://i.imgur.com/sNRejaQ.png)