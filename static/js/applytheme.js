// Функция для применения сохраненной темы
function applyTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
    } else {
        document.body.classList.remove('dark-mode');
    }
}
    // Применяем сохраненную тему при загрузке страницы

    applyTheme();