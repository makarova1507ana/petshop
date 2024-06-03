// Получаем кнопку переключения темы
const themeToggle = document.querySelector('#theme-toggle');

// Добавляем обработчик события на клик по кнопке
themeToggle.addEventListener('click', () => {
    // Переключаем класс 'dark-mode' на body
    document.body.classList.toggle('dark-mode');

    // Проверяем, какая тема сейчас активна, и сохраняем выбранную тему в локальном хранилище
    const currentTheme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('theme', currentTheme);
});



