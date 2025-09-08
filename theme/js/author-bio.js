window.onload = function () {
    fetch('/author/sarah-rouge.html').then(response => response.text()).then(html => {
        document.getElementById('include-pages').innerHTML = html;
    });
};