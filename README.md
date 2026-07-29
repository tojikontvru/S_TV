# S TV — Защищённый медиаплеер ТВ и Радио

**Современный одностраничный веб-плеер** с агрегацией 3 API-зеркал, футуристичным AMOLED-дизайном и **максимальной защитой URL потоков**.

## 🔒 Защита URL потоков

Главная особенность проекта — **URL потоков НИГДЕ не сохраняются в открытом виде** на стороне клиента:

| Где | Что хранится | URL потока? |
|---|---|---|
| **DOM-разметка** | `data-idx` (только индекс) | ❌ Нет |
| **Атрибуты элементов** | `data-idx`, `data-type` | ❌ Нет |
| **localStorage** (`stv_fav`) | `{idx, type}` без URL | ❌ Нет |
| **localStorage** (`stv_meta`) | `{name, quality, category}` | ❌ Нет |
| **JS-память** | `channelsData[]`, `radioData[]` | ✅ Только в RAM |
| **Кнопки "Копировать URL"** | Отсутствуют | ❌ Нет таких кнопок |

Извлечение URL происходит только в момент клика по карточке:

```js
function openPlayer(idx) {
  const url = channelsData[idx].url;   // ← RAM only
  video.src = url;                      // ← идёт напрямую в плеер
}
```

Ни DevTools, ни "Просмотр кода", ни `view-source:` не покажут URL потоков — всё зашито в JS-функции, а DOM содержит только индексы.

## ✨ Возможности

### 📺 ТВ-каналы
- 850+ каналов в 8 категориях: Фильмы, Спорт, Новости, Детские, Музыка, HD, Региональные, Другое
- Параллельное сканирование 3 API-зеркал — берётся самый быстрый ответ
- HTTP 200 валидация перед добавлением каналов
- Пакетная загрузка по 30 каналов (Promise.allSettled)
- HLS.js плеер с авто-fallback на нативное видео
- Полноэкранный режим и Picture-in-Picture
- Регулятор громкости с плавной анимацией

### 📻 Радио
- 5 категорий: Pop, Rock, Jazz, Talk, Dance
- HTML5 Audio с визуализатором
- Фоновое воспроизведение и блокировка экрана

### ⭐ Избранное
- Быстрое сохранение: `localStorage` хранит только `{idx, type}`
- Восстановление списка при загрузке
- Синхронизация фокуса на всех вкладках

### ⚙️ Настройки
- 3 темы: **AMOLED** (полностью чёрный), **Dark** (тёмно-синий), **Gray** (нейтральный)
- 3 размера карточек: **Compact / Normal / Large**
- Telegram-ссылка на @Mushtariy_LLC

### 🎨 UI/UX
- Splash-экран с 200 звёздами на Canvas + parallax
- Glass morphism (rgba card + 20px blur)
- Плавные переходы между вкладками
- Touch-жесты и длительное нажатие

## 🚀 Деплой на GitHub Pages

1. **Создайте репозиторий** `S_TV` на GitHub
2. **Загрузите файлы**:
   ```bash
   git init
   git add .
   git commit -m "Initial S TV release"
   git branch -M main
   git remote add origin https://github.com/<username>/S_TV.git
   git push -u origin main
   ```
3. **Settings → Pages → Source: GitHub Actions**
4. После первого push автоматически сработает workflow `.github/workflows/deploy.yml`
5. Сайт будет доступен: `https://<username>.github.io/S_TV/`

> ⚠️ **ВАЖНО**: Если в истории чата был опубликован GitHub-токен — **немедленно отзовите его** на [github.com/settings/tokens](https://github.com/settings/tokens), затем переустановите через `git credential-manager` или SSH-ключ.

## 🛠 Стек

| Слой | Технология |
|---|---|
| Frontend | Vanilla HTML5 / CSS3 / ES6+ |
| Видео | HLS.js + нативный `<video>` |
| Аудио | HTML5 `<audio>` |
| Иконки | Font Awesome 6 |
| Шрифт | Inter (Google Fonts) |
| Кэш | Service Worker |
| PWA | Web App Manifest |
| CI/CD | GitHub Actions |

**Никаких фреймворков, никаких сборщиков** — открывается сразу как `index.html`.

## 📦 API-зеркала

Приложение использует 3 зеркала для автоматической балансировки:

```
api.v1.mediabay.tv (первичное, всегда первое)
api.mediabay.tv (резервное)
api.v1.mediabay.uz (резервное)
```

При запросе к каналу сначала пробуются все 3 зеркала. При успешном ответе HTTP 200 URL извлекается из JS-памяти, ни в коем случае не сохраняется в localStorage или DOM.

## 📁 Структура проекта

```
S_TV/
├── index.html              # Главное приложение (146 строк)
├── manifest.json           # PWA manifest
├── sw.js                   # Service Worker для оффлайн-кеша
├── icon.svg                # SVG-иконка
├── public_radio.m3u        # Плейлист радиостанций
├── README.md               # Этот файл
└── LICENSE                 # MIT License

.github/
└── workflows/
    └── deploy.yml         # GitHub Pages автодеплой
```

## 🔐 Лицензия

MIT © Safarali Group — см. [LICENSE](LICENSE)

## 💬 Контакты

Telegram: [@Mushtariy_LLC](https://t.me/Mushtariy_LLC)
