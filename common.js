// ヘッダーのスタイル調整
const TITLE = document.querySelector('h1.title');
const NAV = document.querySelector('div.nav');
const MAIN = document.querySelector('div.main');

function resizeWindow(){
    NAV.style.marginRight = String((document.body.clientWidth - MAIN.offsetWidth) / 2 - 60) + 'px';
	TITLE.style.marginLeft = String((document.body.clientWidth - MAIN.offsetWidth) / 2 + 32 - 8) + 'px';
}

window.onresize = resizeWindow;

resizeWindow();

// ヘッダーのボタン関連
const LINK_BTNS = document.querySelectorAll('div.header button');

LINK_BTNS[0].addEventListener('click', function() {window.location.href = 'https://ksk3110.github.io/'});
LINK_BTNS[1].addEventListener('click', function() {window.location.href = 'https://ksk3110.github.io//articles/'});

// アイコン
document.head.innerHTML += '<link rel="icon" type="image/png" href="/favicon.png"';