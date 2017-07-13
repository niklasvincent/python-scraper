
def test_scraper():
    from . import Scraper
    scraper = Scraper(cache_expiry=1, cache_name="test")
    html = scraper.get("http://testing-ground.scraping.pro/textlist")
    content = html.find("div", {"id": "case_textlist"}).decode_contents()
    assert "CITY" in content
