import time
import datetime
import os
import random

data_num = 0
data_list = []

koushin_zikoku = "nothing"


hun = 5
koshin_time = hun *60





def generate_ren1():
    a = random.randint(1,10)
    n = random.randint(4,15)
    d = random.randint(1,10)
    #x番目について
    x = random.randint(5,100)
    suretu = []
    for i in range(n):
        an = a + i * d
        suretu.append(an)
    return suretu,d,sum(suretu),x,a+(x-1)*d


def write2():
    q_mode = random.randint(1,2)
    global f
    global a
    global koushin_zikoku
    suretu,sa,gokei,n_ban,n_ban_kou = generate_ren1()
    toi = ["公差","和",f"{n_ban}番目の項"]
    f.write('const question_code = document.getElementById("q_code");\n')
    f.write('const question_mon1 = document.getElementById("q_mon1");\n')
    f.write('const question_mon2 = document.getElementById("q_mon2");\n')
    f.write('const question_mon3 = document.getElementById("q_mon3");\n')
    f.write('const question_time = document.getElementById("q_time");')
    mon_code = random.randint(10000,99999)
    ddd = random.randint(0,2)
    f.write(f'question_code.textContent = "問題コード: B{ddd}{mon_code}";\n')
    toi_info = toi[ddd]
    f.write(f'question_mon1.textContent = "次のような等差数列がある．";\n')
    f.write(f'question_mon2.textContent = "{suretu}";\n')
    mode_data = ["中央値","平均値"]
    f.write(f'question_mon3.textContent = "このとき，この数列の{toi_info}を求めなさい．";\n')
    f.write(f'question_time.textContent = "更新:{koushin_zikoku.strftime("%Y/%m/%d %H:%M:%S")}";\n')
    ans = [sa,gokei,n_ban_kou]
    a.write(f'var ans = {ans[ddd]}\n')
    log.write(f'問題コード: B{ddd}{mon_code}\n 次のような等差数列がある．\n{suretu}\nこのとき，この数列の{toi_info}を求めなさい．\n 更新:{koushin_zikoku.strftime("%Y/%m/%d %H:%M:%S")} 答え:{ans[ddd]}\n\n')




def write_open():
    global f
    global a
    global log
    f = open('test.js','w')
    a = open('ans.js','w')
    log = open('log.txt','a')
    
def write():
    q_mode = random.randint(1,2)
    global f
    global a
    global koushin_zikoku
    kamoku = ["C演習","テクニカルライティング","教育学","基本情報処理","教育工学基礎","教育方法論・教育技法"]
    f.write('const question_code = document.getElementById("q_code");\n')
    f.write('const question_mon1 = document.getElementById("q_mon1");\n')
    f.write('const question_mon2 = document.getElementById("q_mon2");\n')
    f.write('const question_mon3 = document.getElementById("q_mon3");\n')
    f.write('const question_time = document.getElementById("q_time");')
    mon_code = random.randint(10000,99999)
    f.write(f'question_code.textContent = "問題コード: A{q_mode}{mon_code}";\n')
    kamoku_info = kamoku[random.randint(0,5)]
    f.write(f'question_mon1.textContent = "今回行われた{kamoku_info}の試験の結果は以下のようになった.";\n')
    q = generate_question()
    f.write(f'question_mon2.textContent = "{q}";\n')
    mode_data = ["中央値","平均値"]
    f.write(f'question_mon3.textContent = "このとき，この試験の点数の{mode_data[q_mode-1]}を小数点第１位まで求めなさい．";\n')
    f.write(f'question_time.textContent = "更新:{koushin_zikoku.strftime("%Y/%m/%d %H:%M:%S")}";\n')
    a.write(f'var ans = {generate_ans(q_mode)}\n')
    log.write(f'問題コード: A{q_mode}{mon_code}\n 今回行われた{kamoku_info}の試験の結果は以下のようになった.\n {q}\n このとき，この試験の点数の{mode_data[q_mode-1]}を小数点第１位まで求めなさい．\n 更新:{koushin_zikoku.strftime("%Y/%m/%d %H:%M:%S")} 答え:{generate_ans(q_mode)}\n\n')

    
def write_close():
    global a
    global f
    f.close()
    a.close()
    log.close()
    os.system('chmod +x test.js')

def generate_question():
    global data_num
    global data_list
    data_num = random.randint(3,15)
    data_list = [random.randint(0,100) for _ in range(data_num)]
    return data_list


def generate_ans(mode):
    global data_num
    global data_list
    data_sort = data_list.copy()
    data_sort.sort()

    if(mode==1):
        if(data_num%2==0):

            return (data_sort[int(data_num/2)-1]+data_sort[int(data_num/2)])/2
        else:
            return data_sort[int(data_num/2)]
    elif(mode==2):
        sum = 0
        for dt in data_list:
            sum = dt + sum
        return round(sum/data_num,1)
    

def sc_message(mes):
    q5 = open('mente.js','w')
    q5.write(mes)
    q5.close()
    os.system('chmod +x mente.js')
    

#テスト用
#koshin_time = 5

#終了タイム
finish_hour = 4
finish_hun = 59

sc_message('')

while True:
    try:
        #ファイルの初期化
        q2 = open('log.txt','w')
        q2.close()
        for i in range(20):
            koushin_zikoku = datetime.datetime.now()
            write_open()
            mondai = random.randint(0,1)
            if(mondai==0):
                write()
            else:
                write2()
            write_close()
            for i in range(koshin_time):
                q4 = open('log2.txt','w')
                q4.write(f"最終稼働:{datetime.datetime.now()}\n")
                q4.close()
                q1 = open('log.txt','r')
                contents_data = q1.readline()
                q1.close()
                now_time = datetime.datetime.now()
                if(now_time.hour==finish_hour and now_time.minute==finish_hun):
                    sc_message('alert("現在，更新期間外です.問題は更新されません.");\n')
                    q3 = open('log.txt','w')
                    q3.write("システムを終了しました.\n")
                    q3.close()
                    exit()
                if(contents_data=="0"):
                    q3 = open('log.txt','w')
                    q3.write("システムを終了しました.\n")
                    q3.close()
                    exit()
                time.sleep(1)
    except Exception as e:
            print(f"エラー:{e}")
            q3 = open('error.txt','w')
            q3.write(f"system error {datetime.datetime.now()}\n")
            q3.close()
