;(function () {
	"use strict";

	function setTheme(t) {
		document.documentElement.setAttribute("data-theme", t);
		try {
			localStorage.setItem("nk-theme", t);
		} catch (e) {}
		var icon = document.querySelector("#themeBtn .theme-icon");
		if (icon) icon.textContent = t === "dark" ? "🌙" : "☀️";
	}

	function init() {
		var saved = "dark";
		try {
			saved = localStorage.getItem("nk-theme") || "dark";
		} catch (e) {}
		setTheme(saved);
		var y = document.getElementById("year");
		if (y) y.textContent = String(new Date().getFullYear());

		var themeBtn = document.getElementById("themeBtn");
		if (themeBtn) {
			themeBtn.addEventListener("click", function () {
				var cur = document.documentElement.getAttribute("data-theme");
				setTheme(cur === "dark" ? "light" : "dark");
			});
		}

		var menuBtn = document.getElementById("menuBtn");
		var sidebar = document.getElementById("sidebar");
		if (menuBtn && sidebar) {
			menuBtn.addEventListener("click", function () {
				var open = sidebar.classList.toggle("open");
				menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
			});
			sidebar.querySelectorAll("a").forEach(function (a) {
				a.addEventListener("click", function () {
					sidebar.classList.remove("open");
					menuBtn.setAttribute("aria-expanded", "false");
				});
			});
		}
	}

	if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
	else init();
})();
