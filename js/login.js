const prevent = document.querySelectorAll("[required]");

function validate(event) {
    event.preventDefault();
}
for (preventerror of prevent) {
    preventerror.addEventListener("invalid", validate);
}