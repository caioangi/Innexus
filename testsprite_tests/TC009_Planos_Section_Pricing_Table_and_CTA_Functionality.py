import asyncio
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None
    
    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()
        
        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",         # Set the browser window size
                "--disable-dev-shm-usage",        # Avoid using /dev/shm which can cause issues in containers
                "--ipc=host",                     # Use host-level IPC for better stability
                "--single-process"                # Run the browser in a single process mode
            ],
        )
        
        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        context.set_default_timeout(5000)
        
        # Open a new page in the browser context
        page = await context.new_page()
        
        # Navigate to your target URL and wait until the network request is committed
        await page.goto("http://localhost:5173", wait_until="commit", timeout=10000)
        
        # Wait for the main page to reach DOMContentLoaded state (optional for stability)
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
        except async_api.Error:
            pass
        
        # Iterate through all iframes and wait for them to load as well
        for frame in page.frames:
            try:
                await frame.wait_for_load_state("domcontentloaded", timeout=3000)
            except async_api.Error:
                pass
        
        # Interact with the page elements to simulate user flow
        # -> Scroll down to locate the Planos pricing section.
        await page.mouse.wheel(0, 600)
        

        # -> Scroll further down to locate the Planos pricing section.
        await page.mouse.wheel(0, 800)
        

        # -> Scroll down more to find the Planos pricing section.
        await page.mouse.wheel(0, 1000)
        

        # -> Click the CTA button on the START plan and verify the action triggered.
        frame = context.pages[-1]
        # Click the CTA button 'Começar Agora' on the START plan
        elem = frame.locator('xpath=html/body/div/div/section[7]/div/div[2]/div/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Click the CTA button on the SCALE plan (index 9) to test its functionality.
        frame = context.pages[-1]
        # Click the CTA button 'Começar Agora' on the SCALE plan to test its functionality.
        elem = frame.locator('xpath=html/body/div/div/section[7]/div/div[2]/div[3]/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # --> Assertions to verify final state
        frame = context.pages[-1]
        await expect(frame.locator('text=START').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=GROW').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=MAIS POPULAR').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=SCALE').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Presença digital básica').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=1 solução por mês').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=1 automação simples').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Suporte técnico').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Entrega inicial 48h').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Soluções ilimitadas moderadas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Até 4 automações').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Integrações avançadas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Suporte mensal').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Gestão de funis').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Relatório mensal').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Soluções digitais ilimitadas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Automações ilimitadas').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Consultoria tech').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Construção de apps/sistemas leves').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Evolução contínua').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Prioridade total').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Começar Agora').nth(0)).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Começar Agora').nth(1)).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Começar Agora').nth(2)).to_be_visible(timeout=30000)
        await asyncio.sleep(5)
    
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
            
asyncio.run(run_test())
    