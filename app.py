# This Python file uses the following encoding: utf-8

import os, datetime

from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template
import random





app = Flask(__name__)   # create our flask app


emoticons = ["(ÒωÓױ)",
"((*′ ▽‘)爻(′▽‘*))",
"(ง •̀_•́)ง┻━┻",
"┬─┬ ノ( ' - 'ノ)",
"( /) V (\ ) ",
"(ฅ´ω`ฅ)",
"(๑>◡<๑)", 
"(´-ι_-｀)",
"(❁´▽`❁)",
"( *・ω・)✄╰ひ╯",
"( ◜◡‾)っ✂╰⋃╯",
"～♪( ´θ｀)ノ",
"(੭ु≧▽≦)੭ु",
"(´・ω・｀)",
"ヽ( ^∀^)ﾉ",
"┌(ㆆ㉨ㆆ)ʃ",
"Θ◇Θ",
"。(O^~^O)",
"( >﹏<。)～",
"╰(*°▽°*)╯",
"(˘❥˘)",
"(PД`q。)·。。。。。。",
"(●′ω`●)",
"ʅ(‾◡◝)ʃ ",
"(,,Ծ▽Ծ,,)",
"(｡▰‿‿▰｡) ❤",
"( ´◔ ‸◔')",
"┌(┐_Д_)┐",
"Z(∩3∩)Z",
"(ΦωΦ)",
"（=ˇωˇ=）"]





# this is our main page
@app.route("/")
def index():

	this_title = "How are you"
	return render_template("index.html", this_title = this_title)

@app.route("/greetings")
def greetings():
	lucky_number = random.randrange(0,len(emoticons)-1)
	your_emoticons = emoticons[lucky_number]
	return render_template("greetings.html", your_emoticons = your_emoticons.decode('utf-8'))



@app.errorhandler(404)
def page_not_found(error):

    return render_template('404.html', emoticons = emoticons), 404


# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	