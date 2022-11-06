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

LINK_BTNS[0].addEventListener('click', function() {window.location.href = 'http://127.0.0.1:5500/'});
LINK_BTNS[1].addEventListener('click', function() {window.location.href = 'http://127.0.0.1:5500/articles/'});
// LINK_BTNS[2].addEventListener('click', function() {window.location.href = 'http://127.0.0.1:5500/tags/'});