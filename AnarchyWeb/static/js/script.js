document.addEventListener("DOMContentLoaded", () => {
    animateCards();
});
async function animateCards() {
    const cards = document.querySelectorAll('div.card');

    for (let i = 0; i < cards.length; i++) {
        setTimeout(() => {
            cards[i].classList.add('show');
        }, i * 50);
    }
}

function getItemsById(prefix) {
    return Array.from(document.querySelectorAll(`div.card[id^="${prefix}"]`)).map(
        (element) => [element.id, element]
    );
}