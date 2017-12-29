const API_HOST = '/api'

const deleteNull = (d) => {
	for (let k in d) {
		if (d[k] === null) {
			delete d[k];
		}
	}
};

const loadNote = () => {
	fetch(`${API_HOST}/notes/${hash}`, {
		method: 'GET'
	}).then((resp) => {
		return resp.json();
	}).then((data) => {
		for (let k in data) {
			document.querySelector(`#note-${k}`).innerHTML += data[k];
		}
	});
};

const hash = window.location.hash.substr(1);
if (hash) {
	document.querySelector('#view-note').style.display = 'flex';
	loadNote();
} else {
	document.querySelector('#view-default').style.display = 'flex';
}

document.querySelector('#post-post').addEventListener('click', (e) => {
	const body = {
		title: e => e.value,
		message: e => e.value,
		expire: e => Math.round((new Date(e.value || 0)).getTime() / 1000) || null,
		private: e => e.checked,
		readonly: e => e.checked
	};

	for (let k in body) {
		body[k] = body[k](document.querySelector(`#post-${k}`));
	}
	deleteNull(body);

	fetch(`${API_HOST}/notes`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(body)
	}).then((resp) => {
		return resp.json();
	}).then((data) => {
		window.location.replace(`/#${data.hash}`);
		window.location.reload();
	});
});
