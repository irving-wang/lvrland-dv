# lvrland-dv
Data visualization for lvr data 

資料來源為內政部不動產交易實價查詢網： [不動產成交案件實際資訊Open Data](http://plvr.land.moi.gov.tw/DownloadOpenData)

## Open Data

## Data Preprocessing
資料轉檔：

    iconv -c -f big5 -t big5 source.csv > target.csv


## HDFS

## Chart

## 中文字型

1. _%Python Install Dir%_\Lib\site-packages\matplotlib\mpl-data
2. matplotlibrc: remove comment, then add "Microsoft YaHei"
    - font.family         : sans-serif
    - font.sans-serif     : Microsoft YaHei, Bitstream Vera Sans, Lucida Grande...
3. 複製字型
    - source: C:\Windows\Fonts\Microsoft YaHei
    - target: _%Python Install Dir%_\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\Microsoft YaHei

參考: [解決Matplotlib中文亂碼問題](http://www.wnqzw.com/article/9077.html)

### Scatterplot
- 分區成交量
- 分區成交價
- 地區

### Line
- 成交量趨勢
- 成交價趨勢

### Bar
- 分區成交量
- 分區成交價
- 月份統計

### Pie
- 單位面積
- 總面積
- 成交量
- 成交價

## Geographic

