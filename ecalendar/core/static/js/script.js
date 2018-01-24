//event modal
var me = document.getElementById("id-modal-event");

me.addEventListener("click", function(e) {
	if (e.target === this) {
		closeEventModal();
	}
});

function closeEventModal() {
	me.style.display = "none";
}

function openEventModal() {
	me.style.display = "flex";
}