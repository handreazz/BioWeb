#!C:/BioWeb/python.exe
#coding:utf-8
import time
print("Content-type:text/html;charset=utf-8\r\n\r\n")

print("""
<!DOCTYPE html>

<html>
<head>
        <meta charset="utf-8" />
        <title>Demo3</title>
        <script type="text/javascript" src="jquery-1.10.1.min.js"></script>
</head>
<body style="font-family: 'Microsoft YaHei', STXingkai, SimSun">
        <style type="text/css">
                .Title {
                        margin: 30px;
                        color: darkblue;
                        font-size: 60px;
                        font-weight: bold;
                }
                .SubTitle {
                        margin: 20px;
                        color: cadetblue;
                        font-size: xx-large;
                        font-weight: bold;
                        display: none;
                }
                .Tip {
                        magin: 20px;
                        font-size: larger;
                        display: none;
                }
                .ContentGrid {
                        padding: 10px;
                        text-align: center;
                        width: 600px;
                }
        </style>
        <div style="margin: 150px 5% auto 5%; text-align: center;">
                <img alt="Portrait" src="headpic.jpg" width="240" height="240" />
                <p class="Title" id="title">唔...说点啥呢</p>
                <p class="SubTitle" id="sub-title">如你所见，在你的py中可以直接print网页源代码呢</p>
                <p class="Tip" id="tip">
                        输出个漂亮的动态网页多好~<br>""")
print(time.strftime("Time now: %Y-%m-%d %H:%M:%S",time.localtime(time.time())))
print("""
                </p>
        </div>
        <script type="text/javascript">
                $("#title").fadeIn(1000);
                $("#sub-title").delay(1000);
                $("#sub-title").fadeIn(1000);
                $("#tip").delay(2000);
                $("#tip").fadeIn(1000);
        </script>

</body>
</html>
""")