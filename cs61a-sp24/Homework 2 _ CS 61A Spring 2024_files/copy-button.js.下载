function copyCode(template, id) {
    const unescape = (string) => {
        const span = document.createElement("span");
        span.innerHTML = string;
        return span.innerText;
    };

    navigator.clipboard.writeText(unescape(template));
    document.getElementById(id).querySelector(".copy-tooltip span").innerText = "Copied!";
}

for (const button of document.querySelectorAll(".inline-copy-button")) {
    button.addEventListener("mouseleave", () => {
        button.querySelector(".copy-tooltip span").innerText = "Copy";
    })
}
