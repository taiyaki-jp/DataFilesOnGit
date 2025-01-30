import streamlit as st
import os
#streamlit環境です
#gitに上げればそのGitが擬似的なランキングサーバーになる
#Unity側からもGit上のファイルを動的に読めるはず

st.title("スコアランキング")

datas=[] #str[]
path = 'DataFile/Scores.txt'

#書き込み
def FileWrite():
    with open(path,mode="w") as f :
        f.write("\n".join(map(str,datas)))

#読み込み
def FileRead():
    if os.path.isfile(path) == False:#ファイルが無ければ
        FileWrite()#先に書き込む
    f=open(path)
    readData=[s.rstrip() for s in f.readlines()]
    #st.write(readData)#中身確認用
    return readData

#画面に表示
def DataPrint():
    datas=FileRead()
    for i,n in enumerate(datas):
        st.write(f"{i+1}位：{n}点")

#strを一旦intになおしてソート
def DataSort():
    IntPerced=[]#Int[]
    for i,n in enumerate(datas):#intに変換
        IntPerced.append(int(n))
    
    SortedData=sorted(IntPerced,reverse=True)

    for i,n in enumerate(SortedData):#strに戻す
        datas[i]=str(n)


DataPrint()

userScore=st.number_input("あなたのスコア", value=0)#この画面からも操作できるように

if st.button("決定"):#この画面からも操作できるように
    datas= FileRead()
    datas.append(str(userScore))
    DataSort()
    FileWrite()
    DataPrint()
    st.rerun()
    
    

