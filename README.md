# Transit Card Scraper
Pull data about your transit cards. Currently supporting:
* [Myki](https://www.mymyki.com.au/) - Melbourne, Australia
* [GoCard](https://gocard.translink.com.au/) - Brisbane, Australia

You need to have already registered for accounts with these services.

This also syncs the scraped data to a Firebase Realtime database which will also
have to be setup separately.

Rename `.env-example` to `.env` and fill in your details.

## Development

You'll need to have Python 3 installed before doing anything.

To get up going run:

```bash
bin/setup
```
