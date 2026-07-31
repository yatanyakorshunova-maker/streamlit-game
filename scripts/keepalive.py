import asyncio
from playwright.async_api import async_playwright

# Ссылка на твоё приложение
APP_URL = "https://tvoi-app.streamlit.app/"

async def wake_app():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(APP_URL, wait_until="domcontentloaded", timeout=120000)
        await page.wait_for_timeout(5000)
        
        # Ищем кнопку пробуждения
        wake_button = page.get_by_role("button", name="Yes, get this app back up!")
        
        if await wake_button.count() > 0:
            print(f"🔁 Приложение спит. Бужу... {APP_URL}")
            await wake_button.click()
            await page.wait_for_timeout(60000)  # ждём, пока проснётся
        else:
            print(f"✅ Приложение уже активно: {APP_URL}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(wake_app())
