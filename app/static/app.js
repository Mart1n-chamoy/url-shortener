async function shortenUrl() {

    const url = document.getElementById("url").value;
    const custom_code =
        document.getElementById("custom_code").value;

    const response = await fetch("/shorten", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url,
            custom_code
        })
    });

    const data = await response.json();

    if (!response.ok) {

        document.getElementById("result").innerHTML = `
            <div class="result-box">
                ❌ ${data.detail}
            </div>
        `;

        return;
    }

    const shortUrl =
        `${window.location.origin}/${data.short_code}`;

    document.getElementById("result").innerHTML = `
        <div class="result-box">

            <strong>URL corta:</strong>

            <br><br>

            <a href="${shortUrl}" target="_blank">
                ${shortUrl}
            </a>

            <br><br>

            <button onclick="copyUrl('${shortUrl}')">
                Copiar URL
            </button>

        </div>
    `;
}

async function getStats() {

    const code =
        document.getElementById("stats_code").value;

    const response =
        await fetch(`/stats/${code}`);

    const data = await response.json();

    if (!response.ok) {

        document.getElementById("stats").innerHTML = `
            <div class="result-box">
                ❌ Código no encontrado
            </div>
        `;

        return;
    }

    document.getElementById("stats").innerHTML = `
        <div class="result-box">

            <p>
                <strong>URL:</strong><br>
                ${data.original_url}
            </p>

            <p>
                <strong>Código:</strong>
                ${data.short_code}
            </p>

            <p>
                <strong>Clicks:</strong>
                ${data.clicks}
            </p>

        </div>
    `;
}

function copyUrl(url) {

    navigator.clipboard.writeText(url);

    alert("URL copiada");
}