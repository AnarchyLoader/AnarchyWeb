document.addEventListener('DOMContentLoaded', () => {
    animateCards();

    checkServers().then((server) => {
        console.log(`Server: ${server}`);
        document.querySelectorAll('.download').forEach((element) => {
            element.href = server + element.getAttribute('file');
        });
    });

    document.querySelectorAll('.source').forEach((element) => {
        let domain = element.href.trim();
        let domainMatch = domain.match(/https?:\/\/(www\.)?([^\/]+)/);
        let parsedDomain = domainMatch ? domainMatch[2] : 'N/A';

        if (!element.href.includes('#disabled')) {
            element.textContent = `(source, ${parsedDomain})`;
        }
    });
});

async function animateCards() {
    const cards = document.querySelectorAll('div.card');

    for (let i = 0; i < cards.length; i++) {
        setTimeout(() => {
            cards[i].classList.add('show');
        }, i * 50);
    }
}

async function checkServers() {
    let servers = [
        'https://cdn.anarchy.my/',
        'https://axkanxneklh7.objectstorage.eu-amsterdam-1.oci.customer-oci.com/n/axkanxneklh7/b/anarchy/o/',
    ];

    for (let i = 0; i < servers.length; i++) {
        let response = await fetch(servers[i]);
        if (response.ok) {
            return servers[i];
        }
    }
}
