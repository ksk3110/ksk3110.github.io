import re
import os
import shutil

frame = '''<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=Inter&family=Noto+Sans+JP&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="https://ksk3110.github.io/style.css">
	<script src="https://ksk3110.github.io/common.js" defer></script>
	<title>[TITLE]</title>
</head>
<body>
	<div class="header">
		<h1 class="title">Ksk3110</h1>
		<div class="nav">
			<button><img src="https://ksk3110.github.io/icons/home.svg"  title="トップページ"></button>
			<button><img src="https://ksk3110.github.io/icons/articles.svg"  title="記事一覧"></button>
		</div>
	</div>
	<div class="content">
		<div class="main">
			<h1 id="title">[TITLE]</h1>
			<h3>[DATE]</h3>
			[CONTENT]
		</div>
	</div>
</body>
</html>'''

if os.path.exists('./article'): shutil.rmtree('./article')
os.mkdir('./article')

def generate(data: str, id: int):
	data = data.split('\n')
	meta = data[0:2]
	del data[0:2]

	compiled = []
	for line in data: # Pharser
		if re.fullmatch('# .+', line):    compiled.append(f"<h1>{re.sub('^# ', '', line)}</h1>")
		elif re.fullmatch('## .+', line): compiled.append(f"<h2>{re.sub('^## ', '', line)}</h2>")
		else:
			if re.findall(r'\[https?://.+?\|.+?\]', line): # <a></a>
				for links in re.findall(r'\[https?://.+?\|.+?\]', line):
					links = re.search(r'\[https?://.+?\|.+?\]', line).group()
					line = re.sub(r'\[https?://.+?\|.+?\]', '=LINK=', line, 1)

					links = re.sub(r'^\[', '<a href="', links,1)
					links = re.sub(r'\|', '">', links, 1)
					links = re.sub(r'\]$', '</a>', links,1)

					line = line.replace('=LINK=', links)

			if re.findall(r'\*\*.+?\*\*', line): # <strong><strong>
				for links in re.findall(r'\*\*.+?\*\*', line):
					links = re.search(r'\*\*.+?\*\*', line).group()
					line = re.sub(r'\*\*.+?\*\*', '=STRONG=', line, 1)

					links = re.sub(r'^\*\*', '<strong>', links,1)
					links = re.sub(r'\*\*$', '</strong>', links,1)

					line = line.replace('=STRONG=', links)

			compiled.append(f"<p>{line}</p>")

	html = frame
	html = html.replace('[CONTENT]', '\n'.join(compiled))
	html = html.replace('[TITLE]', meta[0])
	html = html.replace('[DATE]', meta[1])
	
	with open(f"./article/{id}.html", encoding='UTF-8', mode='w') as new:
		new.write(html)

amount = 0
while os.path.isfile(f"./data/{amount}.md"):
	print(amount)
	amount += 1

for i in range(amount):
	with open(f"./data/{i}.md", encoding='UTF-8', mode='r') as f:
		generate(f.read(), i)

articlesHtml = '''<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Inter&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=Inter&family=Noto+Sans+JP&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="https://ksk3110.github.io/style.css">
	<script src="https://ksk3110.github.io/common.js" defer></script>
	<title>記事一覧</title>
</head>
<body>
	<div class="header">
		<h1 class="title">Ksk3110</h1>
		<div class="nav">
			<button><img src="https://ksk3110.github.io/icons/home.svg"  title="トップページ"></button>
			<button><img src="https://ksk3110.github.io/icons/articles_now.svg"  title="記事一覧"></button>
		</div>
	</div>
	<div class="content">
		<div class="main">
			<h1>記事一覧</h1>
			[LIST]
		</div>
	</div>
</body>
</html>'''

with open(f"./articles/index.html", encoding='UTF-8', mode='w') as f:
	articleList = []
	for i in range(amount):
		d = open(f"./data/{i}.md", encoding='UTF-8', mode='r')
		dl = d.read().split('\n')
		title = dl[0]
		date = dl[1]
		articleList.insert(0, f'<div class="box"><a href="https://ksk3110.github.io/article/{i}.html">{title}</a><p>{date}</p></div>')
		d.close()

	f.write(articlesHtml.replace('[LIST]' , '\n'.join(articleList)))