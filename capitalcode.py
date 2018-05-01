# -*- coding: utf-8 -*-

CapitalCode = {
    1000:['SK_ERROR_LOGIN_FIRST','請先由Center 進行登入動作'],
    1001:['SK_ERROR_INITIALIZE_FAIL','登入失敗，請由LOG查看失敗原因。'],
    1002:['SK_ERROR_ACCOUNT_NOT_EXIST','交易帳號不存在。'],
    1003:['SK_ERROR_ACCOUNT_MARKET_NOT_MATCH','下單帳號類型不正確，是否有證券帳號下期貨之情行。'],
    1004:['SK_ERROR_PERIOD_OUT_OF_RANGE','PERIOD 超出選擇範圍。'],
    1005:['SK_ERROR_FLAG_OUT_OF_RANGE','FLAG 超出選擇範圍。'],
    1006:['SK_ERROR_BUYSELL_OUT_OF_RANGE','BUYSELL 超出選擇範圍。'],
    1007:['SK_ERROR_ORDER_SERVER_INVALID','下單主機不存在。'],
    1008:['SK_ERROR_PERMISSION_DENIED','權限不足，請確認API權限已開通'],
    1009:['SK_ERROR_TRADE_TYPR_OUT_OF_RANGE','TRADE TYPE 超出選擇範圍。'],
    1010:['SK_ERROR_DAY_TRADE_OUT_OF_RANGE','DAY TRADE超出選擇範圍。'],
    1011:['SK_ERROR_ORDER_SIGN_INVALID',''],
    1012:['SK_ERROR_NEW_CLOSE_OUT_OF_RANGE','NEW CLOSE 超出選擇範圍。'],
    1013:['SK_ERROR_PRODUCT_INVALID','下單商品不存在。'],
    1014:['SK_ERROR_QTY_INVALID','單量錯誤，請確認是否為數字。'],
    1015:['SK_ERROR_DAYTRADE_DENIED','商品不支援當沖'],
    1016:['SK_ERROR_SPCIAL_TRADE_TYPE_INVALID','商品不支援該下單類型。'],
    1017:['SK_ERROR_PRICE_INVALID','下單價格錯誤。'],
    1018:['SK_ERROR_INDEX_OUT_OF_RANGE','INDEX 超出選擇範圍。'],
    1019:['SK_ERROR_QUERY_IN_PROCESSING','查詢尚未結束請稍後再試。'],
    1020:['SK_ERROR_LOGIN_INVALID',''],
    1021:['SK_ERROR_REGISTER_CALLBACK',''],
    1022:['SK_ERROR_FUNCTION_PERMISSION_DENIED',''],
    1023:['SK_ERROR_MARKET_OUT_OF_RANGE','MARKET 超出選擇範圍。'],
    1024:['SK_ERROR_PERMISSION_TIMEOUT','太久未使用API，請重新申請權限開放。'],
    1025:['SK_ERROR_FOREIGNSTOCK_PRICE_OUT_OF_RANGE',''],
    1026:['SK_ERROR_FOREIGNSTOCK_UNDEFINE_COINTYPE',''],
    1027:['SK_ERROR_FOREIGNSTOCK_SAME_COINSTYPE',''],
    1028:['SK_ERROR_FOREIGNSTOCK_SALE_SHOULD_ORIGINAL_COIN',''],
    1029:['SK_ERROR_FOREIGNSTOCK_TRADE_UNIT_INVALID',''],
    1030:['SK_ERROR_FOREIGNSTOCK_STOCKNO_INVALID',''],
    1031:['SK_ERROR_FOREIGNSTOCK_ACCOUNTTYPE_INVALID',''],
    1032:['SK_ERROR_FOREIGNSTOCK_INITIALIZE_FAIL',''],
    1033:['SK_ERROR_TS_INITIALIZE_FAIL',''],
    1034:['SK_ERROR_OVERSEA_TRADE_PRODUCT_FAIL',''],
    1035:['SK_ERROR_OVERSEA_TRADE_DATA_NOT_COMPLETE','海期交易商品尚未初使完成，請先執行SKOrderLib_LoadOSCommodity'],
    1036:['SK_ERROR_CERT_VERIFY_CN_INVALID','憑證CN錯誤，'],
    1037:['SK_ERROR_CERT_VERIFY_SERVER_REJECT','憑證驗章失敗，請確認憑證有效性'],
    1038:['SK_ERROR_CERT_NOT_VERIFIED','憑證尚未驗章，請先執行ReadCertByID'],
    1039:['SK_ERROR_OVERSEA_ACCOUNT_NOT_EXIST','海期帳號不存在。'],
    1040:['SK_ERROR_ORDER_LOCK','下單上鎖，請先執行UnlockOrder進行解鎖。'],
    1041:['SK_ERROR_SERVER_NOT_CONNECTED','與主機尚未連線。'],
    1042:['SK_ERROR_OVERSEA_KLINE_DATA_TYPE_NOT_FOUND','KLINE TYPE超出選擇範圍。'],
    1043:['SK_ERROR_STRIKEPRICE_INVALID','履約價不正確。'],
    1044:['SK_ERROR_CALLPUT_INVALID','CALL PUT 不正確。'],
    1045:['SK_ERROR_CERT_NOT_FOUND','憑證不存在，請先匯入憑證到IE 中。'],
    1046:['SK_ERROR_RESERVED_OUT_OF_RANGE','委託盤別超出範圍'],
    1047:['SK_ERROR_SMART_TRADE_ORDER_SERVER_INVALID','智慧單中台主機不存在'],
    1048:['SK_ERROR_CANCEL_ORDER_SMARTKEY_INVALID','智慧單(停損單)序號為無效值'],
    1049:['SK_ERROR_OVERSEA_FUTURE_SPREAD_ORDER','海期價差委託時，（價格為非０數值）出現分子填入負號之錯誤'],
    1050:['待補','待補'],
    2001:['SK_WARNING_OF_COM_DATA_MISSING','海期交易商品檔下載失敗'],
    2002:['SK_WARNING_TS_READY',''],
    2003:['SK_WARNING_LOGIN_ALREADY','ID已登入，無需重覆登入。'],
    2004:['SK_WARNING_LOGIN_SPECIAL_ALREADY',''],
    2005:['SK_WARNING_CERT_VERIFIED_ALREADY','驗章已過，無需重覆驗章。'],
    2006:['SK_WARNING_ORDER_DID_NOT_LOCKED','下單市埸未上鎖。'],
    2007:['SK_WARNING_OO_COM_QUOTEDATA_MISSING','海選商品檔下載失敗'],
    2008:['SK_WARNING_OO_COM_ORDERDATA_MISSING','海選交易商品檔下載失敗'],
    3001:['SK_SUBJECT_CONNECTION_CONNECTED','連線'],
    3002:['SK_SUBJECT_CONNECTION_DISCONNECT','斷線'],
    3003:['SK_SUBJECT_CONNECTION_STOCKS_READY','報價商品載入完成'],
    3004:['SK_SUBJECT_CONNECTION_CLEAR',''],
    3005:['SK_SUBJECT_CONNECTION_RECONNECT',''],
    3006:['SK_SUBJECT_QUOTE_PAGE_EXCEED','PageNo 大於上限'],
    3007:['SK_SUBJECT_QUOTE_PAGE_INCORRECT',''],
    3008:['SK_SUBJECT_TICK_PAGE_EXCEED','Tick PageNo 大於上限'],
    3009:['SK_SUBJECT_TICK_PAGE_INCORRECT',''],
    3010:['SK_SUBJECT_TICK_STOCK_NOT_FOUND','Tick 商品不存在'],
    3011:['SK_SUBJECT_BEST5_DATA_NOT_FOUND','商品五檔不存在'],
    3012:['SK_SUBJECT_QUOTEREQUEST_NOT_FOUND',''],
    3013:['SK_SUBJECT_SERVER_TIME_NOT_FOUND',''],
    3015:['SK_SUBJECT_ALL_MARKET_OK',''],
    3016:['SK_SUBJECT_MARKET_INFO_READY',''],
    3017:['SK_SUBJECT_CATALOG_LIST_READY',''],
    3018:['SK_SUBJECT_INITIALIZESTOCKS',''],
    3019:['SK_SUBJECT_MACD_DATA_NOT_FOUND','MACD不存在'],
    3020:['SK_SUBJECT_BOOLTUNEL_DATA_NOT_FOUND','BOOL通道不存在'],
    3021:['SK_SUBJECT_CONNECTION_FAIL_WITHOUTNETWORK','網路斷線'],
    3022:['SK_SUBJECT_CONNECTION_SOLCLIENTAPI_FAIL','(無網路)連線錯誤'],
    3023:['SK_SUBJECT_STOCKNO_IS_INVALID','商品代碼無效'],
    3024:['SK_SUBJECT_MARKET_NO_IS_OUT_OF_RANGE','國內市場代碼超出範圍 (0~4)'],
    151: ['SK_ERROR_LOGIN_WRONG_PASSWORD','密碼錯誤'],
    152: ['SK_ERROR_LOGIN_WRONG_PASSWORD_OVER_LIMIT','密碼輸入錯誤次數超過上限'],
    153: ['SK_ERROR_LOGIN_WRONG_ID ','您輸入的資料錯誤！請輸入正確的身份證字號'],
    4001:['SK_KLINE_DATA_TYPE_NOT_FOUND','KLINE TYPE 超出選擇範圍。'],
    151: ['SK_ERROR_LOGIN_WRONG_PASSWORD',''],
    152: ['SK_ERROR_LOGIN_WRONG_PASSWORD_OVER_LIMIT ',''],
    153: ['SK_ERROR_LOGIN_WRONG_ID ',''],
    9999:['SK_FAIL',''],
    0   :['SK_SUCCESS', '成功']
}

CapitalMarket = {
    0: '上市',
    1: '上櫃',
    2: '期貨',
    3: '選擇權',
    4: '興櫃'
}
