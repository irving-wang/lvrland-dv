lvr_code2county = {'C': '基隆市',
                   'A': '臺北市',
                   'F': '新北市',
                   'H': '桃園縣',
                   'O': '新竹市',
                   'J': '新竹縣',
                   'K': '苗栗縣',
                   'B': '臺中市',
                   'M': '南投縣',
                   'N': '彰化縣',
                   'P': '雲林縣',
                   'I': '嘉義市',
                   'Q': '嘉義縣',
                   'D': '臺南市',
                   'E': '高雄市',
                   'T': '屏東縣',
                   'G': '宜蘭縣',
                   'U': '花蓮縣',
                   'V': '臺東縣',
                   'X': '澎湖縣',
                   'W': '金門縣',
                   'Z': '連江縣'}

lvr_county2code = {'基隆市': 'C',
                   '臺北市': 'A',
                   '新北市': 'F',
                   '桃園縣': 'H',
                   '新竹市': 'O',
                   '新竹縣': 'J',
                   '苗栗縣': 'K',
                   '臺中市': 'B',
                   '南投縣': 'M',
                   '彰化縣': 'N',
                   '雲林縣': 'P',
                   '嘉義市': 'I',
                   '嘉義縣': 'Q',
                   '臺南市': 'D',
                   '高雄市': 'E',
                   '屏東縣': 'T',
                   '宜蘭縣': 'G',
                   '花蓮縣': 'U',
                   '臺東縣': 'V',
                   '澎湖縣': 'X',
                   '金門縣': 'W',
                   '連江縣': 'Z'}

lvr_transcation_type = {
    'A': '不動產買賣',
    'B': '預售屋買賣',
    'C': '不動產租賃'}

lvr_columns = ['鄉鎮市區', '交易標的', '土地區段位置或建物區門牌', '土地移轉總面積平方公尺', '都市土地使用分區', '非都市土地使用分區',
               '非都市土地使用編定', '交易年月日', '交易筆棟數', '移轉層次', '總樓層數', '建物型態', '主要用途', '主要建材',
               '建築完成年月', '建物移轉總面積平方公尺', '建物現況格局-房', '建物現況格局-廳', '建物現況格局-衛',
               '建物現況格局-隔間', '有無管理組織', '總價元', '單價每平方公尺', '車位類別', '車位移轉總面積平方公尺', '車位總價元',
               '備註', '編號']

lvr_6city = {
    'A': '臺北市',
    'F': '新北市',
    'H': '桃園縣',
    'B': '臺中市',
    'D': '臺南市',
    'E': '高雄市'}


def get_lvr_csv(path, code):
    return '{0}\\{1}_lvr_land_A.CSV'.format(path, code)
