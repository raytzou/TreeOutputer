### 資料夾樹狀結構輸出小程式

ChatGPT 產的程式碼\
覺得不錯就推上來了，有時候編寫特定的專案的文件，或是需要提供非專案的資料夾結構\
這樣的小工具就挺方便的

## 使用方式

直接使用 cmd 執行即可
```bash
python .\tree_md.py
```
接著輸入 **目錄完整位置** 和 **查詢的深度**
```bash
請輸入完整資料夾路徑：E:\foo\bar\example
請輸入查詢深度 (0=只顯示當前層, 1=包含子資料夾, 以此類推)：0
樹狀結構已儲存到：E:\currentDir\tree.txt
```
程式就會在當前資料夾內生成tree.txt
```
.  # 來自 E:\foo\bar\example
├── inner
│   └── innerfile.txt
├── README.md
└── tree_md.py
```