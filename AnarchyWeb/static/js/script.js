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
        let parsedDomain = domainMatch ? domainMatch[2] : 'n/a';

        if (!element.href.includes('#disabled')) {
            element.textContent = `(source, ${parsedDomain})`;
        }
    });
});

function showReposLinks(show) {
    let repos = document.querySelector('div.repos');
    let repos_links = document.querySelectorAll('div.repos-links a');
    let is_animation = repos.getAttribute('in_animation') === 'true';

    if (show && !is_animation) {
        repos.style.height = '70px';
        repos.setAttribute('in_animation', true);

        setTimeout(() => {
            repos_links.forEach((e, index) => {
                setTimeout(() => {
                    e.style.opacity = 1;
                }, index * 100);
            });
            setTimeout(() => {
                repos.setAttribute('in_animation', false);
            }, 300 + repos_links.length * 100);
        }, 300);
    } else if (!show && !is_animation) {
        repos.setAttribute('in_animation', true);

        repos_links.forEach((e, index) => {
            setTimeout(() => {
                e.style.opacity = 0;
            }, index * 100);
        });

        setTimeout(() => {
            repos.style.height = '20px';
            repos.setAttribute('in_animation', false);
        }, 300 + repos_links.length * 100);
    }
}

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
