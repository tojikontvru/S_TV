# S TV — Бесплатное ТВ и Радио

**Разработчик:** Safarali Group  
**Версия:** 1.0.0  
**Сайт:** [https://tojikontvru.github.io/S_TV/](https://tojikontvru.github.io/S_TV/)

## Безопасность

Все URL потоков защищены:
- Хранятся **ТОЛЬКО** в памяти JavaScript (массив `_channels`)
- **НЕ** отображаются в интерфейсе
- **НЕ** сохраняются в localStorage
- **НЕ** записываются в data-атрибуты
- **НЕ** копируются в буфер обмена
- Инспектор кода **НЕ** показывает ссылки

## Возможности

- 📺 850+ ТВ-каналов с автосканером
- 📻 Радиостанции с CSS-визуализатором
- 🎨 Тёмная тема (AMOLED / Тёмная / Серая)
- 📱 Полностью адаптивный
- 🔍 Мгновенный поиск
- ⭐ Избранное (без сохранения URL)
- 🎲 Случайный канал
- 🎬 HLS.js видеоплеер
- 📻 Аудиоплеер для радио

## Технологии

- HTML5 + CSS3 + Vanilla JavaScript
- HLS.js (CDN) — M3U8 потоки
- Font Awesome 6 (CDN)
- Google Fonts Inter

## Установка

```bash
git clone https://github.com/tojikontvru/S_TV.git
```

Откройте `index.html` в браузере.

## API

Сканирование 850 потоков через 3 зеркала:
- `api.mediabay.tv`
- `api.v1.mediabay.tv`
- `api.v1.mediabay.uz`

Кеш — 24 часа.

## Обратная связь

- Telegram: [@Mushtariy_LLC](https://t.me/Mushtariy_LLC)
- Email: support@safaraligroup.com

## Лицензия

MIT License
