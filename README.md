# ghpy - Google Hacking with Python
## 安裝環境
Windows 10 x 64  
python 3.11.1 (All User, 預設安裝路徑會在C:\Program Files\Python311)  
Chrome 108.0.5359.125  
## Python相依套件
1. 網頁爬蟲相關
* beautifulsoup4
* requests
* selenium
2. 檔案分析相關(docx, xlsx, pdf ...)
* lxml
* openpyxl
* pandas
* pdfminer.six
* pypiwin32
* python-pptx
* python-docx
* xlrd
3. 其他
* pyproject-toml
* wheel
## 使用
Step 1. 安裝相依套件
```
pip install wheel
pip install pyproject-toml
pip install -r requirements.txt
```
\* 依序以上指令安裝  
\* requirements.txt中 lxml 套件安裝依照存放路徑設定(預設為 file:///C:/ghpy/software/lxml-4.9.0-cp311-cp311-win_amd64.whl)  
  
Step 2. 安裝 Chrome 瀏覽器  
  
Step 3. 使用  
```
python ghpy.py -u <目表Host/IP> -t <輸出檔案格式>
```
\* 輸出檔案格式預設為 xlsx , 目前支援 csv, xlsx  
## 備註
[1] python-docx error : 依環境[下載](https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml) lxml  
  例：Windows 10 x 64 選 lxml‑4.9.0‑cp311‑cp311‑win_amd64.whl   
```
pip install lxml-4.9.0-cp311-cp311-win_amd64.whl
```
[2] path warning : 環境變數加入 path
```
WARNING: The script xxx.exe is installed in 'C:\Users\XXXX\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
```
[3] 環境所需軟體/套件在 software  
[4] google 驗證問題 : ghpy_ap.py 自動切換 proxy   
```
python ghpy_ap.py -u <目標Host/IP> -t <輸出檔案格式>
```
## 問題
ghpy_ap.py 自動切換 proxy 版本使用 Free Proxy 幾乎都會被阻擋.  
