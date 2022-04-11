
import math 
# 計算モジュールのインポート
# sin,cos,tan利用のため

for i in range(0,360,15): # 0度から345度まで15度ずつ繰り返す
    print(f"角度が{i}°の時")
    rad = math.radians(i) # 角度をラジアンに変換
    print(f"con({i}°)は{round(math.cos(rad),4)}") #少数第4位まで表示する
    print(f"sin({i}°)は{round(math.sin(rad),4)}")
    
    if(i in [90,270]): # tanの定義域処理
        print(f"tan{i}°は定義されてない")
    else:
        print(f"tan({i}°)は{round(math.tan(rad),4)}")
    
print('''
以下、角度が360以上の時
sin(角度÷360のあまり)
cos(角度÷360のあまり)
tan(角度÷360のあまり)
と等しくなる
''')