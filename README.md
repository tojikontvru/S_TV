# S TV — Защищённый медиаплеер ТВ и Радио

> **Современный одностраничный веб-плеер** с публичными источниками данных, футуристичным AMOLED-дизайном и **максимальной защитой URL потоков**.

![S TV](og-image.png)

---

## 🔒 Защита URL потоков

Главная особенность проекта — **URL потоков НИГДЕ не сохраняются в открытом виде** на стороне клиента:

| Где | Что хранится | URL потока? |
|---|---|---|
| **DOM-разметка** | `data-idx` (только индекс) | ❌ Нет |
| **Атрибуты элементов** | `data-idx`, `data-type` | ❌ Нет |
| **`localStorage`** (`stv_fav`) | `{idx, type}` без URL | ❌ Нет |
| **`localStorage`** (`stv_meta`) | `{name, quality, category}` | ❌ Нет |
| **`sessionStorage`** | — | ❌ Не используется |
| **Cookies** | — | ❌ Не используются |
| **JS-память** | `channelsData[]`, `radioData[]` | ✅ Только в RAM |
| **Кнопки "Копировать URL"** | Отсутствуют | ❌ Нет таких кнопок |

**Извлечение URL** происходит только в момент клика по карточке:
```js
function openPlayer(idx) {
  const url = channelsData[idx].url;   // ← RAM only
  video.src = url;                      // ← идёт напрямую в плеер
}
```

Ни DevTools, ни "Просмотр кода", ни `view-source:` не покажут URL потоков — всё зашито в JS-функции, а DOM содержит только индексы.

---

## ✨ Возможности

### 📺 ТВ-каналы
- **850+ каналов** из публичного источника `iptv-org.github.io`
- 8 категорий: Фильмы, Спорт, Новости, Детские, Музыка, HD, Региональные, Другое
- Автоматический парсинг M3U плейлиста
- HLS.js плеер с авто-fallback на нативное видео
- Полноэкранный режим и Picture-in-Picture
- Регулятор громкости с плавной анимацией

### 📻 Радио
- **20+ радиостанций** с разными жанрами (Pop, Rock, Jazz, Talk, Dance)
- Местные FM-станции Европы (NRJ, Virgin, Europe 1, RTL, Chérie FM и др.)
- HTML5 Audio с визуализатором
- Фоновое воспроизведение и блокировка экрана
- Стриминг метаданных (исполнитель, трек)

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
- Web Share API для "Поделиться"
- Touch-жесты и длительное нажатие

---

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

---

## 🛠️ Стек

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
| Источники | IPTV-org (TV), публичный M3U (Radio) |

**Никаких фреймворков, никаких сборщиков** — открывается сразу как `index.html`.

---

## 📦 Источники данных

### ТВ
- **`https://iptv-org.github.io/iptv/index.m3u`** — публичный плейлист с 850+ каналами
- Парсинг на клиенте с автоматическим определением категорий

### Радио
- **`public_radio.m3u`** — 20+ радиостанций с различными жанрами
- Включает популярные FM-станции Европы: NRJ, Virgin, Europe 1, RTL, Chérie FM, Fun Radio, RFM и др.

---

## 📁 Структура проекта

```
S_TV/
├── index.html              # Главное приложение (1111 строк)
├── public_radio.m3u         # 20+ радиостанций (M3U плейлист)
├── manifest.json           # PWA manifest
├── sw.js                   # Service Worker для оффлайн-кеша
├── icon.svg                # SVG-иконка
├── icon-192.png            # PWA 192x192
├── icon-512.png            # PWA 512x512
├── apple-touch-icon.png    # iOS 180x180
├── favicon.ico             # Multi-resolution favicon
├── favicon-32.png          # Favicon 32x32
├── og-image.png            # Open Graph 1200x630
├── README.md               # Этот файл
├── LICENSE                 # MIT
└── .github/
    └── workflows/
        └── deploy.yml      # GitHub Pages автодеплой
```

---

## 🔐 Лицензия

MIT © Safarali Group — см. [LICENSE](LICENSE)

---

## 💬 Контакты

Telegram: [@Mushtariy_LLC](https://t.me/Mushtariy_LLC)
