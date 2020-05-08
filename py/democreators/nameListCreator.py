import random
'''リストにある名前と苗字を組み合わせてでたらめなお名前を大量作成するツール
'''

# 苗字
last_names = [
 '佐藤', '鈴木', '高橋', '田中', '伊藤', '渡辺', '山本', '中村', '小林', '加藤', '吉田', '山田', '佐々木', '山口', '松本', '井上', '木村', '林', '斎藤', '清水',
 '山崎', '森', '池田', '橋本', '阿部', '石川', '山下', '中島', '石井', '小川', '前田', '岡田', '長谷川', '藤田', '後藤', '近藤', '村上', '遠藤', '青木', '坂本',
 '斉藤', '福田', '太田', '西村', '藤井', '岡本', '金子', '藤原', '三浦', '中野', '中川', '原田', '松田', '竹内', '小野', '田村', '中山', '和田', '石田', '森田',
 '上田', '原', '内田', '柴田', '酒井', '宮崎', '横山', '高木', '安藤', '宮本', '大野', '小島', '谷口', '工藤', '今井', '高田', '増田', '丸山', '杉山', '村田',
 '大塚', '新井', '小山', '平野', '藤本', '河野', '上野', '武田', '野口', '松井', '千葉', '菅原', '岩崎', '木下', '久保', '佐野', '野村', '松尾', '菊地', '市川',
 '杉本', '古川', '大西', '島田', '水野', '桜井', '高野', '渡部', '吉川', '山内', '西田', '飯田', '菊池', '西川', '小松', '北村', '安田', '五十嵐', '川口',
 '平田', '関', '中田', '久保田', '服部', '東', '岩田', '川崎', '土屋', '福島', '本田', '辻', '樋口', '秋山', '田口', '永井', '山中', '中西', '吉村', '川上',
 '石原', '大橋', '松岡', '浜田', '馬場', '森本', '矢野', '浅野', '星野', '松下', '大久保', '吉岡', '小池', '野田', '荒木', '大谷', '松浦', '熊谷', '内藤',
 '黒田', '尾崎', '川村', '永田', '望月', '松村', '田辺', '堀', '荒井', '大島', '菅野', '平井', '早川', '西山', '栗原', '広瀬', '横田', '石橋', '岩本', '萩原',
 '片山', '関口', '宮田', '大石', '本間', '高山', '須藤', '吉野', '岡崎', '小田', '伊東', '鎌田', '篠原', '上原', '小西', '松原', '福井', '古賀', '成田', '大森',
 '小泉', '南', '奥村', '内山', '沢田', '桑原', '三宅', '片岡', '川島', '富田', '杉浦', '岡', '奥田', '八木', '小沢', '松永', '北川', '河合', '平山', '関根',
 '牧野', '白石', '今村', '寺田', '青山', '中尾', '小倉', '渋谷', '上村', '小野寺', '大山', '岡村', '足立', '坂口', '天野', '多田', '佐久間', '根本', '豊田'
]
# 名前
first_names = [
 '大翔', '樹', '悠真', '翔', '湊', '蓮', '悠人', '悠斗', '新', '颯太', '楓', '莉子', '凛', '美月', '杏奈', '陽菜', '詩織', '碧', 'あかり', 'すみれ', '瑛太',
 '大和', '陸', '陽太', '蒼太', '陽翔', '駿', '隼人', '悠太', '悠翔', '陸斗', '颯', '陽', '海斗', '陽斗', '翼', '瑛斗', '奏太', '柊', '翔太', '歩', '航',
 '大輝', '智也', '隼', '颯真', '陽葵', '匠', '仁', '誠', '奏汰', '蒼大', '遥斗', '和真', '健人', '大河', '湊太', '理人', '瑛大', '健太', '航太', '大地',
 '大智', '斗真', '陽仁', '琉生', '龍之介', '啓太', '健', '巧', '創', '奏和', '蒼汰', '大雅', '拓海', '拓実', '拓真', '陽人', '一真', '瑛士', '慶', '結斗',
 '元', '航希', '俊介', '聡太', '蒼真', '智哉', '篤人', '湊斗', '唯斗', '陽輝', '陸人', '諒', '櫂', '一輝', '岳', '寛人', '慶太', '健斗', '賢人', '玄',
 '航大', '朔太郎', '丞', '真', '大樹', '歩夢', '優人', '陽真', '結衣', '美咲', '杏', '咲良', '芽衣', '玲奈', '葉月', '愛莉', '結月', 'ひかり', '千尋', '美羽',
 '遥', '澪', '花音', '華', '芽依', '莉緒', '結菜', '怜奈', 'さくら', '咲希', '美結', '美織', '蘭', '莉央', '琴葉', '朱莉', '美桜', '楓花', 'すず', 'はな',
 '愛梨', '紬', '美怜', '唯', '莉乃', 'ひまり', '杏菜', '花', '琴乃', '桜子', '優奈', '栞', 'みのり', '茜', '一花', '希', '彩乃', '咲', '詩', '七海', '紗良',
 '心結', '真央', '美玲', '穂乃香', '優月', '鈴', 'はるか', 'めい', '花奈', '芽生', '環', '琴音', '彩羽', '桜', '汐莉', '紗衣', '紗奈', '千紗', '美緒', '未来',
 'ひな', '一華', '果穂', '彩香', '実咲', '渚', '翠', '日和', '百花', '明莉', '優', '悠月', '梨乃', '理子', '鈴夏', '和花', '栞奈'
]

# 作成する数
sample_count = 47

cnt = 0
# お名前生成
while cnt <= sample_count:
    last_name = random.choice(last_names)
    first_name = random.choice(first_names)
    print(last_name + first_name)

    cnt = cnt + 1

print('end: ' + str(cnt-1))
