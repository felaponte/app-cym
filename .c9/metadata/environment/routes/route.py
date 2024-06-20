{"filter":false,"title":"route.py","tooltip":"/routes/route.py","undoManager":{"mark":54,"position":54,"stack":[[{"start":{"row":0,"column":0},"end":{"row":25,"column":16},"action":"insert","lines":["@app.route(\"/\")","def home_page():","    connectionSQL()","    return render_template(\"home.html\")","","@app.route(\"/register_page\")","def register_page():","    return render_template(\"register.html\")","    ","@app.route(\"/consult_page\")","def consult_page():","    return render_template(\"consult.html\")","    ","@app.route(\"/register_user\", methods=[\"post\"])    ","def register_user():","    id = request.form[\"id\"]","    name = request.form[\"name\"]","    lastname = request.form[\"lastname\"]","    birthday = request.form[\"birthday\"]","    print(id, name, lastname, birthday)","    return \"ok\"","    ","#@app.route(\"/consult_user\", methods=[\"post\"])    ","#def consult_user():"," #   print(id, name, lastname, birthday)","  #  return \"ok\""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":3}],[{"start":{"row":2,"column":4},"end":{"row":3,"column":39},"action":"remove","lines":["connectionSQL()","    return render_template(\"home.html\")"],"id":4},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["r"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["e"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["t"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["u"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["r"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":[" "],"id":5},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["f"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["u"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["n"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["c"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":["_"],"id":6},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["h"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["o"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["m"]},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["_"],"id":7},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["p"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["a"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["g"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":25},"end":{"row":2,"column":27},"action":"insert","lines":["()"],"id":8}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":10},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["o"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"remove","lines":["r"],"id":11},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["o"]}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"],"id":12},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["o"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":[" "],"id":13},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["c"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["o"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["n"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["t"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["r"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["o"]},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["l"]}],[{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["l"],"id":14},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["e"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["r"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["."]}],[{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["c"],"id":15},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["o"]},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["n"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["t"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["r"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["o"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["l"]}],[{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":[" "],"id":16},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["i"]},{"start":{"row":0,"column":25},"end":{"row":0,"column":26},"action":"insert","lines":["m"]},{"start":{"row":0,"column":26},"end":{"row":0,"column":27},"action":"insert","lines":["p"]},{"start":{"row":0,"column":27},"end":{"row":0,"column":28},"action":"insert","lines":["o"]},{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":["r"]},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":[" "],"id":17},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"insert","lines":["*"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":43},"action":"remove","lines":["ender_template(\"register.html\")"],"id":18},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["r"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["f"],"id":19},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["u"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["n"]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["c"]}],[{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["_"],"id":20},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["r"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["g"],"id":21},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["i"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["s"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["t"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["e"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":24},"action":"remove","lines":["func_register"],"id":22},{"start":{"row":8,"column":11},"end":{"row":8,"column":31},"action":"insert","lines":["func_register_page()"]}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":42},"action":"remove","lines":["render_template(\"consult.html\")"],"id":23},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["r"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["e"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["t"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["u"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["n"]},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"remove","lines":["r"],"id":24},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"remove","lines":["n"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"remove","lines":["u"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"remove","lines":["t"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"remove","lines":["e"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"remove","lines":["r"]}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["f"],"id":25},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["u"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["n"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["c"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["_"]}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":16},"action":"remove","lines":["func_"],"id":26},{"start":{"row":12,"column":11},"end":{"row":12,"column":30},"action":"insert","lines":["func_consult_page()"]}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":15},"action":"remove","lines":["\"ok\""],"id":27},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["f"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["u"]},{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["n"]},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["c"]}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":15},"action":"remove","lines":["func"],"id":28},{"start":{"row":21,"column":11},"end":{"row":21,"column":31},"action":"insert","lines":["func_register_user()"]}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":29}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"],"id":30},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":[" "],"id":31},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["s"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["e"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["r"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["v"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["e"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":[" "],"id":32},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["i"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["m"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["p"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["o"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["r"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":[" "],"id":33}],[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["*"],"id":34}],[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"remove","lines":["*"],"id":35}],[{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["a"],"id":36},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["p"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["p"]}],[{"start":{"row":17,"column":0},"end":{"row":21,"column":39},"action":"remove","lines":["    id = request.form[\"id\"]","    name = request.form[\"name\"]","    lastname = request.form[\"lastname\"]","    birthday = request.form[\"birthday\"]","    print(id, name, lastname, birthday)"],"id":37}],[{"start":{"row":16,"column":20},"end":{"row":17,"column":0},"action":"remove","lines":["",""],"id":38}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":1},"action":"remove","lines":["#"],"id":39}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"remove","lines":["#"],"id":40}],[{"start":{"row":21,"column":1},"end":{"row":22,"column":16},"action":"remove","lines":["#   print(id, name, lastname, birthday)","  #  return \"ok\""],"id":41}],[{"start":{"row":21,"column":1},"end":{"row":21,"column":2},"action":"insert","lines":["r"],"id":42},{"start":{"row":21,"column":2},"end":{"row":21,"column":3},"action":"insert","lines":["e"]},{"start":{"row":21,"column":3},"end":{"row":21,"column":4},"action":"insert","lines":["t"]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["u"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["r"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["n"]}],[{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":[" "],"id":43},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["f"]},{"start":{"row":21,"column":9},"end":{"row":21,"column":10},"action":"insert","lines":["u"]},{"start":{"row":21,"column":10},"end":{"row":21,"column":11},"action":"insert","lines":["n"]},{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["c"]},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["_"]}],[{"start":{"row":21,"column":13},"end":{"row":21,"column":14},"action":"insert","lines":["c"],"id":44},{"start":{"row":21,"column":14},"end":{"row":21,"column":15},"action":"insert","lines":["o"]},{"start":{"row":21,"column":15},"end":{"row":21,"column":16},"action":"insert","lines":["n"]},{"start":{"row":21,"column":16},"end":{"row":21,"column":17},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":18},"action":"insert","lines":["u"],"id":45},{"start":{"row":21,"column":18},"end":{"row":21,"column":19},"action":"insert","lines":["l"]},{"start":{"row":21,"column":19},"end":{"row":21,"column":20},"action":"insert","lines":["t"]},{"start":{"row":21,"column":20},"end":{"row":21,"column":21},"action":"insert","lines":["_"]},{"start":{"row":21,"column":21},"end":{"row":21,"column":22},"action":"insert","lines":["u"]},{"start":{"row":21,"column":22},"end":{"row":21,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":21,"column":23},"end":{"row":21,"column":24},"action":"insert","lines":["e"],"id":46},{"start":{"row":21,"column":24},"end":{"row":21,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":21,"column":25},"end":{"row":21,"column":27},"action":"insert","lines":["()"],"id":47}],[{"start":{"row":20,"column":19},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["p"]},{"start":{"row":21,"column":5},"end":{"row":21,"column":6},"action":"insert","lines":["r"]},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["i"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["n"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":21,"column":9},"end":{"row":21,"column":11},"action":"insert","lines":["()"],"id":52}],[{"start":{"row":21,"column":10},"end":{"row":21,"column":12},"action":"insert","lines":["\"\""],"id":53}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["o"],"id":54},{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"insert","lines":["k"]}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "],"id":55}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"remove","lines":[" "],"id":56}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "],"id":57}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "],"id":58}]]},"ace":{"folds":[],"scrolltop":49.599998474121094,"scrollleft":0,"selection":{"start":{"row":18,"column":4},"end":{"row":18,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1718841901486,"hash":"66d6753bfea6778c1788fee2424462a67276418a"}