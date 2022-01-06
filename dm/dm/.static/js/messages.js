function closeMessage(e){
	/* Close message container */

	const nav = e.target.closest('nav.user-messages');
	nav.classList.add('d-none');
}


function loadCloseMessage() {
   const btn = document.getElementById('btn-close-message');

   btn.addEventListener('click', closeMessage);
}

export default loadCloseMessage;
