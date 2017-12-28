const API_HOST = '/api'

const hash = window.location.hash.substr(1);
if (hash) {
	document.querySelector('#view-note').style.display = 'flex';

	fetch(`${API_HOST}/notes/${hash}`, {
		method: 'GET'
	}).then((resp) => {
		return resp.json();
	}).then((data) => {
		for (let k in data) {
			document.querySelector(`#note-${k}`).innerHTML += data[k];
		}
	});


} else {
	document.querySelector('#view-default').style.display = 'flex';
}

document.querySelector('#post-post').addEventListener('click', (e) => {
	fetch(`${API_HOST}/notes`, {
		method: 'POST',
		body: {}
	});
});
