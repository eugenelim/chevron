# Chevron

**A keyboard-first start page in one HTML file.** No server, build, account or database. Open it in a browser and it works.

[**Quick start**](#quick-start) · [Configure](#configure) · [Built-in bookmarks](#built-in-bookmarks) · [Keyboard shortcuts](#keyboard-shortcuts) · [Privacy](#privacy)

![A tour of Chevron: shortcuts, search, pages, stock charts, weather, the bookmark editor, tags, themes and light mode](docs/demo.gif)

## Why Chevron

- **Open any link in two keystrokes.** Type `gm` for Gmail or `hn` for Hacker News, anywhere on the page.
- **One file you own.** Keep it on disk, host it anywhere, or hand a pre-filled copy to your team.
- **Everything in one box.** `Ctrl/⌘ K` searches bookmarks, runs commands and searches the web (`yt lofi`, `gh react`, `$ AAPL`).
- **Built to stay tidy.** An inbox for links you paste, tags, health checks, duplicate detection and a trash with undo.
- **Glanceable.** Clocks with local weather, stock charts, notes and a calendar.
- **Looks how you want.** 13 themes in light and dark, card styles, fonts and backdrops.
- **Private.** Your data stays in your browser's `localStorage`.

## Quick start

```sh
curl -O https://raw.githubusercontent.com/eugenelim/chevron/main/index.html
open index.html   # or double-click it
```

Then make it your browser's home page or new-tab page. Works in current Chrome, Edge, Firefox and Safari. To share it, serve the file from any static host (GitHub Pages, Netlify, an intranet server).

**First things to try:** type a shortcut such as `gm`, press `Ctrl/⌘ K`, paste a link anywhere to save it to the Inbox, press `Shift A` to change the look, and press `?` for every shortcut.

## Configure

You can change everything in the browser: right-click a link, card or page tab for its options, press `Shift N` to add a bookmark, and `Shift S` for settings. Your changes save as you go.

To change what **new visitors** see, edit the defaults block near the top of `index.html`:

```html
<script id="dash-defaults" type="application/json">
{
  "storageKey": "dashboard",
  "title": "Dashboard",
  "pages": [
    { "name": "Productivity", "categories": [
      { "name": "Mail", "icon": "📬", "bookmarks": [
        { "name": "Gmail", "url": "https://mail.google.com/", "tags": ["email"], "shortcut": "gm" }
      ] },
      { "name": "Stocks", "icon": "📈", "type": "stocks", "symbols": ["AMEX:SPY", "NASDAQ:AAPL"] }
    ] }
  ],
  "clocks": [
    { "label": "London", "timeZone": "Europe/London", "lat": 51.51, "lon": -0.13, "unit": "celsius" }
  ],
  "settings": { "theme": "cocoa", "mode": "system" }
}
</script>
```

**The easy way:** set the dashboard up in the browser, choose **Settings → Data → Copy as defaults JSON**, and paste the result over the block.

| Field | Meaning |
| --- | --- |
| `storageKey` | Name for the saved data. Give each copy its own key, since browsers often treat all `file://` pages as one site. |
| `title` | The browser tab's name. |
| `pages[].categories[]` | Cards. `type` is `bookmarks` (default), `notes`, `calendar`, `clock`, `weather`, `stocks` or `search`. Optional: `icon`, `color`, `span` (1–2), `sort`, `content` (Markdown for notes), `symbols` (TradingView symbols for stocks). |
| `bookmarks[]` | `name`, `url`, and optional `tags`, `shortcut`, `notes`, `pinned`, `icon`. |
| `clocks[]` | `label`, an IANA `timeZone`, and optional `lat`, `lon`, `unit` (`celsius`/`fahrenheit`) for weather. |
| `finders[]` | Web searches: `key` is what you type, `%s` in `url` becomes your query. |
| `inbox[]`, `collections[]` | Links that start in the Inbox; saved filters such as `{ "name": "Work", "query": "tag:work" }`. |
| `settings` | Any setting below. |

<details>
<summary><b>Settings reference</b></summary>

| Key | Values (default first) |
| --- | --- |
| `theme` | `cocoa`, `nightcity`, `slate`, `fjord`, `dusk`, `ember`, `solar`, `rose`, `forest`, `ocean`, `sunset`, `mono`, `matrix` |
| `mode` | `system`, `light`, `dark` |
| `accent` | `""` (theme colour) or a hex colour |
| `style` | `solid`, `glass`, `outline`, `soft`, `terminal` |
| `headerStyle` | `accent`, `plain`, `filled`, `underline` |
| `font` | `sans`, `mono`, `serif`, `rounded` |
| `backdrop` | `dots`, `none`, `grid`, `gradient`, `aurora`, `stripes` |
| `backdropIntensity` | `35` (0–100) |
| `radius` | `12` (0–24) |
| `density` | `comfortable`, `compact`, `spacious` |
| `columns` | `0` (auto) or `1`–`6` |
| `favicons` | `google`, `duckduckgo`, `site`, `off` |
| `newTab` | `true` |
| `hour12` | `false` |
| `showSeconds` / `showDate` | `false` / `true` |
| `weather` | `true` |
| `weekStart` | `0` (Sunday) or `1` (Monday) |
| `defaultFinder` | `g` (any finder key) |
| `showShortcuts`, `showPinned`, `previews`, `legend`, `pasteToInbox` | `true` |
| `trashDays` | `30` |

</details>

**Existing visitors** keep their own copy. When you change the defaults, they get a banner to add the new links, replace their copy, or keep theirs.

**Moving your data:** **Settings → Data** exports a JSON backup, browser-format HTML or CSV, and imports backups, browser bookmark exports, CSV or a list of URLs.

## Built-in bookmarks

Three pages come pre-filled: **Productivity**, **News** and **Finance** (with a Stocks card for SPY, AAPL and GOOGL). Type a shortcut on the page to open its link.

<details>
<summary><b>Productivity</b></summary>

| Card | Link | Shortcut |
| --- | --- | --- |
| Mail & Calendar | [Gmail](https://mail.google.com/) | `gm` |
| Mail & Calendar | [Google Calendar](https://calendar.google.com/) | `gc` |
| Tools | [GitHub](https://github.com/) | `gh` |
| Tools | [ChatGPT](https://chatgpt.com/) | `ai` |
| Tools | [Claude](https://claude.ai/) | `cl` |
| Tools | [Gemini](https://gemini.google.com/) | `gi` |
| Tools | [DuckDuckGo](https://duckduckgo.com/) | `dd` |
| Files | [Google Drive](https://drive.google.com/) | `gd` |
| Files | [Dropbox](https://www.dropbox.com/home) | `db` |
| Personal | [Google Maps](https://www.google.com/maps) | `map` |
| Personal | [YouTube](https://www.youtube.com/) | `yt` |
| Personal | [Google Flights](https://www.google.com/travel/flights) | `fl` |
| Personal | [Every Time Zone](https://everytimezone.com/) | `et` |
| Personal | [Windy](https://www.windy.com/) | `wi` |
| Social | [LinkedIn](https://www.linkedin.com/) | `li` |
| Social | [WhatsApp Web](https://web.whatsapp.com/) | `wa` |
| Social | [Instagram](https://www.instagram.com/) | `ig` |
| Social | [X](https://x.com/) | `x` |
| Social | [Reddit](https://www.reddit.com/) | `rd` |

</details>

<details>
<summary><b>News</b></summary>

| Card | Link | Shortcut |
| --- | --- | --- |
| News | [AP News](https://apnews.com/) | `ap` |
| News | [BBC News](https://www.bbc.com/news) | `bbc` |
| News | [The Guardian](https://www.theguardian.com/) | `gu` |
| News | [Al Jazeera](https://www.aljazeera.com/) | `aj` |
| News | [The Age](https://www.theage.com.au/) | `ta` |
| News | [Politico Europe](https://www.politico.eu/) | `pe` |
| News | [AP Politics](https://apnews.com/politics) | `us` |
| News | [Kagi News](https://news.kagi.com/) | `kn` |
| Sports | [ESPN](https://www.espn.com/) | `es` |
| Sports | [BBC Sport](https://www.bbc.com/sport) | `bs` |
| Sports | [BBC Football](https://www.bbc.com/sport/football) | `bf` |
| Sports | [FotMob](https://www.fotmob.com/) | `fm` |
| Sports | [Tennis.com](https://www.tennis.com/) | `tn` |
| Sports | [Formula 1](https://www.formula1.com/) | `f1` |
| Tech News | [Hacker News](https://news.ycombinator.com/) | `hn` |
| Tech News | [Ars Technica](https://arstechnica.com/) | `at` |
| Tech News | [Crunchbase News](https://news.crunchbase.com/) | `cb` |
| AI | [Anthropic News](https://www.anthropic.com/news) | `an` |
| AI | [OpenAI News](https://openai.com/news/) | `oa` |
| AI | [Google DeepMind Blog](https://deepmind.google/blog/) | `dm` |
| AI | [Latent Space](https://latent.space/) | `ls` |
| AI | [Simon Willison](https://simonwillison.net/) | `sw` |
| Engineering | [Cloudflare Blog](https://blog.cloudflare.com/) | `cf` |
| Engineering | [Stripe Engineering](https://stripe.dev/blog/topic/engineering) | `st` |
| Engineering | [Netflix Tech Blog](https://netflixtechblog.com/) | `nf` |
| Engineering | [GitHub Engineering](https://github.blog/engineering/) | `ge` |
| Engineering | [Jane Street Tech Blog](https://blog.janestreet.com/) | `js` |
| Engineering | [Meta Engineering](https://engineering.fb.com/) | `me` |
| Engineering | [Google Research Blog](https://research.google/blog/) | `gr` |

</details>

<details>
<summary><b>Finance</b></summary>

| Card | Link | Shortcut |
| --- | --- | --- |
| Finance News | [Reuters Business](https://www.reuters.com/business/) | `rt` |
| Finance News | [AP Business](https://apnews.com/business) | `ab` |
| Finance News | [Bloomberg](https://www.bloomberg.com/) | `bl` |
| Finance News | [Financial Times](https://www.ft.com/) | `ft` |
| Finance News | [The Economist](https://www.economist.com/) | `ec` |
| Finance News | [Wall Street Journal](https://www.wsj.com/) | `wsj` |
| Finance News | [Barron's](https://www.barrons.com/) | `ba` |
| Finance Tools | [Google Finance](https://www.google.com/finance/) | `gf` |
| Finance Tools | [Yahoo Finance](https://finance.yahoo.com/) | `yf` |
| Finance Tools | [TradingView](https://www.tradingview.com/) | `tv` |
| Finance Tools | [Finviz](https://finviz.com/) | `fv` |
| Finance Tools | [FRED](https://fred.stlouisfed.org/) | `fr` |
| Finance Tools | [SEC EDGAR](https://www.sec.gov/edgar/search/) | `sec` |
| Finance Tools | [Morningstar](https://www.morningstar.com/) | `ms` |
| Finance Tools | [Portfolio Visualizer](https://www.portfoliovisualizer.com/) | `pv` |
| Finance Tools | [Bogleheads](https://www.bogleheads.org/) | `bh` |
| Commentary & Data | [Abnormal Returns](https://abnormalreturns.com/) | `ar` |
| Commentary & Data | [Calculated Risk](https://www.calculatedriskblog.com/) | `cr` |
| Commentary & Data | [A Wealth of Common Sense](https://awealthofcommonsense.com/) | `wc` |
| Commentary & Data | [Of Dollars and Data](https://ofdollarsanddata.com/) | `od` |
| Commentary & Data | [Apollo Daily Spark](https://www.apolloacademy.com/the-daily-spark/) | `sp` |
| Commentary & Data | [Federal Reserve](https://www.federalreserve.gov/) | `fed` |
| Economists | [Marginal Revolution](https://marginalrevolution.com/) | `mr` |
| Economists | [Apricitas Economics](https://www.apricitas.io/) | `ae` |
| Economists | [Claudia Sahm](https://stayathomemacro.substack.com/) | `cs` |
| Economists | [Conversable Economist](https://conversableeconomist.com/) | `ce` |
| Economists | [The Grumpy Economist](https://www.johnhcochrane.com/) | `jc` |
| Economists | [Paul Krugman](https://paulkrugman.substack.com/) | `pk` |
| Economists | [Brad DeLong](https://braddelong.substack.com/) | `bd` |
| Economists | [Adam Tooze – Chartbook](https://adamtooze.substack.com/) | `tz` |
| Economists | [Noahpinion](https://www.noahpinion.blog/) | `np` |
| Economists | [Robert Shiller Data](https://shillerdata.com/) | `rs` |
| Economists | [Peterson Institute (PIIE)](https://www.piie.com/) | `pi` |

</details>

## Keyboard shortcuts

Press `?` in the app for the full, searchable list.

| Keys | Action |
| --- | --- |
| letters | Open a bookmark by its shortcut |
| `Ctrl/⌘ K` | Search bookmarks, commands (`:`), tags (`#`) and the web |
| `1`–`9`, `[` `]` | Switch pages |
| `Shift N` / `C` / `P` / `W` | New bookmark / card / page / widget |
| `Shift B` / `I` / `T` | Bookmarks table / Inbox / Trash |
| `Shift A` / `D` / `S` | Look studio / light–dark / Settings |
| `Shift O` | Weather forecast |
| `Ctrl/⌘ V` | Save a copied link to the Inbox |
| Double-click a tab | Rename the page |
| Click a clock / stock | Hourly and 7-day weather / price chart from 1W to 5Y |

**Search filters** combine with words: `tag:ai`, `page:finance`, `site:github.com`, `is:pinned`, `opened:never`, `added:<7d`, `-word`. **Web finders:** `g`, `d`, `gm`, `gh`, `yt`, `w`, `m`, `$`, `fred`, then your query; add more in Settings → Search.

## Privacy

Your dashboard lives in your browser's `localStorage` and is never uploaded. The page only makes these requests:

- **Site icons** from the icon service you pick (or none with **Letters only**).
- **Weather** and city search from [Open-Meteo](https://open-meteo.com/) (no key; data [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)), sending only each clock city's coordinates.
- **Stock charts** as [TradingView](https://www.tradingview.com/) embeds, while a Stocks card is on screen.
- **Link checks**, only when you run one.

Clearing your browser's site data erases the dashboard, so export a backup if you've customised a lot.

## Contributing

It's all in `index.html`: vanilla JavaScript, no dependencies. After changing the UI, re-record the tour with [uv](https://docs.astral.sh/uv/) and Edge or Chrome installed:

```sh
uv run tools/record-demo.py            # every frame
uv run tools/record-demo.py 07-finance # just one
```

## License

[MIT](LICENSE)
