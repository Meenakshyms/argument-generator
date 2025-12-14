// Theme toggle
function toggleTheme() {
    const body = document.body;
    if (body.classList.contains("light")) {
        body.classList.remove("light");
        body.classList.add("dark");
        localStorage.setItem("theme", "dark");
    } else {
        body.classList.remove("dark");
        body.classList.add("light");
        localStorage.setItem("theme", "light");
    }
}

// Restore theme on load
document.addEventListener("DOMContentLoaded", () => {
    const saved = localStorage.getItem("theme") || "light";
    document.body.classList.add(saved);
});

// Search suggestions
const topicInput = document.getElementById("topic");
const suggestionsBox = document.getElementById("suggestions");

if (topicInput) {
    topicInput.addEventListener("input", async () => {
        const query = topicInput.value;
        if (query.length < 1) {
            suggestionsBox.innerHTML = "";
            return;
        }
        const res = await fetch(`/suggest?q=${query}`);
        const data = await res.json();
        suggestionsBox.innerHTML = "";
        data.forEach(item => {
            const div = document.createElement("div");
            div.classList.add("suggestion-item");
            div.textContent = item;
            div.onclick = () => {
                topicInput.value = item;
                suggestionsBox.innerHTML = "";
            };
            suggestionsBox.appendChild(div);
        });
    });
}
