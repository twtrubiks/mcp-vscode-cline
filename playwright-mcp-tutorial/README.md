# Playwright MCP

* [Youtube Tutorial - 複雜爬蟲掰掰！Playwright MCP + AI 輕鬆實現 PTT 圖片自由！(等待新增)](xxx)

playwright 在 [深入 browser-use 的多模態自動化革命](https://github.com/twtrubiks/browser-use-tutorial) 這邊和大家提過了, 今天單獨來使用它.

[playwright-mcp](https://github.com/microsoft/playwright-mcp)

## Running on Linux - Standalone MCP server

安裝 playwright, 這邊使用 npx,

```cmd
npx @playwright/mcp@latest --port 8931
```

然後設定 `SSE` endpoint, 到你的 Vscode

```json
{
  "mcpServers": {
    "playwright": {
      "url": "http://localhost:8931/sse"
    }
  }
}
```

## 流程

以前抓圖片非常辛苦, 尤其是要解析網頁 tag, 可參考我以前寫的 [PTT圖片下載器 (Python) For Windows and Linux](https://github.com/twtrubiks/PTT_Beauty_Spider/tree/master).

現在我們把抓取圖片網址並解析這個麻煩的部份給 AI 處理, 我們只負責下載圖片, 流程如下,

透過 Prompt 讓 Playwright MCP 抓 PTT 表特板的圖片網址, 將抓取到的圖片網址保存到文字檔, 接著讓 AI 將文字檔的網址透過我們寫的 `app.py` 去完成圖片的下載(分批慢慢下載).

```mermaid
flowchart TD
    A[使用者提供 Prompt] --> B["Playwright MCP (抓 PTT 表特板的圖片網址)"];
    B -- "1.存取 PTT 表特板並提取圖片網址" --> PTT["(PTT 表特板)"];
    PTT -- "圖片網址" --> B;
    B -- "2.將抓取到的圖片網址保存至" --> TXT["文字檔 (img.txt)"];
    TXT -- "3.文字檔的網址提供給" --> AI_CONTROLLER["AI"];
    AI_CONTROLLER -- "4.依照我們寫的 app.py<br>    去完成圖片下載<br>    (分批慢慢下載)" --> APP_EXECUTION["下載任務執行<br>(透過 app.py)"];
    APP_EXECUTION --> IMG["下載圖片"];

    classDef promptNode fill:#fffde7,stroke:#ffc107,stroke-width:2px,color:#333;
    classDef mcpNode fill:#e3f2fd,stroke:#2196f3,stroke-width:2px,color:#333;
    classDef pttNode fill:#e0f7fa,stroke:#00bcd4,stroke-width:2px,color:#333;
    classDef fileNode fill:#fce4ec,stroke:#e91e63,stroke-width:2px,color:#333;
    classDef aiNode fill:#dcedc8,stroke:#8bc34a,stroke-width:2px,color:#333;
    classDef execNode fill:#ede7f6,stroke:#673ab7,stroke-width:2px,color:#333;
    classDef imageNode fill:#e8f5e9,stroke:#4caf50,stroke-width:2px,color:#333;

    class A promptNode;
    class B mcpNode;
    class PTT pttNode;
    class TXT fileNode;
    class AI_CONTROLLER aiNode;
    class APP_EXECUTION execNode;
    class IMG imageNode;
```

## Prompt

請參考 [00-doc.md](.clinerules/00-doc.md)

## 注意事項

如果你要用最新板的 cline, 會有讀不到 terminal 輸出的問題, 請參考 [https://github.com/cline/cline/issues/3445#issuecomment-2901994208](https://github.com/cline/cline/issues/3445#issuecomment-2901994208)

建議直接把 cline 預設的 terminal 改成 zsh.

如果你要持續在背景執行任務, 請使用 `nohup`

他的全名是 "no hang up"，意思是「不要中斷」.

主要功能是讓您執行的指令或程式在您登出系統或關閉終端機後，仍然可以繼續在背景執行，

不會因為 SIGHUP (hangup) 訊號而被終止.

`nohup python app.py "https://xxxxx.jpeg" &`

或是把它寫入檔案中(因為我們要用輸出判斷成功或失敗, 這邊是使用這個方法)

`python app.py "https://xxxxx.jpeg" > my_output.log 2>&1 &`

## 結論

基本上, 你要用在 Cursor, Windsurf, Claude 這類都沒問題.

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡  :laughing:

綠界科技ECPAY ( 不需註冊會員 )

![alt tag](https://payment.ecpay.com.tw/Upload/QRCode/201906/QRCode_672351b8-5ab3-42dd-9c7c-c24c3e6a10a0.png)

[贊助者付款](http://bit.ly/2F7Jrha)

歐付寶 ( 需註冊會員 )

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## 贊助名單

[贊助名單](https://github.com/twtrubiks/Thank-you-for-donate)

## License

MIT license
