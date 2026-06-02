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

    document.getElementById("result").innerHTML = `
        <p>
            URL corta:
            <a href="/${data.short_code}">
                ${window.location.origin}/${data.short_code}
            </a>
        </p>
    `;
}