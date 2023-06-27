function loadCloseMessage() {
	if (document.getElementById('user-messages')) {
		const closeBtn = document.getElementById('btn-close-message');
		closeBtn.addEventListener('click', e => {
			const nav = e.target.closest('nav.user-messages');
			nav.classList.add('d-none');
		});
	}
}


export default loadCloseMessage;
