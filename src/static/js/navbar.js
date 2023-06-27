function hideNavBar() {
    const togglerBtn = document.getElementById("btnNavbarToggler");
	const navDiv = document.getElementById("navbarResponsive");
    togglerBtn.classList.add("collapsed");
    togglerBtn.setAttribute("aria-expanded", "false");
    navDiv.classList.remove("show");
}


function checkIfHideNav() {
    const widthScreen = window.screen.width;
    const minWidthScreen = 991;
    if (widthScreen < minWidthScreen) {
        hideNavBar();
    }
}


export default function loadNavBar() {
    const navDiv = document.getElementById('navbarResponsive');
    const links = navDiv.querySelectorAll('li.nav-item > a.nav-link');
    links.forEach(link => link.addEventListener('click', checkIfHideNav));
}



